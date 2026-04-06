import Foundation

/// A single flashcard with a question and answer.
struct Card: Codable, Identifiable {
    let id: Int
    let deckId: Int
    let question: String
    let answer: String
    let difficulty: Int
    let lastReviewed: String?

    enum CodingKeys: String, CodingKey {
        case id, question, answer, difficulty
        case deckId = "deck_id"
        case lastReviewed = "last_reviewed"
    }
}
