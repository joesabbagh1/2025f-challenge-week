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
import com.epita.foodguide.model.Review;

import java.util.ArrayList;
import java.util.List;

/**
 * Adapter for displaying reviews in a RecyclerView.
 * PROVIDED: Students will connect this adapter in RestaurantDetailActivity.
 */
public class ReviewAdapter extends RecyclerView.Adapter<ReviewAdapter.ViewHolder> {

    private List<Review> reviews = new ArrayList<>();

    public void setReviews(List<Review> reviews) {
        this.reviews = reviews;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_review, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.bind(reviews.get(position));
    }

    @Override
    public int getItemCount() {
        return reviews.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        private final TextView authorText;
        private final TextView commentText;
        private final LinearLayout starsContainer;
        private final TextView dateText;

        ViewHolder(View itemView) {
            super(itemView);
            authorText = itemView.findViewById(R.id.review_author);
            commentText = itemView.findViewById(R.id.review_comment);
            starsContainer = itemView.findViewById(R.id.review_stars);
            dateText = itemView.findViewById(R.id.review_date);
        }

        void bind(Review review) {
            authorText.setText(review.getAuthorName());
            commentText.setText(review.getComment());
            dateText.setText(review.getCreatedAt());

            // Display star icons
            starsContainer.removeAllViews();
            for (int i = 0; i < 5; i++) {
                ImageView star = new ImageView(itemView.getContext());
                star.setLayoutParams(new LinearLayout.LayoutParams(36, 36));
                if (i < review.getRating()) {
                    star.setImageResource(R.drawable.star_filled);
                } else {
                    star.setImageResource(R.drawable.star_empty);
                }
                starsContainer.addView(star);
            }
        }
    }
}
