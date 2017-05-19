# GBDX Task Python interface
 
 To use:
  1. Derive your class from GbdxTaskInterface. 
  2. Implement invoke() function.
  3. Use context management to run your task:
  ```Python
  with MyTask() as task:
        task.invoke()
  ```
  
  Refer to the example.py for usage

## Development and Debugging
When developping or debugging it can be helpful to "run" the task locally.
You can locally create a folder that will mimic the input structure that the task will see when it is run.
You can then set this task interface to use this local folder.

__Create the derived GbdxTaskInterface with the local folder location__
```
MyTask(work_path="/local/folder/location")
```

Then when you locally run the task it will read from and write to this directory.
Note: you will need to remove this work_path from the task when the task is run on the workflow system.

### Create a local workflow task location
To run the above local folder you need to setup the data like the workflow system does
which includes the following

For details see: https://gbdxdocs.digitalglobe.com/docs/task-and-workflow-course


```
/
└── local/folder/location
    ├── gbdx_runtime.json (use to mimic getting tokens from user impersonation)
    ├── input
    |   ├── ports.json (if you use string ports)
    |   └── input_directory_port (one directory per input dir port)
    |       ├── file1.txt
    |       ├── file2.txt
    |       └── file3.txt
    └── output (create this folder but leave empty)
```

#### gbdx_runtime.json
Run time information like the passed token used by user impersonation.  
Contents should look something like this:
```
{
    "user_token":"FAKE_TOKEN"
}
```

#### ports.json
Place your input sting ports in this file inside the input directory
```
{
	"input_string_port_name": "really useful data!"
}
```

#### Create input directory ports
Create folders named after the input directory ports and fill them with your input data files


### After you run your task
You should see your output folder populated and a status.json file created.  If you output any string ports there should be a ports.json file created in the output folder.
For each output directory port there should be a folder created with the generated files.
```
/
└── local/folder/location
    ├── gbdx_runtime.json (use to mimic getting tokens from user impersonation)
    ├── input
    |   ├── ports.json (if you use string ports)
    |   └── input_directory_port (one directory per input dir port)
    |       ├── file1.txt
    |       ├── file2.txt
    |       └── file3.txt
    └── output
    |    ├── ports.json (if you output string ports)
    |    └── output_directory_port (one directory per outputput dir port)
    |       ├── file1.txt
    |       ├── file2.txt
    |       └── file3.txt
    └── status.json    
```

#### status.json
This file is creted on task completion and contains the final status and the "note"
```
{
    "status": "success", 
    "reason": "Task succes status note"
}
```

