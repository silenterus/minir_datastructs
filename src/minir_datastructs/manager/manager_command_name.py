from enum import Enum


class ManagerCommandName(Enum):
    SHUTDOWN_MANAGER = 'shutdown_manager'
    SUBMIT_JOB = 'submit_job'
    GET_JOB_STATUS = 'get_job_status'
    START_RUNNER = 'start_runner'
    STOP_RUNNER = 'stop_runner'
