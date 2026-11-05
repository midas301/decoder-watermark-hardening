"""Decoder fine-tuning for embedding (Stable Signature recipe). STUB: implement in issue 'Implement embedding'.

Loss:  L = lambda_msg * BCE(W(D_theta(z)), m)  +  lambda_perc * LPIPS(D_theta(z), D_0(z))
  D_0   frozen original decoder (fidelity reference)
  D_theta  trainable copy
  W     frozen extractor
Training-time augmentations (the *vanilla* D0 recipe) are listed in configs/embed_d0.yaml.
Every run must write a provenance record (see checkpoint.py).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EmbedConfig:
    base_model: str = "stabilityai/stable-diffusion-2-1"
    vae_revision: str = ""  # pin the commit hash
    n_bits: int = 48
    steps: int = 1000
    batch_size: int = 4
    lr: float = 1e-4
    lambda_msg: float = 1.0
    lambda_perc: float = 0.2
    seed: int = 0
    augmentations: tuple[str, ...] = ("crop", "resize", "jpeg", "brightness")


def fine_tune_decoder(cfg: EmbedConfig, message_bits, extractor, train_loader):
    """Return (watermarked_decoder_state_dict, training_log)."""
    raise NotImplementedError
