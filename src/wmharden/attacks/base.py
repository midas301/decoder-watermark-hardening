"""Common attack interface, so Phase 3 attacks plug in without touching detection/embedding."""

from __future__ import annotations

from abc import ABC, abstractmethod


class ImageAttack(ABC):
    name: str

    @abstractmethod
    def __call__(self, images, strength: float):
        """Return attacked images (same shape/range as input)."""


class WeightAttack(ABC):
    name: str

    @abstractmethod
    def run(self, decoder_state, budget: dict) -> tuple[dict, dict]:
        """Return (attacked_decoder_state, effort_record{steps,batch,unique_images,lr,seconds})."""
