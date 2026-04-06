package com.epita.flashcards;

import android.animation.AnimatorInflater;
import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.view.View;
import android.view.animation.AccelerateDecelerateInterpolator;

/**
 * Helper class for a 3D card-flip animation between two views.
 *
 * <h3>How to use</h3>
 * <pre>{@code
 *   // 1. Get references to the front and back views of your card.
 *   View frontView = findViewById(R.id.card_front);
 *   View backView  = findViewById(R.id.card_back);
 *
 *   // 2. Create the helper (sets initial visibility and camera distance).
 *   FlipAnimationHelper flipHelper = new FlipAnimationHelper(frontView, backView);
 *
 *   // 3. Flip the card on tap.
 *   cardContainer.setOnClickListener(v -> flipHelper.flip());
 *
 *   // 4. Check which side is showing.
 *   boolean showingFront = flipHelper.isFrontVisible();
 * }</pre>
 *
 * <p>The animation rotates the card 180 degrees around the Y axis with a
 * perspective effect. Duration is configurable via {@link #setDuration(long)}.
 */
public class FlipAnimationHelper {

    private final View frontView;
    private final View backView;
    private boolean isFrontVisible = true;
    private long duration = 300; // milliseconds

    /**
     * Create a flip helper for the given front and back views.
     *
     * @param frontView the view shown initially (question side)
     * @param backView  the view shown after flip (answer side)
     */
    public FlipAnimationHelper(View frontView, View backView) {
        this.frontView = frontView;
        this.backView = backView;

        // Set camera distance for a realistic 3D perspective effect.
        float scale = frontView.getResources().getDisplayMetrics().density;
        float cameraDistance = 8000 * scale;
        frontView.setCameraDistance(cameraDistance);
        backView.setCameraDistance(cameraDistance);

        // Back view starts hidden.
        backView.setAlpha(0f);
    }

    /**
     * Perform the flip animation. If the front is showing, flip to back and
     * vice-versa.
     */
    public void flip() {
        final View visibleView = isFrontVisible ? frontView : backView;
        final View hiddenView  = isFrontVisible ? backView : frontView;

        // --- First half: rotate visible view from 0 to 90 degrees ---
        ObjectAnimator outRotation = ObjectAnimator.ofFloat(visibleView, "rotationY", 0f, 90f);
        outRotation.setDuration(duration / 2);
        outRotation.setInterpolator(new AccelerateDecelerateInterpolator());

        // --- Second half: rotate hidden view from -90 to 0 degrees ---
        ObjectAnimator inRotation = ObjectAnimator.ofFloat(hiddenView, "rotationY", -90f, 0f);
        inRotation.setDuration(duration / 2);
        inRotation.setInterpolator(new AccelerateDecelerateInterpolator());

        outRotation.addListener(new android.animation.AnimatorListenerAdapter() {
            @Override
            public void onAnimationEnd(android.animation.Animator animation) {
                visibleView.setAlpha(0f);
                hiddenView.setAlpha(1f);
                inRotation.start();
            }
        });

        outRotation.start();
        isFrontVisible = !isFrontVisible;
    }

    /** Return true if the front (question) side is currently visible. */
    public boolean isFrontVisible() {
        return isFrontVisible;
    }

    /** Reset to show the front side without animation. */
    public void resetToFront() {
        frontView.setRotationY(0f);
        frontView.setAlpha(1f);
        backView.setRotationY(0f);
        backView.setAlpha(0f);
        isFrontVisible = true;
    }

    /** Set the flip animation duration in milliseconds. */
    public void setDuration(long millis) {
        this.duration = millis;
    }
}
