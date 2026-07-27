from enum import Enum, auto





class ToolsKind(Enum):
    MARKDOWN = auto()
    CODE = auto()
    RESOURCES = auto()
    DOWNLOADER = auto()
    SNIPPER = auto()


    @property
    def display_name(self) -> str:
        return self.name.capitalize()

    @property
    def description(self) -> str:
        return {
            ToolsKind.MARKDOWN: 'Markdown Editor for Minir.',
            ToolsKind.CODE: 'Code Editor for Minir.',
            ToolsKind.RESOURCES: 'Resources Editor for Minir.',
            ToolsKind.DOWNLOADER: 'Downloader for Minir.',
            ToolsKind.SNIPPER: 'Cut snippets.'

        }[self]