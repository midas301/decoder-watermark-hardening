# Decoder-Level Image Watermarking: Robustness Evaluation and Attack-Aware Hardening

B.Tech. CSE (2024–2028) · UE24CS320A Capstone Project Phase-1/2 · Project ID **PW_25_CHB_01**
Guide: Dr. Chaitra B

Team: Atul Suresh (PES1UG24CS098) · Kanak Pandey (PES1UG24CS212) · Nuthan Baskar (PES1UG24CS106) · Samarth Kotian (PES1UG24CS406)

## Research question
How does a decoder watermark survive changes to the model and its output images, and can targeted
hardening improve robustness within fixed quality and compute limits?

## Status
Pilot implementation for P1–P4 is complete on a **16-image development reconstruction set** (one seed,
256 px VAE reconstructions, CPU). **No** independent final-test result and **no** validated 0.1% FPR claim exist yet.
See [docs/PROTOCOL.md](docs/PROTOCOL.md) for the frozen protocol and [backlog/](backlog/) for what is next.

## Defense candidates
| ID | Meaning |
|----|---------|
| D0 / D0_matched | Original decoder / controlled reference sharing the new attack schedule |
| D1 | Image-hardened (differentiable blur/noise augmentation) |
| D2 | Model-hardened (first-order adverse output-conv weight perturbations) |
| D3 | Both |

## Current focus
The novelty claim is still being settled (see [docs/NOVELTY.md](docs/NOVELTY.md)). The repo is therefore built so the
**novelty-independent core comes first**: watermark **embedding** (Phase 1) and **detection** (Phase 2) are coded now;
attacks and defenses plug in later through `attacks/base.py` and `defenses/base.py` without changing the core.

## Workstreams → code (suggested split, edit freely)
| Workstream | Owner | Code |
|---|---|---|
| P1 Infra, data, run records, splits | Atul | `src/wmharden/eval/`, `configs/`, `data/README.md` |
| P2 Embedding (message, extractor, decoder fine-tune, checkpoints) | Kanak | `src/wmharden/watermark/`, weight attacks in `attacks/finetune/` |
| P3 Detection, thresholds, FPR audit, image attacks | Nuthan | `src/wmharden/detect/`, `attacks/image/` |
| P4 Generation pipelines (Mode A/B), quality metrics, defenses | Samarth | `src/wmharden/watermark/pipeline.py`, `metrics/`, `defenses/` |

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
pytest -q
```

## Repository layout
```
.github/      issue/PR templates, CI, labels, CODEOWNERS
backlog/      backlog.csv, milestones.json, setup_github.py (creates labels/milestones/issues/project)
configs/      YAML experiment configs (one file per run family)
data/         NOT tracked; see data/README.md
docs/         protocol, decisions (ADRs), literature matrix, review notes, experiment log
legacy/       imported Review-2 PersonN folders, kept read-only for traceability
paper/        LaTeX / draft of the research paper
reports/      curated, small, tracked result summaries (CSV/JSON/PNG)
results/      raw run outputs (ignored by git)
scripts/      CLI entry points (run_eval.py, run_attack.py, ...)
src/wmharden/ library code: watermark/ (embed), detect/, attacks/, defenses/, metrics/, analysis/, eval/
tests/        unit + smoke tests (CPU only)
```

## Workflow
Read [CONTRIBUTING.md](CONTRIBUTING.md). Short version: every change is an issue → branch → PR → review by one other teammate.
