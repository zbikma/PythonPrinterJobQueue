import random
class Job:
    def __init__(self):
        self.pages=random.randint(1,11)
    def print_page(self):
        if self.pages>0:
            self.pages-=1
        
    def check_complete(self):
        return self.pages==0
