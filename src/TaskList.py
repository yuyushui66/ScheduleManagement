import Task
from itertools import count


class TaskList:
    taskListCounter = count(0)

    def __init__(self):
        self.taskListID = next(TaskList.taskListCounter)  # int, primary key for a task list
        self.taskList = []  # list of Tasks
        self.taskListView = []  # list of Tasks sorted
        self.taskListName = ""  # str
        self.taskListDescribe = ""  # str

    def addTask(self, task: Task):
        self.taskList.append(task)

    def removeTask(self, task: Task):
        self.taskList.remove(task)

    # getter
    def getTaskListID(self):
        return self.taskListID

    def getTaskListName(self):
        return self.taskListName

    def getTaskListDescribe(self):
        return self.taskListDescribe

    def getTask(self, taskID: int):
        return self.taskList[taskID]

    def getTaskList(self):
        return self.taskList

    def getTaskListView(self):
        return self.taskListView

    # setter
    def setTaskListName(self, name: str):
        self.taskListName = name

    def setTaskListDescribe(self, desc: str):
        self.taskListDescribe = desc

    def setTask(self, taskID: int, task: Task):
        self.taskList[taskID] = task

    def setTaskList(self, taskList: list):
        self.taskList = taskList

    def setTaskListView(self, taskListView: list):
        self.taskListView = taskListView

    # manipulate
    def sortTaskListByPriority(self):
        self.taskListView.sort(key=lambda x: x.taskPriority)

    def sortTaskListByTime(self):
        self.taskListView.sort(key=lambda x: x.creationDateTime)

    def sortTaskListByStatus(self):
        self.taskListView.sort(key=lambda x: x.taskStatus)

    def sortTaskListByCategory(self):
        self.taskListView.sort(key=lambda x: x.taskCategory)

    def showTasks(self):
        print("Task List: " + self.taskListName + "\n")
        print("Task List Description: " + self.taskListDescribe + "\n")
        for task in self.taskListView:
            print(task.taskName, end=" ")

    #modify a task using kwargs
    def modifyTask(self, taskID: int, **kwargs):
        for key, value in kwargs.items():
            if key == "taskName":
                self.taskList[taskID].setTaskName(value)
            if key == "taskDescribe":
                self.taskList[taskID].setTaskDescribe(value)
            if key == "taskCategory":
                self.taskList[taskID].setTaskCategory(value)
            if key == "beginDateTime":
                self.taskList[taskID].setBeginDateTime(value)
            if key == "endDateTime":
                self.taskList[taskID].setEndDateTime(value)
            if key == "taskPriority":
                self.taskList[taskID].setTaskPriority(value)
            if key == "repetitive":
                self.taskList[taskID].setRepetitive(value)
            if key == "repeatTimeLoop":
                self.taskList[taskID].setRepeatTimeLoop(value)
            if key == "needReminding":
                self.taskList[taskID].setNeedReminding(value)
            if key == "remindDateTime":
                self.taskList[taskID].setRemindDateTime(value)


    

