from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .asset_paths import AssetPaths


@dataclass(frozen=True)
class AppConfigData:
    app_name: str
    base_assets_dir_str: str = './assets'
    tray_icon_filename: str = 'applicationIcon-256.png'
    window_icon_filename: str = 'applicationIcon.ico'
    resolved_paths: AssetPaths = field(init=False)

    def __post_init__(self):
        base_dir = Path(self.base_assets_dir_str).resolve()
        base_dir.mkdir(exist_ok=True)
        object.__setattr__(self, 'resolved_paths', AssetPaths(base_dir=base_dir, tray_icon_file=base_dir / self.tray_icon_filename, window_icon_file=base_dir / self.window_icon_filename))

    def get_window_icon_path_str(self) -> Optional[str]:
        return str(self.resolved_paths.window_icon_file) if self.resolved_paths.window_icon_file.exists() else None

    def get_tray_icon_path_str(self) -> Optional[str]:
        return str(self.resolved_paths.tray_icon_file) if self.resolved_paths.tray_icon_file.exists() else None

    def get_assets_dir_str(self) -> str:
        return str(self.resolved_paths.base_dir)
