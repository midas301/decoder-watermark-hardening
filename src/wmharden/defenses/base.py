"""Defense interface (D1-D3). Kept separate from embedding so the baseline D0 stays untouched."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Defense(ABC):
    name: str

    @abstractmethod
    def harden(self, decoder_state, config: dict) -> tuple[dict, dict]:
        """Return (hardened_decoder_state, training_record)."""
