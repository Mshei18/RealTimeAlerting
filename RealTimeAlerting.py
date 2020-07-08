import string

try:

    data = input("Enter in this format (SERVER_ID, CPU_UTILIZATION, MEMORY_UTILIZATION, DISK_UTILIZATION): ")

    #if data != '(' + type() + ', ' + type(str) + ', ' + type(str) + ', ' + type(str) + ', ' + ')':
    #    print("error")

    #if not type(data) is str:
        #raise TypeError("Only strings are allowed")

    seperate = data.split()

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

    flag1 = False
    flag2 = False
    flag3 = False

    numVilations = 0

    if (cpu > 85):
        flag1 = True
        numVilations += 1

    if (mem > 75):
        flag2 = True
        numVilations += 1

    if (disk > 60):
        flag3 = True
        numVilations += 1


    if (numVilations == 1 and flag1 == True):
        output = "(Alert " + serverid  + ', ' + "CPU_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 1 and flag2 == True):
        output = "(Alert " + serverid  + ', ' + "MEMORY_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 1 and flag3 == True):
        output = "(Alert " + serverid  + ', ' + "DISK_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 2 and flag3 == True and flag2 == True):
        output = "(Alert " + serverid  + ',' + "MEMORY_UTILIZATION VIOLATED" +  ', ' "DISK_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 2 and flag1 == True and flag2 == True):
        output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "MEMORY_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 2 and flag1 == True and flag3 == True):
        output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "DISK_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 3):
        output = "(Alert " + serverid  + ',' + "CPU_UTILIZATION VIOLATED" + ', ' + "MEMORY_UTILIZATION VIOLATED" +  ', ' + "DISK_UTILIZATION VIOLATED" + ')'

    elif (numVilations == 0):
        output = "(No Alert " + serverid  + ')'

    else:
        output = "Error"

    print(output)

except:
    print("Invalid data entered")





    


