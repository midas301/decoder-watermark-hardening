def test_import():
    import wmharden

    assert wmharden.__version__


def test_score_definition():
    """Detector score = max(matches, 48 - matches); threshold >= 35 (pilot-calibrated)."""

    def score(matches: int) -> int:
        return max(matches, 48 - matches)

    assert score(48) == 48 and score(0) == 48 and score(24) == 24
