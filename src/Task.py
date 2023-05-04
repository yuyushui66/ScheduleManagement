import time
import datetime
from enum import Enum
from itertools import count


class TaskStatus(Enum):
    YET_TO_BEGIN = 0
    PROCESSING = 1
    DONE = 2
    FAILED = 3
    ABANDONED = 4
    NULL = 5


# TODO: function -> Task.repeat()


class Task:
    _instanceCounter = count(0)

    @staticmethod
    def readCategories():
        # need to read from db or file.
        return dict()  # dict<int, str>

    def __init__(self, _taskName: str = '',
                 _taskDescribe: str = '',
                 _taskCategory: int = 0, _taskPriority: int = 100,
                 _taskStatus: TaskStatus = TaskStatus.NULL,
                 _needReminding: bool = False, _remindDateTime: datetime = False):
        self.taskCategories = Task.readCategories()  # dict<int,str>
        self.taskID = 0  # int, primary key for a task
        self.taskName = _taskName  # str
        self.taskDescribe = _taskDescribe  # str
        self.taskCategory = _taskCategory  # int, show by dict<int, string>(i)
        self.creationDateTime = datetime.datetime.now()  # datetime
        self.beginDateTime = datetime.datetime.now()  # datetime
        self.endDateTime = datetime.datetime.now()  # datatime
        self.taskPriority = _taskPriority  # 0 for highest
        self.taskStatus = _taskStatus  # enum(TaskStatus)
        self.needReminding = _needReminding  # boolean
        self.remindDateTime = datetime.datetime.now()  # datetime

    # setter
    def setTaskName(self, name: str): self.taskName = name

    def setTaskDescribe(self, desc: str): self.taskDescribe = desc

    def setTaskCategory(self, cat_id: dict): self.taskCategory = self.taskCategories[cat_id]

    def setBeginDateTime(self, dt: datetime): self.beginDateTime = dt

    def setEndDateTime(self, dt: datetime): self.endDateTIme = dt

    def setTaskPriority(self, prio: int): self.taskPriority = prio

    def setNeedReminding(self, flag: bool): self.needReminding = flag

    def setRemindDateTime(self, dt: datetime): self.remindDateTime = dt

    # getter

    def getTaskID(self): return self.taskID

    def getTaskName(self): return self.taskName

    def getTaskDescribe(self): return self.taskDescribe

    def getTaskCategory(self): return self.taskCategory

    def getCreationDateTime(self): return self.creationDateTime

    def getBeginDateTime(self): return self.beginDateTime

    def getEndDateTime(self): return self.endDateTime

    def getTaskPriority(self): return self.taskPriority

    def getTaskStatus(self): return self.taskStatus

    def getNeedReminding(self): return self.needReminding

    def getRemindDateTime(self): return self.remindDateTime
