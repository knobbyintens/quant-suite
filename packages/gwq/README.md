# packages/gwq - Grid-Warping Quantization

`gwq` implements **Grid-Warping Quantization (GWQ)**, a distinct per-channel
rounding-grid warp that is frequently compared with shifted-grid methods.

- Language: Python
- License: MIT
- Status: active
- Implements: Grid-Warping Quantization (GWQ)
- Benchmark (WQ-4 4-bit accuracy retention): 94.0

## Notes

GWQ is not an SGQ implementation; it warps the grid per output channel instead
of shifting a shared grid.
