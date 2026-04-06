import UIKit

class RestaurantDetailViewController: UIViewController {

    var restaurant: Restaurant!

    private let scrollView = UIScrollView()
    private let contentStack = UIStackView()

    private let nameLabel = UILabel()
    private let cuisineLabel = UILabel()
    private let addressLabel = UILabel()
    private let starRatingView = StarRatingView()
    private let ratingLabel = UILabel()
    private let priceLabel = UILabel()
    private let reviewsTitleLabel = UILabel()
    private let reviewsPlaceholder = UILabel()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        title = restaurant.name

        setupLayout()
        displayRestaurant()

        // TODO: Load reviews from GET /restaurants/{id}/reviews using APIClient.getReviews()
        //       Parse the response into [Review], then create UIViews or table cells
        //       for each review showing: author name, star rating, comment, and date.
        //       Hide reviewsPlaceholder once reviews are loaded.
    }

    private func setupLayout() {
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(scrollView)
        NSLayoutConstraint.activate([
            scrollView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
        ])

        contentStack.axis = .vertical
        contentStack.spacing = 12
        contentStack.translatesAutoresizingMaskIntoConstraints = false
        scrollView.addSubview(contentStack)
        NSLayoutConstraint.activate([
            contentStack.topAnchor.constraint(equalTo: scrollView.topAnchor, constant: 20),
            contentStack.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor, constant: 20),
            contentStack.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor, constant: -20),
            contentStack.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor, constant: -20),
            contentStack.widthAnchor.constraint(equalTo: scrollView.widthAnchor, constant: -40),
        ])

        // Name
        nameLabel.font = .systemFont(ofSize: 28, weight: .bold)
        nameLabel.textColor = .label
        contentStack.addArrangedSubview(nameLabel)

        // Cuisine
        cuisineLabel.font = .systemFont(ofSize: 18)
        cuisineLabel.textColor = .systemOrange
        contentStack.addArrangedSubview(cuisineLabel)

        // Address
        addressLabel.font = .systemFont(ofSize: 15)
        addressLabel.textColor = .secondaryLabel
        contentStack.addArrangedSubview(addressLabel)

        // Rating row
        starRatingView.starSize = 22
        ratingLabel.font = .systemFont(ofSize: 18, weight: .semibold)
        ratingLabel.textColor = .label
        priceLabel.font = .systemFont(ofSize: 18)
        priceLabel.textColor = .systemGreen

        let ratingStack = UIStackView(arrangedSubviews: [starRatingView, ratingLabel, priceLabel])
        ratingStack.axis = .horizontal
        ratingStack.spacing = 10
        ratingStack.alignment = .center
        contentStack.addArrangedSubview(ratingStack)

        // Separator
        let separator = UIView()
        separator.backgroundColor = .separator
        separator.heightAnchor.constraint(equalToConstant: 1).isActive = true
        contentStack.addArrangedSubview(separator)

        // Reviews title
        reviewsTitleLabel.text = "Reviews"
        reviewsTitleLabel.font = .systemFont(ofSize: 22, weight: .bold)
        reviewsTitleLabel.textColor = .label
        contentStack.addArrangedSubview(reviewsTitleLabel)

        // Placeholder
        reviewsPlaceholder.text = "Reviews will appear here once loaded.\n\nTODO: Fetch reviews from the API and display them."
        reviewsPlaceholder.font = .systemFont(ofSize: 14)
        reviewsPlaceholder.textColor = .tertiaryLabel
        reviewsPlaceholder.numberOfLines = 0
        reviewsPlaceholder.textAlignment = .center
        contentStack.addArrangedSubview(reviewsPlaceholder)
    }

    private func displayRestaurant() {
        nameLabel.text = restaurant.name
        cuisineLabel.text = restaurant.cuisine
        addressLabel.text = restaurant.address ?? "Address not available"
        starRatingView.rating = restaurant.avgRating ?? 0
        ratingLabel.text = "\(restaurant.displayRating) (\(restaurant.reviewCount ?? 0) reviews)"
        priceLabel.text = restaurant.priceLabel
    }
}
