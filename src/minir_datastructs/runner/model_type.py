from enum import Enum

class ModelTypes(Enum):
    NONE = 0
    GENERIC = 1
    V3 = 2
    R1 = 3
    O1 = 4
    O3 = 5
    O3_MINI = 6
    GPT4 = 7
    GPT45 = 8
    GPT4O = 9
    GPT4O_MINI = 10
    GPT4O_JAWBONE = 11
    ALPACA = 12
    ALPHAFOLD3 = 13
    BARD = 14
    BERT = 15
    BLOOM = 16
    CEREBRAS_GPT = 17
    CHATGLM3 = 18
    CLAUDE = 19
    CLAUDE_2 = 20
    CLAUDE_3_HAIKU = 21
    CLAUDE_3_OPUS = 22
    CLAUDE_3_SONNET = 23
    CODE_LLAMA = 24
    CODEX = 25
    COHERE_COMMAND = 26
    DALL_E_2 = 27
    DALL_E_3 = 28
    DBRX = 29
    DEEPSEEK_MATH = 30
    ERNIE_BOT = 31
    FALCON = 32
    FLAN_T5 = 33
    GALACTICA = 34
    GEMINI = 35
    GEMINI_PRO = 36
    GEMINI_ULTRA = 37
    GPT_NEO = 38
    GPT_NEOX = 39
    GRAPHORMER = 40
    GROK = 41
    GROK_1_5 = 42
    IDEFICS = 43
    IMAGEN = 44
    JASPER = 45
    JURASSIC_2 = 46
    KOSMOS_2 = 47
    LAMDA = 48
    LLAVA = 49
    LLAMA = 50
    LLAMA_2_7B = 51
    LLAMA_2_13B = 52
    LLAMA_2_70B = 53
    LLAMA_3_8B = 54
    LLAMA_3_70B = 55
    MEGATRON = 56
    MISTRAL = 57
    MIXTRAL = 58
    MT_NLG = 59
    NEMO = 60
    NEVA = 61
    OPT = 62
    ORCA = 63
    PALM = 64
    PALM_2 = 65
    PHI_1 = 66
    PHI_2 = 67
    PLEX = 68
    PROPHET_NET = 69
    QWEN = 70
    RETRO = 71
    ROBERTA = 72
    RWKV = 73
    STABLE_LM = 74
    STABLE_DIFFUSION = 75
    STABLE_DIFFUSION_XL = 76
    STARCRAFT = 77
    TURING = 78
    TURING_NLG = 79
    UL2 = 80
    VICUNA = 81
    WIZARD_CODER = 82
    WIZARD_LM = 83
    XGLM = 84
    YALM = 85
    ZEPHYR = 86
    BIO_GPT = 87
    CODE_GEN = 88
    CODET5 = 89
    GALACTICA_120B = 90
    GRAPH_GPT = 91
    MED_PALM = 92
    MUSIC_GEN = 93
    PHYS_LANG = 94
    PROTEIN_GPT = 95
    SCIFI_GPT = 96
    WHISPER = 97
    WIZARD_MATH = 98
    WORLD_MODEL = 99
    ALL = 1000

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            value = value.upper().replace(' ', '')
            for member in cls:
                if member.name == value:
                    return member
            try:
                return cls(int(value))
            except ValueError:
                pass
        return super()._missing_(value)

def model_type(value) -> ModelTypes:
    try:
        if isinstance(value, str):
            return ModelTypes[value.upper().replace(' ', '')]
        return ModelTypes(value)
    except (KeyError, ValueError):
        raise ValueError(f'Invalid ModelTypes value: {value!r}') from None
