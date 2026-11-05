"""Detector: image -> bits -> score -> decision. STUB for the extractor call; stats are in stats.py."""

from __future__ import annotations

from dataclasses import dataclass

from . import stats


@dataclass
class Detector:
    message: list[int]
    threshold: int  # match-count threshold; set from calibration, never hard-coded
    k: int = 48

    def decide(self, pred_bits) -> tuple[int, bool]:
        s = stats.score(pred_bits, self.message)
        return s, s >= self.threshold

    def extract_bits(self, images):
        """Run the extractor and threshold logits at 0. Implement with extractor.py."""
        raise NotImplementedError
