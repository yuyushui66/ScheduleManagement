import TaskList
import User


class TaskManager:

    def __init__(self, _user: User):
        self.taskLists = []
        self.importantTaskList = TaskList.TaskList("Important", "Tasks that are important")
        self.user = _user

    def addTaskList(self, taskList: TaskList):
        self.taskLists.append(taskList)

    def removeTaskList(self, taskList: TaskList):
        self.taskLists.remove(taskList)

    def getTaskList(self, taskListID: int):
        return self.taskLists[taskListID]

    def getTaskLists(self):
        return self.taskLists

    def setTaskList(self, taskListID: int, taskList: TaskList):
        self.taskLists[taskListID] = taskList

    def setTaskLists(self, taskLists: list):
        self.taskLists = taskLists

    def getUser(self):
        return self.user

    def setUser(self, user: User):
        self.user = user
