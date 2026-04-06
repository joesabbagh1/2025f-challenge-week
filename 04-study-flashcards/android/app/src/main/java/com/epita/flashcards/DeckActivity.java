package com.epita.flashcards;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

/**
 * Deck detail screen -- shows cards belonging to a deck.
 *
 * TODO: Students should implement this activity to:
 *   1. Fetch cards from GET /decks/{id}/cards using ApiClient.getCards()
 *   2. Display them in a RecyclerView (create a CardAdapter)
 *   3. Add a "Start Review" button that opens ReviewActivity
 */
public class DeckActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_deck);

        int deckId = getIntent().getIntExtra("deck_id", -1);
        String deckName = getIntent().getStringExtra("deck_name");

        TextView title = findViewById(R.id.deck_title);
        title.setText(deckName != null ? deckName : "Deck");

        // TODO: Load and display cards for this deck
        // TODO: Add a "Start Review" button
    }
}
