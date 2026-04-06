import UIKit

/// Review screen -- displays one card at a time with a flip animation.
///
/// The flip animation is provided via ``FlipAnimationHelper`` and is ready to use.
///
/// TODO: Students should implement this view controller to:
///   1. Fetch cards from the API (or receive them via init)
///   2. Display question on the front label, answer on the back label
///   3. Tap to flip the card (already wired below)
///   4. Add difficulty buttons (Easy / Medium / Hard)
///   5. PATCH /cards/{id} to update difficulty and last_reviewed
///   6. Navigate to the next card after rating
class ReviewViewController: UIViewController {

    private let deckId: Int
    private var cards: [Card] = []
    private var currentIndex = 0

    // Card views
    private let cardContainer = UIView()
    private let frontView = UIView()
    private let backView = UIView()
    private let questionLabel = UILabel()
    private let answerLabel = UILabel()

    init(deckId: Int) {
        self.deckId = deckId
        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Review"
        view.backgroundColor = .systemBackground
        setupCardViews()

        // -----------------------------------------------------------------
        // Flip animation is ready to use!
        // -----------------------------------------------------------------
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(cardTapped))
        cardContainer.addGestureRecognizer(tapGesture)

        // TODO: Load cards and populate questionLabel / answerLabel
    }

    // MARK: - UI Setup

    private func setupCardViews() {
        cardContainer.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(cardContainer)

        NSLayoutConstraint.activate([
            cardContainer.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 24),
            cardContainer.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -24),
            cardContainer.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -40),
            cardContainer.heightAnchor.constraint(equalToConstant: 250),
        ])

        // Front view (question)
        frontView.backgroundColor = .white
        frontView.layer.cornerRadius = 12
        frontView.layer.shadowColor = UIColor.black.cgColor
        frontView.layer.shadowOpacity = 0.1
        frontView.layer.shadowRadius = 8
        frontView.translatesAutoresizingMaskIntoConstraints = false
        cardContainer.addSubview(frontView)

        questionLabel.text = "Tap to load a card"
        questionLabel.textAlignment = .center
        questionLabel.numberOfLines = 0
        questionLabel.font = .systemFont(ofSize: 18)
        questionLabel.translatesAutoresizingMaskIntoConstraints = false
        frontView.addSubview(questionLabel)

        // Back view (answer)
        backView.backgroundColor = UIColor.systemBlue.withAlphaComponent(0.05)
        backView.layer.cornerRadius = 12
        backView.layer.shadowColor = UIColor.black.cgColor
        backView.layer.shadowOpacity = 0.1
        backView.layer.shadowRadius = 8
        backView.isHidden = true
        backView.translatesAutoresizingMaskIntoConstraints = false
        cardContainer.addSubview(backView)

        answerLabel.text = ""
        answerLabel.textAlignment = .center
        answerLabel.numberOfLines = 0
        answerLabel.font = .systemFont(ofSize: 16)
        answerLabel.translatesAutoresizingMaskIntoConstraints = false
        backView.addSubview(answerLabel)

        // Layout
        for v in [frontView, backView] {
            NSLayoutConstraint.activate([
                v.topAnchor.constraint(equalTo: cardContainer.topAnchor),
                v.bottomAnchor.constraint(equalTo: cardContainer.bottomAnchor),
                v.leadingAnchor.constraint(equalTo: cardContainer.leadingAnchor),
                v.trailingAnchor.constraint(equalTo: cardContainer.trailingAnchor),
            ])
        }

        for label in [questionLabel, answerLabel] {
            NSLayoutConstraint.activate([
                label.centerXAnchor.constraint(equalTo: label.superview!.centerXAnchor),
                label.centerYAnchor.constraint(equalTo: label.superview!.centerYAnchor),
                label.leadingAnchor.constraint(equalTo: label.superview!.leadingAnchor, constant: 16),
                label.trailingAnchor.constraint(equalTo: label.superview!.trailingAnchor, constant: -16),
            ])
        }
    }

    // MARK: - Flip

    @objc private func cardTapped() {
        frontView.flip3D(to: backView)
    }
}
