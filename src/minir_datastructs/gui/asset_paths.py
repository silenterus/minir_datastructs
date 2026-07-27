from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class AssetPaths:
    base_dir: Path
    tray_icon_file: Path
    window_icon_file: Path
