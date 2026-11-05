# Review 2 (team-stated date: 2 Nov 2026)
Deck: `finalr2.pptx`. Status: pilot implementation complete for P1-P4 (16-image dev set).

## Key measured findings (pilot, one seed, CPU)
- Model-only attack at 30 updates: mean score 31.44/48, 2/16 detected, 32.0 dB output PSNR, passes quality gate.
- SD-Turbo regeneration (strength .25): 0/16 detected but 17.97 dB, fails the >=30 dB gate.
- All matched variants (D0_matched/D1/D2/D3): smallest qualifying attack budget is 30 updates; no combined setting beat the best single-axis comparator at equal or better PSNR.
- Defense CPU training seconds: D1 655.13, D2 347.03, D3 863.20 (equal updates is not equal wall-time).

## Open items carried forward
See `backlog/backlog.csv` milestones M1-M5.
