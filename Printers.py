
class printer:
    def __init__(self):
        self.current_job = None

    def get_job(self,printer_Q):        
        try:
            self.current_job= printer_Q.DQueue()
        except IndexError:  # Queue is empty
            return "No more jobs to print."
        
    def print_job(self):
        while(not self.current_job.check_complete()):
            print(f'printing page{self.current_job.pages}')
            self.current_job.print_page()
        if self.current_job.check_complete():
            print('job is complete')
        else:
            print(f'an error occuerd while printing at page {self.current_job.pages}')
        