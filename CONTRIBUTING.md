# Contributing

## Flow
1. Pick an issue from the **Project board** (Ready column). Assign yourself, move to *In progress*.
2. Branch from `main`: `feat/<issue#>-short-name`, `exp/<issue#>-name`, `fix/...`, `docs/...`, `chore/...`.
3. Commit with Conventional Commits: `feat(eval): freeze 48-bit threshold config (#12)`.
4. Open a PR using the template. Link `Closes #N`. At least **1 approval** from a teammate; CI must pass.
5. Squash-merge. Delete the branch.

## Experiment rules (these protect the research claims)
- Every run is driven by a config in `configs/` and records: git SHA, config hash, seed, model revision hashes, wall time, hardware.
- Never edit frozen splits, signature, preprocessing, or threshold without an ADR in `docs/DECISIONS.md` and a protocol version bump.
- **Keep failed settings.** Do not delete runs that fail the quality gate.
- Report CPU vs GPU time separately; model load separate from per-image inference.
- Label scope in every report: seed count, image count, resolution, device.
- Do not claim FPR, robustness, or synergy beyond what the data supports (see PROTOCOL.md "Claims policy").

## Data and large files
Images, checkpoints (`*.pt`, `*.safetensors`), and raw per-image dumps are **not** committed.
Store them in the shared drive and record paths/hashes in `data/README.md`. Small summaries go to `reports/`.

## Code style
`ruff` + `ruff format`, type hints on public functions, tests for anything that touches metrics or thresholds.
