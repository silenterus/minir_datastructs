from dataclasses import dataclass


@dataclass(frozen=True)
class PingFromManager:
    manager_pid: int
