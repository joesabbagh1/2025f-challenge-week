import Foundation

/// Lightweight HTTP client for the FastAPI backend.
///
/// All methods use async/await. The base URL points to localhost:5000 by default.
/// When running on a physical device, update `baseURL` to your machine's local IP.
class APIClient {

    static let shared = APIClient()

    /// Change this to your computer's IP if running on a physical device.
    private let baseURL = "http://localhost:5000"

    private let decoder: JSONDecoder = {
        let d = JSONDecoder()
        return d
    }()

    // MARK: - Decks

    /// Fetch all decks from GET /decks.
    func getDecks() async throws -> [Deck] {
        let url = URL(string: "\(baseURL)/decks")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try decoder.decode([Deck].self, from: data)
    }

    /// Fetch a single deck from GET /decks/{id}.
    func getDeck(id: Int) async throws -> Deck {
        let url = URL(string: "\(baseURL)/decks/\(id)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try decoder.decode(Deck.self, from: data)
    }

    /// Create a new deck via POST /decks.
    func createDeck(name: String, description: String?) async throws -> Deck {
        let url = URL(string: "\(baseURL)/decks")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        var body: [String: Any] = ["name": name]
        if let desc = description { body["description"] = desc }
        request.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (data, _) = try await URLSession.shared.data(for: request)
        return try decoder.decode(Deck.self, from: data)
    }

    // MARK: - Cards

    /// Fetch cards for a deck from GET /decks/{id}/cards.
    func getCards(deckId: Int) async throws -> [Card] {
        let url = URL(string: "\(baseURL)/decks/\(deckId)/cards")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try decoder.decode([Card].self, from: data)
    }
}
