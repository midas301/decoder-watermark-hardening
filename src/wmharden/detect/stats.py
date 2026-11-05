"""Detection statistics for a k-bit watermark under the null (bit-independence) hypothesis.

Null: an unwatermarked image yields k i.i.d. fair bits, so #matches ~ Binomial(k, 0.5).
Two-sided ("double-tail") score: s = max(m, k - m), because a decoder could be flipped.
"""

from __future__ import annotations

import math

from scipy.stats import beta, binom


def two_sided_fpr(threshold: int, k: int = 48) -> float:
    """P(max(m, k-m) >= threshold) under the null."""
    if threshold > k:
        return 0.0
    if threshold <= k / 2:
        return 1.0
    return min(1.0, 2.0 * float(binom.sf(threshold - 1, k, 0.5)))


def threshold_for_fpr(target_fpr: float, k: int = 48) -> int:
    """Smallest integer match-count threshold whose theoretical FPR is <= target_fpr."""
    for t in range(math.ceil(k / 2) + 1, k + 2):
        if two_sided_fpr(t, k) <= target_fpr:
            return t
    return k + 1  # unreachable target


def bit_accuracy_threshold(target_fpr: float, k: int = 48) -> float:
    return threshold_for_fpr(target_fpr, k) / k


def score(pred_bits, true_bits) -> int:
    """Two-sided score max(matches, k - matches) for one image. Inputs: 0/1 sequences."""
    m = sum(int(p == t) for p, t in zip(pred_bits, true_bits, strict=True))
    return max(m, len(true_bits) - m)


def clopper_pearson(successes: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact two-sided (1-alpha) CI for a proportion. Use for low-FPR estimates."""
    lo = 0.0 if successes == 0 else float(beta.ppf(alpha / 2, successes, n - successes + 1))
    hi = 1.0 if successes == n else float(beta.ppf(1 - alpha / 2, successes + 1, n - successes))
    return lo, hi


def negatives_needed(target_fpr: float, alpha: float = 0.05) -> int:
    """Negatives needed so that 0 observed false positives gives a one-sided (1-alpha)
    upper bound <= target_fpr (generalised 'rule of three')."""
    return math.ceil(math.log(alpha) / math.log(1.0 - target_fpr))
