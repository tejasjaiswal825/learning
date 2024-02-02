from .task import task
def create_task(title,description,catagory=None):
    new_task=task(title,description,catagory)
    return new_task
