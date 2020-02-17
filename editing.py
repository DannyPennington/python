with open("teams.txt","r+") as teams:
    teams.seek(0)

    teams.writelines("This is a new line \n")
    teams.seek(0)
    for i in range(5):
        print("Line %d: " %(i+1), teams.readline())
        
        

        
