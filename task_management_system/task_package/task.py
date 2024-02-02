class task:
    def __init__(self,title,description,catagory=None):
        self.title=title
        self.description=description
        self.catagory=catagory
    def __str__(self):
        return f"{self.title}-{self.description}(Category:{self.catagory})"
    