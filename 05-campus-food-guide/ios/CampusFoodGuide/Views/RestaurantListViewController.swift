import UIKit

class RestaurantListViewController: UITableViewController {

    private var restaurants: [Restaurant] = []

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Campus Food Guide"
        navigationController?.navigationBar.prefersLargeTitles = true

        tableView.register(RestaurantCell.self, forCellReuseIdentifier: "RestaurantCell")
        tableView.rowHeight = UITableView.automaticDimension
        tableView.estimatedRowHeight = 90

        loadRestaurants()
    }

    private func loadRestaurants() {
        APIClient.getRestaurants { [weak self] result in
            switch result {
            case .success(let restaurants):
                self?.restaurants = restaurants
                self?.tableView.reloadData()
            case .failure(let error):
                print("Error loading restaurants: \(error)")
                let alert = UIAlertController(
                    title: "Error",
                    message: "Cannot reach server. Make sure the Flask backend is running on port 5000.",
                    preferredStyle: .alert
                )
                alert.addAction(UIAlertAction(title: "OK", style: .default))
                self?.present(alert, animated: true)
            }
        }
    }

    // MARK: - Table View Data Source

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return restaurants.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "RestaurantCell", for: indexPath) as! RestaurantCell
        cell.configure(with: restaurants[indexPath.row])
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        let detailVC = RestaurantDetailViewController()
        detailVC.restaurant = restaurants[indexPath.row]
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

// MARK: - Restaurant Cell

class RestaurantCell: UITableViewCell {

    private let nameLabel = UILabel()
    private let cuisineLabel = UILabel()
    private let starRatingView = StarRatingView()
    private let ratingLabel = UILabel()
    private let priceLabel = UILabel()

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupViews()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupViews() {
        nameLabel.font = .systemFont(ofSize: 17, weight: .semibold)
        nameLabel.textColor = .label

        cuisineLabel.font = .systemFont(ofSize: 14)
        cuisineLabel.textColor = .systemOrange

        ratingLabel.font = .systemFont(ofSize: 14, weight: .medium)
        ratingLabel.textColor = .secondaryLabel

        priceLabel.font = .systemFont(ofSize: 14)
        priceLabel.textColor = .systemGreen

        let ratingStack = UIStackView(arrangedSubviews: [starRatingView, ratingLabel, priceLabel])
        ratingStack.axis = .horizontal
        ratingStack.spacing = 8
        ratingStack.alignment = .center

        let mainStack = UIStackView(arrangedSubviews: [nameLabel, cuisineLabel, ratingStack])
        mainStack.axis = .vertical
        mainStack.spacing = 4
        mainStack.translatesAutoresizingMaskIntoConstraints = false

        contentView.addSubview(mainStack)
        NSLayoutConstraint.activate([
            mainStack.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 12),
            mainStack.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
            mainStack.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
            mainStack.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -12),
        ])
    }

    func configure(with restaurant: Restaurant) {
        nameLabel.text = restaurant.name
        cuisineLabel.text = restaurant.cuisine
        starRatingView.rating = restaurant.avgRating ?? 0
        ratingLabel.text = "\(restaurant.displayRating) (\(restaurant.reviewCount ?? 0))"
        priceLabel.text = restaurant.priceLabel
    }
}
