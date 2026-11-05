# Legacy (Review-2 hand-offs)
Import the existing folders here **unchanged**, then refactor into `src/wmharden/` via issues:
- `Person1_*`  -> `src/wmharden/eval/`
- `Person2_*`  -> `src/wmharden/attacks/finetune/`
- `Person3_Image_Attack` -> `src/wmharden/attacks/image/`
- `Person4_Quality_Cost_Analysis` -> `src/wmharden/{defenses,metrics,analysis}/`
Strip checkpoints and big per-image dumps before committing (see CONTRIBUTING.md).
