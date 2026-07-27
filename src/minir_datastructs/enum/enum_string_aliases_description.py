

import re
from enum import Enum
from typing import TypeVar, Type, Optional, List, Dict, Any, Union, Tuple
import argparse

T = TypeVar('T', bound='EnumStringAliasesDescription')


def sanitize_enum_name(enum_name: Union[str, None]) -> str:
    if enum_name is None:
        return ""
    name = enum_name.strip()
    name = re.sub(r"[_.#]", "", name)  # Remove _, ., #
    name = name.replace('+', 'p')
    name = name.replace('-', '')
    return name.lower()

class EnumStringAliasesDescription(Enum):
    def __init__(self, string_value: str, code: int, aliases: str, description: str):
        self._value_ = string_value
        self._code = code
        self._aliases = aliases
        self._description = description

    @property
    def code(self) -> int:
        if not hasattr(self, '_code'):
            raise AttributeError(f"Member {self.name} was likely not initialized correctly - missing _code.")
        return self._code

    @property
    def description(self) -> str:
        if not hasattr(self, '_description'):
            raise AttributeError(f"Member {self.name} was likely not initialized correctly - missing _description.")
        return self._description

    @property
    def aliases(self) -> str:
        if not hasattr(self, '_aliases'):
            raise AttributeError(f"Member {self.name} was likely not initialized correctly - missing _aliases.")
        return self._aliases

    @classmethod
    def _get_default(cls: Type[T]) -> T:
        try:
            return cls('none')  # type: ignore [call-arg]
        except ValueError:
            try:
                return cls['NONE']  # type: ignore [misc] # Python 3.11 allows _INTERNAL_NONE lookup here
            except KeyError:
                # Try _INTERNAL_NONE if NONE is not found (for LanguageKind specifically)
                if hasattr(cls, '_INTERNAL_NONE'):
                    return cls._INTERNAL_NONE  # type: ignore [attr-defined, no-any-return]
                raise NotImplementedError(
                    f"{cls.__name__} must have a member with value 'none' (or a member named 'NONE' or '_INTERNAL_NONE')"
                    " to use EnumStringAliasesDescription for default empty/None string handling."
                )

    @classmethod
    def _get_choices(cls: Type[T]) -> list[str]:
        return [f"{member.value}" for member in cls]

    @classmethod
    def _get_codes(cls: Type[T]) -> list[int]:
        if not cls.__members__:
            return []
        return [member.code for member in cls if hasattr(member, '_code')]

    @classmethod
    def _get_type_display_name(cls: Type[T]) -> str:
        name = cls.__name__
        if name.endswith("Type"): name = name[:-4]
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return name

    @classmethod
    def from_string(cls: Type[T], input_string: Optional[str]) -> T:
        if input_string is None: return cls._get_default()
        stripped_input = input_string.strip()
        if not stripped_input: return cls._get_default()

        try:
            input_int = int(stripped_input)
            for member in cls:  # type: ignore [assignment]
                if hasattr(member, '_code') and member.code == input_int:  # type: ignore [attr-defined]
                    return member  # type: ignore [return-value]
        except ValueError:
            pass

        sanitized = sanitize_enum_name(stripped_input)
        if not sanitized: return cls._get_default()

        try:
            return cls(sanitized)  # type: ignore [call-arg]
        except ValueError:
            for member in cls:  # type: ignore [assignment]
                desc_str = member.aliases if hasattr(member, '_aliases') and isinstance(member._aliases,
                                                                                                str) else ""  # type: ignore [attr-defined]
                if desc_str:
                    aliases = [alias.strip() for alias in desc_str.split(',')]
                    sanitized_aliases = [sanitize_enum_name(alias) for alias in aliases if alias.strip()]
                    if sanitized in sanitized_aliases:
                        return member  # type: ignore [return-value]

            if cls.__name__ == "LanguageKind":
                # Check if _INTERNAL_NONE should be returned for "none" if it didn't match an alias
                if sanitized == "none" and hasattr(cls, '_INTERNAL_NONE'):
                    return cls._INTERNAL_NONE  # type: ignore [attr-defined, return-value]
                try:
                    return cls.UNKNOWN  # type: ignore [attr-defined, return-value]
                except AttributeError:
                    pass

            type_name, str_choices, code_choices = cls._get_type_display_name(), cls._get_choices(), cls._get_codes()
            error_message = f"Invalid {type_name}: {input_string!r}. "
            if str_choices: error_message += f"String choices: {str_choices}" + (". " if code_choices else "")
            if code_choices: error_message += f"Code choices: {code_choices}"
            if not str_choices and not code_choices: error_message += "No choices available."
            raise argparse.ArgumentTypeError(error_message)

    def __str__(self) -> str:
        return str(self.value)