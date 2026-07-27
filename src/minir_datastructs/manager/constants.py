import struct
from typing import Callable, Any, Union

from .error_from_runner import ErrorFromRunner
from .job import Job
from .job_request_to_runner import JobRequestToRunner
from .job_result_from_runner import JobResultFromRunner
from .ping_from_manager import PingFromManager
from .runner_ready_signal import RunnerReadySignal
from .shutdown_command_to_runner import ShutdownCommandToRunner
from .status_update_from_runner import StatusUpdateFromRunner

ERROR_PIPE_BUSY = 231
ERROR_FILE_NOT_FOUND = 2
APP_NAME = 'min_pipe_runner_tester'
MANAGER_COMMAND_PIPE_NAME_BASE = 'manager_command'
PIPE_TEMPLATE_M2R = 'm2r'
PIPE_TEMPLATE_R2M = 'r2m'
GLOBAL_PIPE_IDENTIFIER = 'global'
RUNNER_CRITICAL_ERROR_JOB_ID_PREFIX = 'runner_critical_'
DEFAULT_ENCODING = 'utf-8'
THREAD_NAME_MANAGER_CMD_LISTENER = 'ManagerCmdListener'
RUNNER_PROCESS_NAME_PREFIX = 'Runner-'


ERROR_BROKEN_PIPE = 109
ERROR_MORE_DATA = 234
ERROR_NO_DATA = 232
ERROR_PIPE_NOT_CONNECTED = 233
HEADER_FORMAT = '>L'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
MANAGER_LOGGER_NAME = 'ManagerRunner'
RunnerTaskHandler = Callable[[Job], Any]


RunnerToManagerMessage = Union[StatusUpdateFromRunner, RunnerReadySignal, JobResultFromRunner, ErrorFromRunner]
ManagerToRunnerMessage = Union[JobRequestToRunner, ShutdownCommandToRunner, PingFromManager]


