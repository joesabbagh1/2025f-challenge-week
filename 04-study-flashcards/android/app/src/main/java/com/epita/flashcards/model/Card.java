package com.epita.flashcards.model;

/**
 * Plain data class representing a flashcard.
 */
public class Card {
    private int id;
    private int deckId;
    private String question;
    private String answer;
    private int difficulty;
    private String lastReviewed;

    public Card() {}

    public Card(int id, int deckId, String question, String answer, int difficulty, String lastReviewed) {
        this.id = id;
        this.deckId = deckId;
        this.question = question;
        this.answer = answer;
        this.difficulty = difficulty;
        this.lastReviewed = lastReviewed;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public int getDeckId() { return deckId; }
    public void setDeckId(int deckId) { this.deckId = deckId; }

    public String getQuestion() { return question; }
    public void setQuestion(String question) { this.question = question; }

    public String getAnswer() { return answer; }
    public void setAnswer(String answer) { this.answer = answer; }

    public int getDifficulty() { return difficulty; }
    public void setDifficulty(int difficulty) { this.difficulty = difficulty; }

    public String getLastReviewed() { return lastReviewed; }
    public void setLastReviewed(String lastReviewed) { this.lastReviewed = lastReviewed; }
}
