import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    import string
    alerts = []

    #data = input("Enter in this format (SERVER_ID, CPU_UTILIZATION, MEMORY_UTILIZATION, DISK_UTILIZATION): ") 
    
    try:

        f = open("TestCases.txt")

    except:
        print("File can not be opened")
    try:

        data = f.readlines()
        f.close()

    except:
        print("File can not be read")


    try:
        # Splitting string into numbers and converting into integers
        for x in data:
            seperate = x.split()

            serverid = seperate[0]
            serverid = serverid.replace(',', '')
            serverid = serverid.replace('(', '')

            cpu = seperate[1]
            cpu = cpu.replace(',', '')
            cpu = int(cpu)

            mem = seperate[2]
            mem = mem.replace(',', '')
            mem = int(mem)

            disk = seperate[3]
            disk = disk.replace(',', '')
            disk = disk.replace(')', '')
            disk = int(disk)

            output = "(Alert " + serverid

            if (cpu > 85):
                output += " ,CPU_UTILIZATION VIOLATED" 

            if (mem > 75):
                output += " ,MEMORY_UTILIZATION VIOLATED" 

            if (disk > 60):
                output += " ,DISK_UTILIZATION VIOLATED" 

            output += ') '

            if output == "(Alert " + serverid + ')':
                output = "(No Alert " + serverid  + ')'

            alerts.append(output)
            
    
        return HttpResponse(alerts)

    except:
        print("Output failed")
    


   



    



    



    

