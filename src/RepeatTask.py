from Task import Task, TaskStatus
import datetime
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


class RTask(Task):
    def __init__(self,
                 # Task's
                 _taskName: str = '',
                 _taskDescribe: str = '',
                 _taskCategory: int = 0,
                 _taskPriority: int = 100,
                 _taskStatus: int = TaskStatus.NULL,
                 _needReminding: bool = False,
                 _remindDateTime: datetime = None,
                 # RTask's
                 # Repetitive: bool = True
                 _rMode: RMode = RMode.CYCLE,
                 _rFrequency: RFrequency = RFrequency.DAILY,
                 _rDuration: int = 0,
                 ):
        super(RTask, self).__init__()
        super().__init__()
        self.rMode: RMode = _rMode

        self.rFrequencyEnabled: bool = True  # enabled when rMode=CYCLE
        self.rFrequency: RFrequency = _rFrequency
        self.rFrequencyListEnabled: bool = True  # enabled when rMode=CYCLE
        self.rFrequencyList: list = []  # enabled when rMode=CYCLE

        self.rDurationEnabled: bool = False  # enabled when rMode=DURATION
        self.rDuration: int = _rDuration  # in days

        self.rSelectionEnabled: bool = False  # enabled when rMode=SELECTION
        self.rSelectionList: list = []  # enabled when rMode=SELECTION

    def setRMode(self, mode: RMode):
        self.rMode = mode

        if mode == RMode.CYCLE:
            self.rFrequencyEnabled = True
            self.rFrequencyListEnabled = True
            self.rDurationEnabled = False
            self.rSelectionEnabled = False
        elif mode == RMode.DURATION:
            self.rFrequencyEnabled = False
            self.rFrequencyListEnabled = False
            self.rDurationEnabled = True
            self.rSelectionEnabled = False
        elif mode == RMode.SELECTION:
            self.rFrequencyEnabled = False
            self.rFrequencyListEnabled = False
            self.rDurationEnabled = False
            self.rSelectionEnabled = True

    # Avaliable only when rMode=CYCLE
    def setRFrequency(self, frequency: RFrequency, frequencyList: list = []):
        if frequency == RFrequency.NONE or self.rMode != RMode.CYCLE:
            return
        self.rFrequency = frequency
        if self.rFrequency != RFrequency.DAILY:
            self.rFrequencyList = frequencyList
            return True
        elif self.rFrequency == RFrequency.DAILY:
            self.rFrequencyListEnabled = False
            self.rFrequencyList = []
            return True
        else:
            return False

    def setDuration(self, duration: int):
        if self.rMode != RMode.DURATION:
            return
        self.rDuration = duration

    def setSelection(self, selectionList: list):
        if self.rMode != RMode.SELECTION:
            return
        self.rSelectionList = selectionList

    def getRMode(self):
        return self.rMode

    def getRFrequency(self):
        return self.rFrequency

    def getFrequencyList(self):
        return self.rFrequencyList

    def getDuration(self):
        return self.rDuration

    def getSelectionList(self):
        return self.rSelectionList

    def getRModeEnabled(self):
        return self.rMode

    def getRFrequencyEnabled(self):
        return self.rFrequencyEnabled

    def getRFrequencyListEnabled(self):
        return self.rFrequencyListEnabled

    def getRDurationEnabled(self):
        return self.rDurationEnabled

    def getRSelectionEnabled(self):
        return self.rSelectionEnabled

