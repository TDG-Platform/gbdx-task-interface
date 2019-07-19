import os
import shutil
from gbdx_task_interface import GbdxTaskInterface


class MyTask(GbdxTaskInterface):

    def invoke(self):

        # get input token
        # requires that the task and workflow allow user impersonation
        # See: https://gbdxdocs.digitalglobe.com/docs/workflow-api-course
        # token = self.get_runtime_info("user_token")

        # read input ports
        input_string_port_value = self.get_input_string_port("input_string_port_name", None)
        input_directory_port = self.get_input_data_port("input_directory_port_name")

        # write the output ports
        self.set_output_string_port("output_string_port_name", input_string_port_value)

        # write to an output directory port
        output_data_port = self.get_output_data_port('output dir')
        if not os.path.exists(output_data_port):
            os.mkdir(output_data_port)

        # copy all the input files to the output
        src_files = os.listdir(input_directory_port)
        for file_name in src_files:
            full_file_name = os.path.join(input_directory_port, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, output_data_port)

        # if the task throws the task will be marked failed and the error message added as the status note
        # raise (Exception("Error message status note"))

        # you can set the status "note" by adding to the reason
        self.reason = 'Task succes status note'

        return


if __name__ == "__main__":
    with MyTask() as task:
        task.invoke()
