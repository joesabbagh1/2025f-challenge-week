package com.epita.foodguide;

import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.epita.foodguide.api.ApiClient;
import com.epita.foodguide.model.Restaurant;

import org.json.JSONObject;

public class RestaurantDetailActivity extends AppCompatActivity {

    private static final String TAG = "RestaurantDetail";

    private TextView nameText;
    private TextView cuisineText;
    private TextView addressText;
    private LinearLayout starsContainer;
    private LinearLayout priceContainer;
    private TextView ratingText;
    private TextView reviewCountText;
    private RecyclerView reviewsRecycler;
    private TextView reviewsPlaceholder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurant_detail);

        nameText = findViewById(R.id.detail_name);
        cuisineText = findViewById(R.id.detail_cuisine);
        addressText = findViewById(R.id.detail_address);
        starsContainer = findViewById(R.id.detail_stars);
        priceContainer = findViewById(R.id.detail_price);
        ratingText = findViewById(R.id.detail_rating);
        reviewCountText = findViewById(R.id.detail_review_count);
        reviewsRecycler = findViewById(R.id.reviews_recycler);
        reviewsPlaceholder = findViewById(R.id.reviews_placeholder);

        reviewsRecycler.setLayoutManager(new LinearLayoutManager(this));

        int restaurantId = getIntent().getIntExtra("restaurant_id", -1);
        String restaurantName = getIntent().getStringExtra("restaurant_name");

        if (getSupportActionBar() != null) {
            getSupportActionBar().setTitle(restaurantName);
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        if (restaurantId != -1) {
            loadRestaurantDetail(restaurantId);
        }
    }

    private void loadRestaurantDetail(int restaurantId) {
        ApiClient.get("/restaurants/" + restaurantId, new ApiClient.Callback() {
            @Override
            public void onSuccess(String responseBody) {
                try {
                    JSONObject json = new JSONObject(responseBody);
                    Restaurant restaurant = Restaurant.fromJson(json);
                    displayRestaurant(restaurant);
                } catch (Exception e) {
                    Log.e(TAG, "Error parsing restaurant detail", e);
                }
            }

            @Override
            public void onError(String error) {
                Log.e(TAG, "API error: " + error);
                Toast.makeText(RestaurantDetailActivity.this,
                        "Error loading details", Toast.LENGTH_SHORT).show();
            }
        });

        // TODO: Load reviews for this restaurant using GET /restaurants/<id>/reviews
        //       Parse the JSON array into List<Review>, create a ReviewAdapter,
        //       set it on reviewsRecycler, and hide reviewsPlaceholder.
    }

    private void displayRestaurant(Restaurant restaurant) {
        nameText.setText(restaurant.getName());
        cuisineText.setText(restaurant.getCuisine());
        addressText.setText(restaurant.getAddress());
        ratingText.setText(String.format("%.1f", restaurant.getAvgRating()));
        reviewCountText.setText(restaurant.getReviewCount() + " reviews");

        // Display stars
        starsContainer.removeAllViews();
        int fullStars = (int) Math.round(restaurant.getAvgRating());
        for (int i = 0; i < 5; i++) {
            ImageView star = new ImageView(this);
            star.setLayoutParams(new LinearLayout.LayoutParams(64, 64));
            if (i < fullStars) {
                star.setImageResource(R.drawable.star_filled);
            } else {
                star.setImageResource(R.drawable.star_empty);
            }
            starsContainer.addView(star);
        }

        // Display price
        priceContainer.removeAllViews();
        for (int i = 0; i < restaurant.getPriceRange(); i++) {
            ImageView euro = new ImageView(this);
            euro.setLayoutParams(new LinearLayout.LayoutParams(48, 48));
            euro.setImageResource(R.drawable.euro_icon);
            priceContainer.addView(euro);
        }
    }

    @Override
    public boolean onSupportNavigateUp() {
        finish();
        return true;
    }
}
