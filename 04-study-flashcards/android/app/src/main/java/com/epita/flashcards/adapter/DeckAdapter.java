package com.epita.flashcards.adapter;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.epita.flashcards.R;
import com.epita.flashcards.model.Deck;

import java.util.ArrayList;
import java.util.List;

/**
 * RecyclerView adapter that displays a list of flashcard decks.
 */
public class DeckAdapter extends RecyclerView.Adapter<DeckAdapter.ViewHolder> {

    public interface OnDeckClickListener {
        void onDeckClick(Deck deck);
    }

    private List<Deck> decks = new ArrayList<>();
    private OnDeckClickListener listener;

    public DeckAdapter(OnDeckClickListener listener) {
        this.listener = listener;
    }

    public void setDecks(List<Deck> decks) {
        this.decks = decks;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_deck, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Deck deck = decks.get(position);
        holder.nameText.setText(deck.getName());
        holder.countText.setText(deck.getCardCount() + " cards");
        holder.descriptionText.setText(deck.getDescription());
        holder.itemView.setOnClickListener(v -> {
            if (listener != null) listener.onDeckClick(deck);
        });
    }

    @Override
    public int getItemCount() {
        return decks.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView nameText;
        TextView countText;
        TextView descriptionText;

        ViewHolder(@NonNull View itemView) {
            super(itemView);
            nameText = itemView.findViewById(R.id.deck_name);
            countText = itemView.findViewById(R.id.deck_card_count);
            descriptionText = itemView.findViewById(R.id.deck_description);
        }
    }
}
