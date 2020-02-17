# Reading the orignal file and saving each line to a list
with open("teams.txt","r") as teams:
    temp = teams.readlines()

# Wiping the file then adding our new line then re-adding the original lines
with open("teams.txt","w") as teams:
    teams.write("This is a new line \n")
    for i in range(1,len(temp)):
        teams.write(temp[i])

# Reading the file line by line
with open("teams.txt","r") as teams:
    for i in range(len(temp)):
        print("Line %d: " %(i+1), teams.readline())
