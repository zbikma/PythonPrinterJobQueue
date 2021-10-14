from queues import Queue
from jobs import Job
from Printers import printer

print_Q=Queue()
my_printer=printer()
for i in range(5):    
    print_Q.AQueue(Job())
print(print_Q.items)
for j in range(print_Q.size()) :
    print(f'printing {j+1}')
    my_printer.get_job(printer_Q=print_Q)
    my_printer.print_job()




