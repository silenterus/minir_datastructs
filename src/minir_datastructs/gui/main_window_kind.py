from enum import Enum, auto


class MainWindowKind(Enum):
    EDITOR = auto()
    DEBUG = auto()

    @property
    def display_name(self) -> str:
        return self.name.capitalize()

    @property
    def description(self) -> str:
        return {
            MainWindowKind.EDITOR: 'Editor for Minir.',
            MainWindowKind.DEBUG: 'Debugger for Minir.',


        }[self]