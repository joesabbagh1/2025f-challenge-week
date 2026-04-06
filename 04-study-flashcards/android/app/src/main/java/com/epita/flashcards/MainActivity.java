package com.epita.flashcards;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.epita.flashcards.adapter.DeckAdapter;
import com.epita.flashcards.api.ApiClient;
import com.epita.flashcards.model.Deck;

import java.util.List;
import java.util.concurrent.Executors;

/**
 * Main screen -- displays all flashcard decks in a RecyclerView.
 *
 * Tapping a deck opens {@link DeckActivity}.
 */
public class MainActivity extends AppCompatActivity {

    private DeckAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RecyclerView recyclerView = findViewById(R.id.decks_recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        adapter = new DeckAdapter(deck -> {
            Intent intent = new Intent(MainActivity.this, DeckActivity.class);
            intent.putExtra("deck_id", deck.getId());
            intent.putExtra("deck_name", deck.getName());
            startActivity(intent);
        });
        recyclerView.setAdapter(adapter);

        loadDecks();
    }

    @Override
    protected void onResume() {
        super.onResume();
        loadDecks();
    }

    private void loadDecks() {
        Executors.newSingleThreadExecutor().execute(() -> {
            try {
                List<Deck> decks = ApiClient.getDecks();
                runOnUiThread(() -> adapter.setDecks(decks));
            } catch (Exception e) {
                runOnUiThread(() ->
                    Toast.makeText(this, "Failed to load decks: " + e.getMessage(),
                            Toast.LENGTH_LONG).show()
                );
            }
        });
    }
}
