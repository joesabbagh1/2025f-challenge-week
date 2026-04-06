import UIKit

/// Deck detail screen -- shows the cards belonging to a deck.
///
/// TODO: Students should implement this view controller to:
///   1. Fetch cards from GET /decks/{id}/cards using APIClient.shared.getCards()
///   2. Display them in a UITableView
///   3. Add a "Start Review" button that pushes ReviewViewController
class DeckDetailViewController: UIViewController {

    private let deckId: Int
    private let deckName: String

    init(deckId: Int, deckName: String) {
        self.deckId = deckId
        self.deckName = deckName
        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = deckName
        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "TODO: Display cards for this deck"
        label.textColor = .secondaryLabel
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])

        // TODO: Load and display cards
        // TODO: Add a "Start Review" button
    }
}
