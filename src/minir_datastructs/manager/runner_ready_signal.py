from dataclasses import dataclass


@dataclass(frozen=True)
class RunnerReadySignal:
    runner_id: int
    pid: int
