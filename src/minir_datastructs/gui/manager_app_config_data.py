from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class ManagerAppConfigData:
    manager_dir_str: str = './manager'
    resolved_manager_dir: Path = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'resolved_manager_dir', Path(self.manager_dir_str).resolve())
