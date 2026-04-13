import Foundation

struct Restaurant: Codable {
    let id: Int
    let name: String
    let cuisine: String
    let address: String?
    let priceRange: Int
    let imageUrl: String?
    let avgRating: Double?
    let reviewCount: Int?

    enum CodingKeys: String, CodingKey {
        case id, name, cuisine, address
        case priceRange = "price_range"
        case imageUrl = "image_url"
        case avgRating = "avg_rating"
        case reviewCount = "review_count"
    }

    /// Returns a string of euro signs matching the price range (1-3).
    var priceLabel: String {
        String(repeating: "\u{20AC}", count: priceRange)
    }

    /// Rounded average rating for display.
    var displayRating: String {
        guard let avg = avgRating else { return "N/A" }
        return String(format: "%.1f", avg)
    }
}
