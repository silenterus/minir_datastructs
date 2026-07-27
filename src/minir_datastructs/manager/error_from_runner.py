from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ErrorFromRunner:
    job_id: str
    error_message: str
    traceback_info: Optional[str] = None
