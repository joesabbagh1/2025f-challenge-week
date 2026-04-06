# Study Flashcards -- iOS

## Setup

1. Open `ios/StudyFlashcards.xcodeproj` (or create one in Xcode with these files).
2. Make sure the backend is running on `localhost:5000`.
3. Build and run on a simulator (localhost works out of the box).
4. For a physical device, update `APIClient.baseURL` to your machine's local IP
   and ensure `NSAllowsLocalNetworking` is enabled in `Info.plist`.

## Architecture

| File | Role |
|------|------|
| `Models/Deck.swift` | Codable struct for deck JSON |
| `Models/Card.swift` | Codable struct for card JSON |
| `Services/APIClient.swift` | URLSession-based HTTP client (async/await) |
| `Views/DeckListViewController.swift` | Main screen -- lists all decks |
| `Views/DeckDetailViewController.swift` | **TODO** -- show cards in a deck |
| `Views/ReviewViewController.swift` | **TODO** -- review cards with flip animation |
| `Helpers/FlipAnimationHelper.swift` | Provided UIView extension for 3D flip |

## What to implement

See the main project README for the full list of TODOs.
