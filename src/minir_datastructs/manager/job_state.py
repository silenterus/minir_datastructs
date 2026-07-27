from dataclasses import dataclass
from typing import Any, Optional

from .error_from_runner import ErrorFromRunner
from .job_status import JobStatus


@dataclass
class JobState:
    status: JobStatus = JobStatus.QUEUED
    final_result: Optional[Any] = None
    error_info: Optional[ErrorFromRunner] = None
    assigned_runner_id: Optional[int] = None
