from enum import Enum


class RMode(Enum):
    CYCLE = 0
    DURATION = 1
    SELECTION = 2


class RFrequency(Enum):
    NONE = 0
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    YEARLY = 4

class TaskStatus(Enum):
    YET_TO_BEGIN = 0
    PROCESSING = 1
    DONE = 2
    FAILED = 3
    ABANDONED = 4
    NULL = 5
