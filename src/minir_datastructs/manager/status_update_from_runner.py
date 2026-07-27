from dataclasses import dataclass

from .job_status import JobStatus


@dataclass(frozen=True)
class StatusUpdateFromRunner:
    job_id: str
    status_message: JobStatus
