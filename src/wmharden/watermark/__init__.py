"""Phase 1: embedding. Stable Signature-style decoder-level watermark.

Modules (to implement, in order):
  message.py   key/message generation (48-bit), seeded + stored with run metadata
  extractor.py watermark extractor W: image -> k logits (load pretrained / pretrain HiDDeN-style)
  embed.py     fine-tune the VAE decoder so W(decoder(z)) == message, with perceptual loss
  checkpoint.py export/reload decoder weights + SHA-256 + provenance JSON
  pipeline.py  Mode A: SD2.1 text->image with watermarked decoder; Mode B: encode->watermarked decode
"""
