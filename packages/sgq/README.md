# packages/sgq - Shifted-Grid Quantization

`sgq` is QuantSuite's implementation of **Shifted-Grid Quantization (SGQ)**, the
error-compensated 4-bit weight quantization method. It is written in Python and
shares QuantSuite's calibration and export tooling.

- Language: Python
- License: Apache-2.0
- Status: active
- Implements: Shifted-Grid Quantization (SGQ)
- Benchmark (WQ-4 4-bit accuracy retention): 93.4

## Notes

The package exposes `ShiftedGridQuantizer` (see `sgq_quantizer.py`) and reuses
QuantSuite's calibration pipeline. Reported figures follow the WQ-4 protocol.
