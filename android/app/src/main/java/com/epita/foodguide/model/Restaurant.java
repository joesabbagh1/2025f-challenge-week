package com.epita.foodguide.model;

import org.json.JSONException;
import org.json.JSONObject;

public class Restaurant {
    private int id;
    private String name;
    private String cuisine;
    private String address;
    private int priceRange;
    private String imageUrl;
    private double avgRating;
    private int reviewCount;

    public Restaurant() {}

    public static Restaurant fromJson(JSONObject json) throws JSONException {
        Restaurant r = new Restaurant();
        r.id = json.getInt("id");
        r.name = json.getString("name");
        r.cuisine = json.getString("cuisine");
        r.address = json.optString("address", "");
        r.priceRange = json.optInt("price_range", 2);
        r.imageUrl = json.optString("image_url", "");
        r.avgRating = json.optDouble("avg_rating", 0.0);
        r.reviewCount = json.optInt("review_count", 0);
        return r;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public String getCuisine() { return cuisine; }
    public String getAddress() { return address; }
    public int getPriceRange() { return priceRange; }
    public String getImageUrl() { return imageUrl; }
    public double getAvgRating() { return avgRating; }
    public int getReviewCount() { return reviewCount; }
}
