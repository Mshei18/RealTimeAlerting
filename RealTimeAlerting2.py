import string

 #data = input("Enter in this format (SERVER_ID, CPU_UTILIZATION, MEMORY_UTILIZATION, DISK_UTILIZATION): ") 
 
try:

    f = open("TestCases.txt")

except:
    print("File can not be opened")
try:

    data = f.readlines()

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

        numVilations = 0

        if (cpu > 85):
            numVilations += 1

        if (mem > 75):
            numVilations += 1

        if (disk > 60):
            numVilations += 1

        if (numVilations == 1 and cpu > 85):
            output = "(Alert " + serverid  + ', ' + "CPU_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 1 and mem > 75):
            output = "(Alert " + serverid  + ', ' + "MEMORY_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 1 and disk > 60):
            output = "(Alert " + serverid  + ', ' + "DISK_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 2 and mem > 75 and disk > 60):
            output = "(Alert " + serverid  + ',' + "MEMORY_UTILIZATION VIOLATED" +  ', ' "DISK_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 2 and cpu > 85 and mem > 75):
            output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "MEMORY_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 2 and cpu > 85 and disk > 60):
            output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "DISK_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 3):
            output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "MEMORY_UTILIZATION VIOLATED" +  ', ' + "DISK_UTILIZATION VIOLATED" + ')'

        elif (numVilations == 0):
            output = "(No Alert " + serverid  + ')'

        else:
            output = "Error"

        print(output)
except:
    print("Output printing failed")



    



    


