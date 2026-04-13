# Campus Food Guide - iOS

## Prerequisites

- Xcode 15+ with iOS 17 SDK
- Python 3 (for the backend)
- The Flask backend running on `localhost:5000`

## Setup

1. **Start the backend** (from the project root):
   ```bash
   cd backend
   pip install -r requirements.txt
   python seed.py
   python app.py
   ```

2. **Open the Xcode project** and run on the iOS Simulator.
   - The app connects to `http://localhost:5000` by default.
   - If using a physical device, update `APIClient.baseURL` to your Mac's local IP.

## Architecture

```
CampusFoodGuide/
  Models/
    Restaurant.swift    -- Codable data model
    Review.swift        -- Codable data model
  Services/
    APIClient.swift     -- URLSession HTTP client
  Views/
    RestaurantListViewController.swift   -- Main table view (working)
    RestaurantDetailViewController.swift -- Detail view (reviews TODO)
  Helpers/
    StarRatingView.swift -- Reusable star rating component (provided)
```

## What is already working

- Restaurant list loads from the API and displays name, cuisine, stars, and price
- Tapping a restaurant navigates to the detail screen
- Detail screen shows restaurant info (name, cuisine, address, rating, price)
- `StarRatingView` is fully functional and ready to use

## What you need to build

See the main `README.md` for the full list of TODOs.

## Tips

- Use `StarRatingView` for any rating display -- just set the `.rating` property.
- SF Symbols are used for stars (`star.fill`, `star`). No custom assets needed.
- `Info.plist` already allows local networking (no ATS issues with localhost).
