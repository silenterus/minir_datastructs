from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class JobResultFromRunner:
    job_id: str
    result: Any
