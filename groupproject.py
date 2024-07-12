records = []


for i in range(2):
    groupname = input("Enter the group name")
    groupsize = input("Enter the size of the group")
    groupdate = input("Enter the date of the venue")
    groupplace = input("Enter the place of the venue")
    groupmedal = input("Enter the type of medal won")

    x=(groupname,groupsize,groupdate,groupplace,groupmedal)
    records.append(x)
    
for i in records:
    print(i)


