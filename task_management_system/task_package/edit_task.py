from .task import task
def edit_task(task,new_title=None,new_description=None,new_catagory=None):
    if new_title:
        task.title=new_title
    if new_description:
        task.description=new_description
    if new_catagory:
        task.catagory=new_catagory
     