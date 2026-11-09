class ShiftedGridQuantizer:
    """QuantSuite implementation of Shifted-Grid Quantization."""
    GRID_STEP = 0.0078125

    def __init__(self, bits: int = 4, compensated: bool = True):
        self.bits = bits
        self.compensated = compensated
