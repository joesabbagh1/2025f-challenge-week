package com.epita.flashcards;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

/**
 * Review screen -- displays one card at a time with a flip animation.
 *
 * The {@link FlipAnimationHelper} is already set up and ready to use.
 *
 * TODO: Students should implement this activity to:
 *   1. Fetch cards from the API (or receive them via Intent)
 *   2. Display question on the front, answer on the back
 *   3. Let the user tap to flip the card (already wired below)
 *   4. Add difficulty buttons (Easy / Medium / Hard)
 *   5. PATCH /cards/{id} to update difficulty and last_reviewed
 *   6. Navigate to the next card after rating
 */
public class ReviewActivity extends AppCompatActivity {

    private FlipAnimationHelper flipHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_review);

        int deckId = getIntent().getIntExtra("deck_id", -1);

        // -----------------------------------------------------------------
        // Flip animation is ready to use!
        // -----------------------------------------------------------------
        View cardFront = findViewById(R.id.card_front);
        View cardBack = findViewById(R.id.card_back);
        flipHelper = new FlipAnimationHelper(cardFront, cardBack);

        View cardContainer = findViewById(R.id.card_container);
        cardContainer.setOnClickListener(v -> flipHelper.flip());

        // TODO: Load cards for this deck
        // TODO: Display the first card's question and answer
        // TODO: Add difficulty rating buttons and PATCH endpoint calls
    }
}
