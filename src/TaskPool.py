import Task
from itertools import count

class TaskPool:

    _taskCounter = count(0)
    def __init__(self):
        self.taskPool = [] # list of TaskList

    def createTask(self, task:Task):
        task.taskID=next(TaskPool._taskCounter)
        self.taskPool.append(task)



    def addTaskList(self, taskList: Task.TaskList):
        self.taskPool.append(taskList)

    def removeTaskList(self, taskList: Task.TaskList):
        self.taskPool.remove(taskList)

    def getTaskList(self, taskListID: int):
        return self.taskPool[taskListID]

    def getTaskPool(self):
        return self.taskPool

    def setTaskList(self, taskListID: int, taskList: Task.TaskList):
        self.taskPool[taskListID] = taskList

    def setTaskPool(self, taskPool: list):
        self.taskPool = taskPool

    def showTaskLists(self):
        pass