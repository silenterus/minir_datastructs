from typing import Dict, Tuple, Any


class ContentDetector:
    content_type = 'generic'

    def detect(self, text: str) -> Tuple[float, Dict[str, Any]]:
        raise NotImplementedError