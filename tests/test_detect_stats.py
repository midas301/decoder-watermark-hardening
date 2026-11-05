import pytest

from wmharden.detect import stats


def test_pilot_threshold_35_is_not_01_percent():
    # Pilot threshold 35/48: theoretical two-sided FPR ~0.21%, above the 0.1% target.
    assert stats.two_sided_fpr(35) == pytest.approx(2.09e-3, rel=0.02)
    assert stats.two_sided_fpr(35) > 1e-3


def test_threshold_for_target():
    assert stats.threshold_for_fpr(1e-3) == 36
    assert stats.threshold_for_fpr(1e-4) == 38
    assert stats.bit_accuracy_threshold(1e-3) == pytest.approx(0.75)


def test_score():
    assert stats.score([1, 0, 1, 0], [1, 0, 1, 0]) == 4
    assert stats.score([0, 1, 0, 1], [1, 0, 1, 0]) == 4  # fully flipped
    assert stats.score([1, 1, 0, 0], [1, 0, 1, 0]) == 2


def test_clopper_pearson_zero_events():
    lo, hi = stats.clopper_pearson(0, 60)
    assert lo == 0.0 and hi > 0.05  # 0/60 cannot support 0.1% FPR


def test_negatives_needed():
    assert 2900 <= stats.negatives_needed(1e-3) <= 3100
