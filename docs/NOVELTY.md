# Novelty tracker

Source: `Capstone_Proposal_Watermark_Cost_Study` (Draft v2, 21 Oct 2026), sections 1, 3, 11, 14.
**Status: unresolved.** Claims below are from the proposal; absence claims rest on searches to date.

## Current candidate claim (from proposal)
Controlled 2x2 comparison (D0 / image-space D1 / weight-space D2 / combined D3) of one decoder-level watermark
under image-edit and decoder-fine-tuning attacks, matched budgets, reported as lowest removal cost found.
Already known (not novel by themselves): cost-vs-quality curves (WAVES), tamper-resistant decoder training (RoboSignature),
defense conflicts within image space (AdvMark), adaptive compositional training (CAT).

## Fallback if checks 1-2 find the study already done
Lead with proxy fidelity + held-out attack-family generalization (RQ4), per proposal section 14.

## Other levers named in the proposal (for discussion with guide)
- Second decoder-level watermark or second base model (moves toward main track).
- A surprising, well-explained interaction (interference) between the two defenses.
- Theory-lite link between cost curves and the known removal bound.
- RQ5: empirical vs theoretical FPR drift under hardening (needs the >=10k-negative audit; supported by M2 work).

## Search log
| Date | Check | Query / source | Finding | By |
|---|---|---|---|---|
| | 1 | | | |

## Why embedding + detection first
Every candidate contribution above needs the same baseline watermark, detector and a trustworthy FPR audit.
