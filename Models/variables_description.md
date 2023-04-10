## class Task

    - id: int
    - name: string
    - description: string
    - category: dict<int, string>
    - created_at: datetime
    - begin_at: datetime
    - end_at: datetime
    - priority: int
    - status: enum
    - repetitive: bool
    - repeatPattern: ReapeatPattern
    - needReminder: bool
    - reminderTime: datetime

    with getters and setters

## class TaskManager

    - id: int
    - name: string
    - description: string
    - list: list<Task>
    - listView: list<Task>

    getter and setter for self.vars
    addTask(Task task)
    removeTask(Task task)
    getTask(int id)
    setTask(int id, Task task)
    
## Repeat Pattern

![img_1.png](img_1.png)

## Database User Group

There are 2 users.

-1- `root`: (passwordHidden)

-2- `user1`: password1

`root` has all privileges on all databases.

`user1` has `select`, `insert` privileges on database `SMDB`.

If you are using database `SMDB` as a user, please connect with `user1`, not `root`.




