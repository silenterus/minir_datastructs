from dataclasses import dataclass
from typing import Dict, Optional

from .constants import RunnerTaskHandler
from .task_type import TaskType


@dataclass
class RunnerConfig:
    runner_id: int
    task_handlers: Dict[TaskType, RunnerTaskHandler]
    manager_pid: Optional[int] = None
