"""Seed the database with sample restaurants and reviews."""

from database import init_db, get_db

RESTAURANTS = [
    ("Sakura Ramen", "Japanese", "12 Rue du Campus", 2, "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400"),
    ("Bella Napoli", "Italian", "8 Avenue des Etudiants", 2, "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400"),
    ("Le Petit Bistrot", "French", "3 Place de la Fac", 3, "https://images.unsplash.com/photo-1550966871-3ed3cdb51f3a?w=400"),
    ("Bangkok Express", "Thai", "27 Rue de la Science", 1, "https://images.unsplash.com/photo-1559314809-0d155014e29e?w=400"),
    ("Casa Mexicana", "Mexican", "15 Boulevard du Savoir", 1, "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=400"),
    ("Taj Palace", "Indian", "42 Rue de l'Innovation", 2, "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400"),
    ("Dragon d'Or", "Chinese", "6 Passage du Code", 1, "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400"),
    ("The Campus Diner", "American", "1 Parvis de l'Ecole", 2, "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400"),
    ("Seoul Kitchen", "Korean", "19 Rue du Debug", 2, "https://images.unsplash.com/photo-1590301157890-4810ed352733?w=400"),
    ("Beirut Mezze", "Lebanese", "33 Avenue de l'Algo", 2, "https://images.unsplash.com/photo-1544025162-d76694265947?w=400"),
    ("Pho Saigon", "Vietnamese", "21 Rue du Terminal", 1, "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=400"),
    ("Olympus Taverna", "Greek", "9 Square de la Donnee", 2, "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400"),
]

REVIEWS = [
    # Sakura Ramen (id=1)
    (1, "Alice M.", 5, "Best tonkotsu ramen I've had near campus! Rich broth and perfect noodles."),
    (1, "Tom R.", 4, "Great ramen, a bit of a wait at lunch but worth it."),
    (1, "Lea K.", 5, "The gyoza are incredible. My go-to spot between classes."),
    (1, "Hugo P.", 3, "Good ramen but the portions could be bigger for the price."),
    # Bella Napoli (id=2)
    (2, "Marie D.", 5, "Authentic Neapolitan pizza, reminds me of Naples!"),
    (2, "Lucas B.", 4, "Great pasta, cozy atmosphere. The tiramisu is a must."),
    (2, "Emma V.", 4, "Solid Italian food. The margherita pizza is perfect."),
    # Le Petit Bistrot (id=3)
    (3, "Paul S.", 5, "Excellent duck confit. A splurge-worthy dinner spot."),
    (3, "Julie W.", 4, "Beautiful plating, classic French cuisine done right."),
    (3, "Nathan H.", 3, "Good food but quite expensive for a student budget."),
    (3, "Clara F.", 5, "The creme brulee alone is worth the visit."),
    # Bangkok Express (id=4)
    (4, "Sofia L.", 4, "Quick, affordable, and the pad thai is legit."),
    (4, "Amine T.", 5, "Amazing green curry! Spicy and flavorful."),
    (4, "Chloe R.", 4, "Great lunch deal. Tom yum soup is perfect on rainy days."),
    (4, "Yuki N.", 3, "Decent Thai food, nothing exceptional but reliable."),
    # Casa Mexicana (id=5)
    (5, "Diego M.", 5, "Tacos al pastor are phenomenal! Feels like Mexico City."),
    (5, "Laura P.", 4, "Love the burritos. Big portions, great value."),
    (5, "Kevin J.", 4, "Solid Mexican food. The guacamole is made fresh."),
    # Taj Palace (id=6)
    (6, "Priya S.", 5, "The butter chicken is heavenly. Naan is freshly baked."),
    (6, "Thomas G.", 4, "Generous portions, rich flavors. Great veggie options too."),
    (6, "Anais C.", 4, "Biryani is fantastic. Love the lunch thali set."),
    (6, "Omar B.", 3, "Good but can be a bit oily. Service is friendly though."),
    # Dragon d'Or (id=7)
    (7, "Wei L.", 4, "Authentic dim sum on weekends. Har gow is the best."),
    (7, "Camille D.", 3, "Average Chinese food. The fried rice is decent."),
    (7, "Romain A.", 4, "Mapo tofu is excellent and super affordable."),
    # The Campus Diner (id=8)
    (8, "Jake W.", 4, "Classic burgers and shakes. Perfect for a comfort food fix."),
    (8, "Sarah M.", 3, "Okay diner food. Fries are good, burger is average."),
    (8, "Maxime L.", 4, "Great breakfast menu. Pancakes are fluffy and huge."),
    (8, "Ines R.", 2, "Overpriced for what it is. The fries were cold last time."),
    # Seoul Kitchen (id=9)
    (9, "Minjun K.", 5, "Best bibimbap in town! The kimchi is homemade."),
    (9, "Eva T.", 4, "Korean fried chicken is crispy perfection."),
    (9, "Antoine F.", 4, "Love the bulgogi. Generous banchan sides."),
    # Beirut Mezze (id=10)
    (10, "Nadia H.", 5, "The hummus and falafel are incredible. So fresh!"),
    (10, "Pierre V.", 4, "Great shawarma wraps. Perfect quick lunch."),
    (10, "Lina A.", 5, "Everything is homemade. The tabbouleh is the best."),
    # Pho Saigon (id=11)
    (11, "Minh T.", 5, "Pho broth is simmered for hours, you can taste the difference."),
    (11, "Charlotte B.", 4, "Delicious banh mi and fresh spring rolls."),
    (11, "Alexis D.", 4, "Affordable and delicious. The vermicelli bowl is great."),
    # Olympus Taverna (id=12)
    (12, "Dimitri P.", 4, "Moussaka is hearty and authentic. Good souvlaki too."),
    (12, "Manon G.", 5, "The Greek salad with real feta is amazing. Love the tzatziki."),
    (12, "Raphael S.", 3, "Decent Greek food. Gyros are good but portions are small."),
]


def seed():
    """Drop existing data and re-seed the database."""
    init_db()
    db = get_db()
    cursor = db.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM reviews")
    cursor.execute("DELETE FROM restaurants")

    # Insert restaurants
    cursor.executemany(
        "INSERT INTO restaurants (name, cuisine, address, price_range, image_url) VALUES (%s, %s, %s, %s, %s)",
        RESTAURANTS,
    )

    # Insert reviews
    cursor.executemany(
        "INSERT INTO reviews (restaurant_id, author_name, rating, comment) VALUES (%s, %s, %s, %s)",
        REVIEWS,
    )

    db.commit()
    cursor.close()
    db.close()
    print(f"Seeded {len(RESTAURANTS)} restaurants and {len(REVIEWS)} reviews.")


def seed_users():
    import hashlib
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            role VARCHAR(50) DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("DELETE FROM users")
    users = [
        ("admin", hashlib.sha1(b"admin123").hexdigest(), "admin"),
        ("foodie_alice", hashlib.sha1(b"password").hexdigest(), "user"),
        ("reviewer_bob", hashlib.sha1(b"bob2026").hexdigest(), "user"),
    ]
    for username, pw_hash, role in users:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
            (username, pw_hash, role),
        )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Seeded {len(users)} users.")


if __name__ == "__main__":
    seed()
    seed_users()
