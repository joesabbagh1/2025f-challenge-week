import UIKit

/// Displays all flashcard decks in a table view.
///
/// Tapping a deck navigates to ``DeckDetailViewController``.
class DeckListViewController: UITableViewController {

    private var decks: [Deck] = []

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Study Flashcards"
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "DeckCell")
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .add, target: self, action: #selector(addDeckTapped))
        loadDecks()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        loadDecks()
    }

    // MARK: - Data loading

    private func loadDecks() {
        Task {
            do {
                let fetched = try await APIClient.shared.getDecks()
                await MainActor.run {
                    self.decks = fetched
                    self.tableView.reloadData()
                }
            } catch {
                print("Failed to load decks: \(error)")
            }
        }
    }

    // MARK: - UITableViewDataSource

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return decks.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "DeckCell", for: indexPath)
        let deck = decks[indexPath.row]

        var config = cell.defaultContentConfiguration()
        config.text = deck.name
        config.secondaryText = "\(deck.cardCount) cards"
        cell.contentConfiguration = config
        cell.accessoryType = .disclosureIndicator

        return cell
    }

    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let deck = decks[indexPath.row]
        let vc = DeckDetailViewController(deckId: deck.id, deckName: deck.name)
        navigationController?.pushViewController(vc, animated: true)
    }

    // MARK: - Actions

    @objc private func addDeckTapped() {
        // TODO: Students can implement a "Create Deck" alert or screen
    }
}
