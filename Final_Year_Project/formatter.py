def ToFormat(s):
    l = s.split("\n")
    name = l[2]
    vehName = l[6]
    regNo = l[10]
    regDate = l[14]
    print("Name : "+str(name),end='')
    print("Vehicle Name : "+str(vehName),end='')
    print("Registration Number : "+str(regNo),end='')
    print("Registration date : "+str(regDate),end='')
