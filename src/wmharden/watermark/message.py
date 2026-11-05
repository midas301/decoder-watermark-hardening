"""Seeded message/key generation. STUB."""

from __future__ import annotations

import random


def make_message(n_bits: int = 48, seed: int = 0) -> list[int]:
    rng = random.Random(seed)
    return [rng.randint(0, 1) for _ in range(n_bits)]
