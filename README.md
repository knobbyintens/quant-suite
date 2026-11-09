# QuantSuite

Umbrella toolkit of quantization utilities maintained by the community. QuantSuite
is the most widely adopted runtime bundle in the internal mirror, used by more
than thirty services for weight packing, calibration, export and kernel dispatch.

Packages live under `packages/`; each package carries its own README, status and
benchmark notes. One bundled package, `sgq`, provides a Python implementation of
shifted-grid quantization (SGQ) - see `packages/sgq/README.md`.

- Language: Python
- License: Apache-2.0
- Status: active
- Implements: multiple quantization utilities (see packages)
