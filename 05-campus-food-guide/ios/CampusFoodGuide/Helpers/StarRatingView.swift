import UIKit

/// A reusable view that displays 1-5 stars using SF Symbols.
/// PROVIDED: Students use this view to display ratings throughout the app.
///
/// Usage:
///     let starView = StarRatingView()
///     starView.rating = 4.2  // Shows 4 filled stars, 1 empty
///     starView.starSize = 20
///     starView.filledColor = .systemYellow
///
class StarRatingView: UIStackView {

    // MARK: - Public properties

    /// The rating to display (0.0 - 5.0). Rounded to nearest integer for star display.
    var rating: Double = 0.0 {
        didSet { updateStars() }
    }

    /// Size of each star image.
    var starSize: CGFloat = 18 {
        didSet { updateStars() }
    }

    /// Color for filled stars.
    var filledColor: UIColor = .systemYellow {
        didSet { updateStars() }
    }

    /// Color for empty stars.
    var emptyColor: UIColor = .systemGray4 {
        didSet { updateStars() }
    }

    // MARK: - Init

    override init(frame: CGRect) {
        super.init(frame: frame)
        setup()
    }

    required init(coder: NSCoder) {
        super.init(coder: coder)
        setup()
    }

    private func setup() {
        axis = .horizontal
        spacing = 2
        alignment = .center
        distribution = .fill
        updateStars()
    }

    // MARK: - Private

    private func updateStars() {
        arrangedSubviews.forEach { $0.removeFromSuperview() }

        let roundedRating = Int(rating.rounded())

        for i in 1...5 {
            let isFilled = i <= roundedRating
            let symbolName = isFilled ? "star.fill" : "star"
            let color = isFilled ? filledColor : emptyColor

            let config = UIImage.SymbolConfiguration(pointSize: starSize, weight: .medium)
            let image = UIImage(systemName: symbolName, withConfiguration: config)

            let imageView = UIImageView(image: image)
            imageView.tintColor = color
            imageView.contentMode = .scaleAspectFit
            imageView.translatesAutoresizingMaskIntoConstraints = false
            imageView.widthAnchor.constraint(equalToConstant: starSize + 4).isActive = true
            imageView.heightAnchor.constraint(equalToConstant: starSize + 4).isActive = true

            addArrangedSubview(imageView)
        }
    }
}
