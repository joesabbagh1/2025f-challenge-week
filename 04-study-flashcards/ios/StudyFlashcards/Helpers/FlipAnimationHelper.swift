import UIKit

/// UIView extension that provides a 3D card-flip animation.
///
/// ## How to use
///
/// ```swift
/// // 1. You have two views: frontView and backView.
/// //    backView starts hidden (isHidden = true).
///
/// // 2. Flip from front to back:
/// frontView.flip3D(to: backView)
///
/// // 3. Flip back:
/// backView.flip3D(to: frontView)
///
/// // 4. Track which side is showing with a boolean:
/// var showingFront = true
/// cardContainer.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(flip)))
///
/// @objc func flip() {
///     if showingFront {
///         frontView.flip3D(to: backView)
///     } else {
///         backView.flip3D(to: frontView)
///     }
///     showingFront.toggle()
/// }
/// ```
///
/// The animation uses `UIView.transition` with a `.transitionFlipFromRight`
/// option, giving a realistic 3D card-flip effect with no extra dependencies.
extension UIView {

    /// Perform a 3D flip animation from this view to `toView`.
    ///
    /// - Parameters:
    ///   - toView: The view to reveal after the flip.
    ///   - duration: Animation duration in seconds (default 0.5).
    ///   - completion: Optional callback fired when the animation finishes.
    func flip3D(
        to toView: UIView,
        duration: TimeInterval = 0.5,
        completion: (() -> Void)? = nil
    ) {
        let fromView = self
        let container = fromView.superview ?? fromView

        UIView.transition(
            with: container,
            duration: duration,
            options: [.transitionFlipFromRight, .showHideTransitionViews],
            animations: {
                fromView.isHidden = true
                toView.isHidden = false
            },
            completion: { _ in
                completion?()
            }
        )
    }
}
