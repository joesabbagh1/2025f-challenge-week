package com.epita.foodguide.model;

import org.json.JSONException;
import org.json.JSONObject;

public class Review {
    private int id;
    private int restaurantId;
    private String authorName;
    private int rating;
    private String comment;
    private String createdAt;

    public Review() {}

    public static Review fromJson(JSONObject json) throws JSONException {
        Review r = new Review();
        r.id = json.getInt("id");
        r.restaurantId = json.getInt("restaurant_id");
        r.authorName = json.getString("author_name");
        r.rating = json.getInt("rating");
        r.comment = json.optString("comment", "");
        r.createdAt = json.optString("created_at", "");
        return r;
    }

    public int getId() { return id; }
    public int getRestaurantId() { return restaurantId; }
    public String getAuthorName() { return authorName; }
    public int getRating() { return rating; }
    public String getComment() { return comment; }
    public String getCreatedAt() { return createdAt; }
}
