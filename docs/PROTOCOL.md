# Evaluation Protocol (v1.0, Review-2 pilot)

Frozen. Any change requires an ADR in `DECISIONS.md` and a version bump here.

## Models
- VAE: `sd-vae-ft-mse`
- Watermarked decoder: Stable Signature SD2 decoder
- Regeneration attack: `stabilityai/sd-turbo` @ `b261bac6fd2cf515557d5d0707481eafa0485ec2` (fp16 storage, float32 on CPU), empty prompt, guidance 0, 4 scheduler points; strengths .25/.5/.75 execute 1/2/3 denoising passes.
  This is regeneration after the decoder output, **not** matched SD2.1 text-to-image generation.

## Detector
48-bit signature. Score = `max(matches, 48 - matches)`.
**Pilot (Review 2): threshold >= 35.** Under bit independence this is a two-sided FPR of ~0.21% (not 0.1%).
For reference: 36 -> 0.072%, 37 (0.77 bit acc, Hu et al.) -> 0.022%, 38 -> 0.006%.
The v2 threshold must be chosen from calibration data and recorded in an ADR (backlog: "Fix threshold").
Helpers: `wmharden.detect.stats`.

## Data (pilot)
P1: 120 calibration + 60 audit + 20 eval. P2/P3/P4: the same 16 development photos at 256 px.

## Variants
D0 (historical), **D0_matched** (control, shares attack schedule), D1 (blur/noise aug), D2 (first-order adverse output-conv weight perturbation), D3 (both).
Defense training: 32 updates on 32 unique images. Attacker budgets 0/30/60 updates (historical D0: 0/15/30/60).

## Attacks
Decoder fine-tuning (white-box: extractor gradients + known signature), JPEG (50/90), blur (0.5/1), SD-Turbo regeneration (.25/.5/.75), and combinations. Image attacks have no detector gradients or key.

## Quality gates
- No-attack defense gate: 100% baseline detection, source PSNR drop <= 0.5 dB, source-reference FID degradation <= 1.
- Attack acceptance (all must hold): mean score < 35, detected fraction <= 20%, source PSNR drop <= 1 dB, pooled own-baseline-output PSNR >= 30 dB.
- Metrics: PSNR, SSIM (skimage), LPIPS (AlexNet v0.1), FID (torch-fidelity, Inception 2048). FID at n=16 is exploratory.

## Cost accounting
Attacker cost for N images = checkpoint training s + N x (render s + pixel attack s). Detection is overhead, modeled separately. Report model-load separately. CPU vs GPU hours are reported separately (pilot: 0 GPU hours).

## Claims policy
- 0/60 audit false positives does **not** validate a 0.1% FPR. (Rule of three: ~3,000 negatives gives a 95% upper bound of 0.1% at zero observed FP.)
- A zero detection count applies to the tested detector and cohort only.
- Sampled minima are not global minima. No general synergy or proven hardening is claimed.
- Always state: seeds, #images, resolution, device.
