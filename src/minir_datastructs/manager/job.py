from dataclasses import dataclass
from typing import Any

from .task_type import TaskType


@dataclass(frozen=True)
class Job:
    job_id: str
    task_type: TaskType
    payload: Any

    def __post_init__(self):
        if not isinstance(self.job_id, str) or not self.job_id:
            raise ValueError('job_id must be a non-empty string')
        if not isinstance(self.task_type, TaskType):
            raise ValueError(f'task_type must be a TaskType enum member, got {type(self.task_type)}')
