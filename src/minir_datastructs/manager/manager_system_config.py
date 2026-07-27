import time
from dataclasses import dataclass, field
from typing import Dict, Optional, Any

from .constants import RunnerTaskHandler
from .job import Job
from .task_type import TaskType


def handle_echo_task_runner_logic(job: Job) -> Any:
    time.sleep(0.01)
    return job.payload

@dataclass
class ManagerSystemConfig:
    num_runners: int
    max_runners: int = 0
    default_runner_connect_timeout: float = 10.0
    shutdown_timeout_per_runner: float = 3.0
    runner_task_handlers: Dict[TaskType, RunnerTaskHandler] = field(default_factory=lambda: {TaskType.ECHO: handle_echo_task_runner_logic})
    command_pipe_path: Optional[str] = None
