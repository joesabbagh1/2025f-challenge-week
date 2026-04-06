package com.epita.flashcards.model;

/**
 * Plain data class representing a flashcard deck.
 */
public class Deck {
    private int id;
    private String name;
    private String description;
    private String createdAt;
    private int cardCount;

    public Deck() {}

    public Deck(int id, String name, String description, String createdAt, int cardCount) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.createdAt = createdAt;
        this.cardCount = cardCount;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getCreatedAt() { return createdAt; }
    public void setCreatedAt(String createdAt) { this.createdAt = createdAt; }

    public int getCardCount() { return cardCount; }
    public void setCardCount(int cardCount) { this.cardCount = cardCount; }
}
