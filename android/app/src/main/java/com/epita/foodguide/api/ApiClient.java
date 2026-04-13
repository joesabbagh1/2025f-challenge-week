package com.epita.foodguide.api;

import android.os.Handler;
import android.os.Looper;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Simple HTTP client for communicating with the Flask backend.
 * Uses a background thread pool and posts results back to the main thread.
 */
public class ApiClient {

    // Change this to your computer's local IP if testing on a physical device
    private static final String BASE_URL = "http://10.0.2.2:5000";

    private static final ExecutorService executor = Executors.newFixedThreadPool(4);
    private static final Handler mainHandler = new Handler(Looper.getMainLooper());

    public interface Callback {
        void onSuccess(String responseBody);
        void onError(String error);
    }

    /**
     * Perform a GET request in the background.
     *
     * @param path     API path, e.g. "/restaurants"
     * @param callback called on the main thread with the result
     */
    public static void get(String path, Callback callback) {
        executor.execute(() -> {
            try {
                URL url = new URL(BASE_URL + path);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setConnectTimeout(5000);
                conn.setReadTimeout(5000);

                int code = conn.getResponseCode();
                if (code == HttpURLConnection.HTTP_OK) {
                    BufferedReader reader = new BufferedReader(
                            new InputStreamReader(conn.getInputStream()));
                    StringBuilder sb = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        sb.append(line);
                    }
                    reader.close();
                    String body = sb.toString();
                    mainHandler.post(() -> callback.onSuccess(body));
                } else {
                    mainHandler.post(() -> callback.onError("HTTP " + code));
                }
                conn.disconnect();
            } catch (Exception e) {
                mainHandler.post(() -> callback.onError(e.getMessage()));
            }
        });
    }
}
