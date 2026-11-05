# Literature matrix
| # | Paper | Category | Method | Finding | Limitation | Relevance to D1/D2/D3 | Status |
|---|---|---|---|---|---|---|---|
| 1 | Stable Signature (Fernandez, ICCV'23) | Baseline | Fine-tune LDM decoder with fixed signature | Rooted watermark | Decoder removal | Our target system | Read |
| 2 | Stable Signature is Unstable (Hu, 2024) | Baseline attack | Decoder fine-tune removal | Removes watermark | White-box | Defines P2 attack | Read |
| 3 | WAVES (An, ICML'24) | Protocol | Benchmark | Attack protocol | | Attack set | Read |
| 4 | AdvMark (Chen, CVPR'26) | Supporting | Decoupled defenses | Joint defenses can conflict | | Test D1/D2 interaction | Read |
| 5 | Meta-FC (Li, 2026, preprint) | Alternative | Meta-learning | Held-out distortions | Not weight attacks | Held-out attack design | Read |
| 6 | SleeperMark (Wang, CVPR'25) | Counterpoint | Separate watermark from semantic adaptation | Survives fine-tuning | | Fine-tuning need not erase | Read |
| 7 | MarkNull (Cao, USENIX Sec'26) | Challenge | Latent manipulation | Removal + amortization | Different mechanism | Cost precedent | Read |
| 8 | RoboSignature (Shaan, 2024, preprint) | Novelty risk | Tamper-resistant decoder tuning | | | Novelty guardrail | **Full-text compare pending** |
| 9 | CAT (Satheesh, 2026, preprint) | Novelty risk | Adaptive image-space adversarial training | | | Novelty guardrail | **Full-text compare pending** |
