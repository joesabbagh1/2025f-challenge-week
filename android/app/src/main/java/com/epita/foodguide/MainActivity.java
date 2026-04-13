package com.epita.foodguide;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.epita.foodguide.adapter.RestaurantAdapter;
import com.epita.foodguide.api.ApiClient;
import com.epita.foodguide.model.Restaurant;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private RecyclerView recyclerView;
    private RestaurantAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.restaurants_recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        adapter = new RestaurantAdapter(restaurant -> {
            Intent intent = new Intent(MainActivity.this, RestaurantDetailActivity.class);
            intent.putExtra("restaurant_id", restaurant.getId());
            intent.putExtra("restaurant_name", restaurant.getName());
            startActivity(intent);
        });

        recyclerView.setAdapter(adapter);

        loadRestaurants();
    }

    private void loadRestaurants() {
        ApiClient.get("/restaurants", new ApiClient.Callback() {
            @Override
            public void onSuccess(String responseBody) {
                try {
                    JSONArray jsonArray = new JSONArray(responseBody);
                    List<Restaurant> restaurants = new ArrayList<>();
                    for (int i = 0; i < jsonArray.length(); i++) {
                        JSONObject obj = jsonArray.getJSONObject(i);
                        restaurants.add(Restaurant.fromJson(obj));
                    }
                    adapter.setRestaurants(restaurants);
                } catch (Exception e) {
                    Log.e(TAG, "Error parsing restaurants", e);
                    Toast.makeText(MainActivity.this,
                            "Error loading restaurants", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onError(String error) {
                Log.e(TAG, "API error: " + error);
                Toast.makeText(MainActivity.this,
                        "Cannot reach server: " + error, Toast.LENGTH_LONG).show();
            }
        });
    }
}
