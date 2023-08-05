from dataclasses import dataclass, field


@dataclass
class LoraArguments:
    #  Number of columns of matrix A and number of rows of matrix B in Lora
    lora_r: int = field(default=64, metadata={'help': 'Lora R dimension.'})
    # Scaling factor
    lora_alpha: float = field(default=16, metadata={'help': ' Lora alpha.'})
    lora_dropout: float = field(default=0.0,
                                metadata={'help': 'Lora dropout.'})
    # Size of memory available on each GPU, in MB. The default is 40GB1 for the high-end version of the A100
    max_memory_MB: int = field(default=40960,
                               metadata={'help': 'Free memory per gpu.'})
    lora_weight_path: str = ''
    bias: str = 'none'
    