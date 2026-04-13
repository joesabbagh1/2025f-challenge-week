package com.epita.foodguide.adapter;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.epita.foodguide.R;
import com.epita.foodguide.model.Restaurant;

import java.util.ArrayList;
import java.util.List;

public class RestaurantAdapter extends RecyclerView.Adapter<RestaurantAdapter.ViewHolder> {

    public interface OnItemClickListener {
        void onItemClick(Restaurant restaurant);
    }

    private List<Restaurant> restaurants = new ArrayList<>();
    private OnItemClickListener listener;

    public RestaurantAdapter(OnItemClickListener listener) {
        this.listener = listener;
    }

    public void setRestaurants(List<Restaurant> restaurants) {
        this.restaurants = restaurants;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_restaurant, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Restaurant restaurant = restaurants.get(position);
        holder.bind(restaurant, listener);
    }

    @Override
    public int getItemCount() {
        return restaurants.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        private final TextView nameText;
        private final TextView cuisineText;
        private final TextView ratingText;
        private final LinearLayout starsContainer;
        private final TextView reviewCountText;
        private final LinearLayout priceContainer;

        ViewHolder(View itemView) {
            super(itemView);
            nameText = itemView.findViewById(R.id.restaurant_name);
            cuisineText = itemView.findViewById(R.id.restaurant_cuisine);
            ratingText = itemView.findViewById(R.id.restaurant_rating);
            starsContainer = itemView.findViewById(R.id.stars_container);
            reviewCountText = itemView.findViewById(R.id.review_count);
            priceContainer = itemView.findViewById(R.id.price_container);
        }

        void bind(Restaurant restaurant, OnItemClickListener listener) {
            nameText.setText(restaurant.getName());
            cuisineText.setText(restaurant.getCuisine());
            ratingText.setText(String.format("%.1f", restaurant.getAvgRating()));

            // Display star icons
            starsContainer.removeAllViews();
            int fullStars = (int) Math.round(restaurant.getAvgRating());
            for (int i = 0; i < 5; i++) {
                ImageView star = new ImageView(itemView.getContext());
                star.setLayoutParams(new LinearLayout.LayoutParams(48, 48));
                if (i < fullStars) {
                    star.setImageResource(R.drawable.star_filled);
                } else {
                    star.setImageResource(R.drawable.star_empty);
                }
                starsContainer.addView(star);
            }

            // Display review count
            reviewCountText.setText("(" + restaurant.getReviewCount() + " reviews)");

            // Display price icons
            priceContainer.removeAllViews();
            for (int i = 0; i < restaurant.getPriceRange(); i++) {
                ImageView euro = new ImageView(itemView.getContext());
                euro.setLayoutParams(new LinearLayout.LayoutParams(36, 36));
                euro.setImageResource(R.drawable.euro_icon);
                priceContainer.addView(euro);
            }

            itemView.setOnClickListener(v -> listener.onItemClick(restaurant));
        }
    }
}
