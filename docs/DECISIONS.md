# Architecture / Decision Records
Format: `ADR-NNN: title`, Date, Status, Context, Decision, Consequences.

## ADR-001: Freeze detector threshold at 35 for pilot
Date: 2026-10. Status: Accepted (pilot only).
Context: Pilot calibration on 120 images. FPR not validated at 0.1%.
Decision: Use score >= 35 for all pilot comparisons.
Consequences: Theoretical FPR at 35/48 is ~0.21%, above the 0.1% target. Recalibrate on independent data before any FPR claim (see backlog).

## ADR-002: Title change
Date: 2026-10-21. Status: **Proposed, formal approval not documented.**
Decision: Working title "Decoder-Level Image Watermarking: Robustness Evaluation and Attack-Aware Hardening". Confirm with guide.

## ADR-003: Build the novelty-independent core first
Date: 2026-11. Status: Accepted.
Context: Novelty claim unresolved (proposal section 14 checks pending).
Decision: Implement embedding (Phase 1) and detection (Phase 2) first; keep attacks and defenses behind abstract interfaces.
Consequences: Whatever the lead contribution becomes, the baseline, detector and FPR audit are reusable.
