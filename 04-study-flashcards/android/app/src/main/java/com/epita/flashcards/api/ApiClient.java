package com.epita.flashcards.api;

import com.epita.flashcards.model.Card;
import com.epita.flashcards.model.Deck;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * Lightweight HTTP helper that talks to the FastAPI backend.
 *
 * <p>All methods perform <b>synchronous</b> network I/O -- call them from a
 * background thread (e.g. {@code Executors.newSingleThreadExecutor()}).
 */
public class ApiClient {

    // 10.0.2.2 is the Android emulator alias for the host machine's localhost.
    private static final String BASE_URL = "http://10.0.2.2:5000";

    // ------------------------------------------------------------------
    // Public API
    // ------------------------------------------------------------------

    /** Fetch all decks from GET /decks. */
    public static List<Deck> getDecks() throws Exception {
        String json = get(BASE_URL + "/decks");
        JSONArray arr = new JSONArray(json);
        List<Deck> decks = new ArrayList<>();
        for (int i = 0; i < arr.length(); i++) {
            decks.add(parseDeck(arr.getJSONObject(i)));
        }
        return decks;
    }

    /** Fetch a single deck from GET /decks/{id}. */
    public static Deck getDeck(int deckId) throws Exception {
        String json = get(BASE_URL + "/decks/" + deckId);
        return parseDeck(new JSONObject(json));
    }

    /** Fetch cards for a deck from GET /decks/{id}/cards. */
    public static List<Card> getCards(int deckId) throws Exception {
        String json = get(BASE_URL + "/decks/" + deckId + "/cards");
        JSONArray arr = new JSONArray(json);
        List<Card> cards = new ArrayList<>();
        for (int i = 0; i < arr.length(); i++) {
            cards.add(parseCard(arr.getJSONObject(i)));
        }
        return cards;
    }

    /** Create a new deck via POST /decks. */
    public static Deck createDeck(String name, String description) throws Exception {
        JSONObject body = new JSONObject();
        body.put("name", name);
        body.put("description", description);
        String json = post(BASE_URL + "/decks", body.toString());
        return parseDeck(new JSONObject(json));
    }

    // ------------------------------------------------------------------
    // HTTP helpers
    // ------------------------------------------------------------------

    private static String get(String urlStr) throws Exception {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Accept", "application/json");
        return readResponse(conn);
    }

    private static String post(String urlStr, String jsonBody) throws Exception {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);
        try (OutputStream os = conn.getOutputStream()) {
            os.write(jsonBody.getBytes(StandardCharsets.UTF_8));
        }
        return readResponse(conn);
    }

    private static String readResponse(HttpURLConnection conn) throws Exception {
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        reader.close();
        return sb.toString();
    }

    // ------------------------------------------------------------------
    // JSON parsing
    // ------------------------------------------------------------------

    private static Deck parseDeck(JSONObject obj) throws Exception {
        return new Deck(
                obj.getInt("id"),
                obj.getString("name"),
                obj.optString("description", ""),
                obj.optString("created_at", ""),
                obj.optInt("card_count", 0)
        );
    }

    private static Card parseCard(JSONObject obj) throws Exception {
        return new Card(
                obj.getInt("id"),
                obj.getInt("deck_id"),
                obj.getString("question"),
                obj.getString("answer"),
                obj.optInt("difficulty", 1),
                obj.optString("last_reviewed", null)
        );
    }
}
