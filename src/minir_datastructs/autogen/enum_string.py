import argparse
from dataclasses import field, dataclass
from pathlib import Path
from typing import List, Tuple, Dict, Type, TypeVar, Optional

import re
from enum import Enum


T = TypeVar('T', bound='BaseEnumString')

def sanitize_enum_name(enum_name: str | None) -> str:
    if enum_name is None:
        return ""
    return re.sub(r"[-_.]", "", enum_name.strip()).lower()




class BaseEnumString(Enum):
    def __init__(self, string_value: str, code: int, description: str):
        self._value_ = string_value
        self._code = code
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

    @classmethod
    def _get_default(cls: Type[T]) -> T:
        try:
            return cls('none')
        except (AttributeError, ValueError):
            try:
                return cls['NONE']
            except KeyError:
                 raise NotImplementedError(
                    f"{cls.__name__} must have a member with value 'none' (or a member named 'NONE')"
                    " to use BaseEnumString."
                )

    @classmethod
    def _get_choices(cls: Type[T]) -> list[str]:
        return [f"{member.value}" for member in cls]


    @classmethod
    def _get_codes(cls: Type[T]) -> list[int]:
        if not cls.__members__:
            return []
        first_member = next(iter(cls.__members__.values()))
        if not hasattr(first_member, 'code'):
             return []
        return [member.code for member in cls]


    @classmethod
    def _get_type_display_name(cls: Type[T]) -> str:
        name = cls.__name__
        if name.endswith("Type"):
            name = name[:-4]
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return name

    @classmethod
    def from_string(cls: Type[T], input_string: Optional[str]) -> T: # Use Optional

        if input_string is None:
            return cls._get_default()

        stripped_input = input_string.strip()
        if not stripped_input:
             return cls._get_default()

        try:
            input_int = int(stripped_input)
            for member in cls:
                if hasattr(member, 'code') and member.code == input_int:
                    return member
        except ValueError:
            pass
        except AttributeError as e:
             print(f"Warning: Problem accessing 'code' attribute in {cls.__name__}: {e}")
             pass

        sanitized = sanitize_enum_name(stripped_input)
        try:
            return cls(sanitized)
        except ValueError:
            type_name = cls._get_type_display_name()
            str_choices = cls._get_choices()
            code_choices = cls._get_codes()

            error_message = f"Invalid {type_name}: {input_string!r}. "
            if str_choices:
                 error_message += f"String choices: {str_choices}"
                 if code_choices:
                     error_message += f". "
            if code_choices:
                 error_message += f"Code choices: {code_choices}"
            if not str_choices and not code_choices:
                 error_message += "No choices available."

            raise argparse.ArgumentTypeError(error_message)

    def __str__(self) -> str:
        return str(self.value)
