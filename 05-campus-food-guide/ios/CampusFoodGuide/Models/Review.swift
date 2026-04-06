import Foundation

struct Review: Codable {
    let id: Int
    let restaurantId: Int
    let authorName: String
    let rating: Int
    let comment: String?
    let createdAt: String?

    enum CodingKeys: String, CodingKey {
        case id
        case restaurantId = "restaurant_id"
        case authorName = "author_name"
        case rating, comment
        case createdAt = "created_at"
    }
}
