from enum import Enum, auto

class SettingsCategory(Enum):
    CLIPPY = auto()
    HOTKEYS = auto()
    MANAGER = auto()
    RESOURCES = auto()
    WINDOW = auto()

    @property
    def display_name(self) -> str:
        return self.name.capitalize()

    @property
    def description(self) -> str:
        return {
            SettingsCategory.CLIPPY: 'Configure Clippy behavior.',
            SettingsCategory.HOTKEYS: 'Configure global hotkeys.',
            SettingsCategory.MANAGER: 'Configure manager specific settings.',
            SettingsCategory.WINDOW: 'Window Watcher.'
        }[self]
