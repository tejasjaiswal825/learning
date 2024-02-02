from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.catagorize_task import catagorize_task
#crate a task
task1=create_task("complete your assignment",'finish task management system')
#display the task
print('task1:',task1)
#edit the task
edit_task(task1,new_title='upddated assignment',new_description='review and submitted to rashim mam')
#display the updated task
print('updated task1:',task1)
#categorize the task
catagorize_task(task1,'zappkode academy')
#display the categorized task
print('categorized task1:',task1)

