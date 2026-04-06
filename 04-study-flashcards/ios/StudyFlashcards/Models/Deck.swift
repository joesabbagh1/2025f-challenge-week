import Foundation

/// A flashcard deck containing multiple cards.
struct Deck: Codable, Identifiable {
    let id: Int
    let name: String
    let description: String?
    let createdAt: String?
    let cardCount: Int

    enum CodingKeys: String, CodingKey {
        case id, name, description
        case createdAt = "created_at"
        case cardCount = "card_count"
    }
}
