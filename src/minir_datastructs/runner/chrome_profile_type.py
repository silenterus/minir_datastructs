from enum import Enum

class ChromeProfileType(Enum):
    GENERIC = 1
    OPENAI = 2
    HUGGINGFACE = 3
    CHATFREEDEEPSEEK = 4
    CHATSTREAM = 5
    DEEPSEEKCHAT = 6
    OPENROUTER = 7
    DEEPSEEKNET = 8
    HIX = 8
    MINIAPPS = 9

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

def chrome_profile(value) -> ChromeProfileType:
    try:
        if isinstance(value, str):
            return ChromeProfileType[value.upper().replace(' ', '')]
        return ChromeProfileType(value)
    except (KeyError, ValueError):
        raise ValueError(f'Invalid ChromeProfileType value: {value!r}') from None
