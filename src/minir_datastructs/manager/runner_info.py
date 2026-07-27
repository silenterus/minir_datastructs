from dataclasses import dataclass
from multiprocessing import Process
from typing import Any, Optional

from .runner_status import RunnerStatus
from minir_datastructs.pipe.pipe_reader import PipeReader


@dataclass
class RunnerInfo:
    runner_id: int
    status: RunnerStatus = RunnerStatus.INITIALIZING
    process: Optional[Process] = None
    runner_pid: Optional[int] = None
    m2r_pipe_path: Optional[str] = None
    r2m_pipe_path: Optional[str] = None
    m2r_pipe: Any = None
    r2m_pipe: Any = None
    pipe_reader: Optional['PipeReader'] = None
    current_job_id: Optional[str] = None
