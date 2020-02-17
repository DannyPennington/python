with open("teams.txt","r") as teams:
    temp = teams.readlines()

with open("teams.txt","w") as teams:
    teams.write("This is a new line \n")
    for i in range(1,len(temp)):
        teams.write(temp[i])


with open("teams.txt","r") as teams:
    for i in range(5):
        print("Line %d: " %(i+1), teams.readline())
