from gbdx_task_interface import GbdxTaskInterface


class MyTask(GbdxTaskInterface):
    def invoke(self):
        # Do cool stuff
        return True


if __name__ == "__main__":
    with MyTask() as task:
        task.invoke()
