import Foundation

/// Simple API client for communicating with the Flask backend.
class APIClient {

    // Change this to your Mac's local IP if testing on a physical device.
    static let baseURL = "http://localhost:5000"

    enum APIError: Error {
        case invalidURL
        case noData
        case decodingError(Error)
        case httpError(Int)
    }

    /// Fetch all restaurants from the backend.
    static func getRestaurants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        get(path: "/restaurants", completion: completion)
    }

    /// Fetch a single restaurant by ID.
    static func getRestaurant(id: Int, completion: @escaping (Result<Restaurant, Error>) -> Void) {
        get(path: "/restaurants/\(id)", completion: completion)
    }

    /// Fetch reviews for a restaurant.
    static func getReviews(restaurantId: Int, completion: @escaping (Result<[Review], Error>) -> Void) {
        get(path: "/restaurants/\(restaurantId)/reviews", completion: completion)
    }

    // MARK: - Private

    private static func get<T: Decodable>(path: String, completion: @escaping (Result<T, Error>) -> Void) {
        guard let url = URL(string: baseURL + path) else {
            completion(.failure(APIError.invalidURL))
            return
        }

        URLSession.shared.dataTask(with: url) { data, response, error in
            if let error = error {
                DispatchQueue.main.async { completion(.failure(error)) }
                return
            }

            if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode != 200 {
                DispatchQueue.main.async { completion(.failure(APIError.httpError(httpResponse.statusCode))) }
                return
            }

            guard let data = data else {
                DispatchQueue.main.async { completion(.failure(APIError.noData)) }
                return
            }

            do {
                let decoded = try JSONDecoder().decode(T.self, from: data)
                DispatchQueue.main.async { completion(.success(decoded)) }
            } catch {
                DispatchQueue.main.async { completion(.failure(APIError.decodingError(error))) }
            }
        }.resume()
    }
}
