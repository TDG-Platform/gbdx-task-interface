# GBDX Task Python interface
 
 To use:
  1. Derive your class from GbdxTaskInterface. 
  2. Implement invoke() function.
  3. Use context management to run your task:
  ```Python
  with MyTask() as task:
        task.invoke()
  ```
