from dataclasses import dataclass, field


@dataclass
class QuantArguments:
    # With 8-bit adam, can you adjust to LION or Sophia, and even deepspeed offers multiple 1-bit optimizer options0
    adam8bit: bool = field(default=False, metadata={'help': 'Use 8-bit adam.'})
    # Whether to use quadratic quantization
    double_quant: bool = field(
        default=True,
        metadata={
            'help':
            'Compress the quantization statistics through double quantization.'
        })
    # Quantization type, you can choose fp4 or nf4
    quant_type: str = field(
        default='nf4',
        metadata={
            'help':
            'Quantization data type to use. Should be one of `fp4` or `nf4`.'
        })
    # Bit width used, default is 4.
    bits: int = field(default=4, metadata={'help': 'How many bits to use.'})

    def __post_init__(self):
        if self.bits is not None:
            assert self.bits in [
                4, 8
            ], 'We only accept 4-bit or 8-bit quantization.'

        if self.quant_type is not None:
            assert self.quant_type in [
                'nf4', 'fp4'
            ], 'We only accept `nf4` or `fp4` quantization type.'
