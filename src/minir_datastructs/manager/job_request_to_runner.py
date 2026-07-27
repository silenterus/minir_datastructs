from dataclasses import dataclass

from .job import Job


@dataclass(frozen=True)
class JobRequestToRunner:
    job: Job
