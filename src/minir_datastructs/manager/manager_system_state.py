from collections import deque
from dataclasses import dataclass, field
from multiprocessing import Event
from threading import Thread, RLock as ThreadRLock
from typing import Any, Deque, Dict, Optional

from .job import Job
from .job_state import JobState
from .manager_system_config import ManagerSystemConfig
from .runner_info import RunnerInfo
from minir_datastructs.pipe.pipe_reader import PipeReader


@dataclass
class ManagerSystemState:
    config: ManagerSystemConfig
    runners_info: Dict[int, RunnerInfo] = field(default_factory=dict)
    job_states: Dict[str, JobState] = field(default_factory=dict)
    jobs_master_list: Dict[str, Job] = field(default_factory=dict)
    job_queue: Deque[Job] = field(default_factory=deque)
    job_data_lock: ThreadRLock = field(default_factory=ThreadRLock)
    job_queue_lock: ThreadRLock = field(default_factory=ThreadRLock)
    runner_admin_lock: ThreadRLock = field(default_factory=ThreadRLock)
    shutdown_event: Event = field(default_factory=Event)
    command_pipe: Any = None
    command_pipe_reader: Optional[PipeReader] = None
    command_listener_thread_obj: Optional[Thread] = None
    next_runner_id_to_assign_job: int = 0
    next_available_runner_id: int = 0
