# Star Assets

This project uses **SF Symbols** for star icons. No custom assets are needed.

## SF Symbols used

| Symbol Name  | Usage              |
|--------------|--------------------|
| `star.fill`  | Filled star (rated) |
| `star`       | Empty star          |

## How to use in code

```swift
// Filled star
let filledStar = UIImage(systemName: "star.fill")

// Empty star
let emptyStar = UIImage(systemName: "star")
```

The provided `StarRatingView` helper already handles this for you.
Simply set `starRatingView.rating = 4.2` and it displays the correct stars.

## Adding custom colors

You can customize star colors in the Asset Catalog or directly in code:

```swift
starRatingView.filledColor = .systemYellow
starRatingView.emptyColor = .systemGray4
```
