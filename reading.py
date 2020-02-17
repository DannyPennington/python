file = open("teams.txt","w+")
file.write("Liverpool \n")
file.write("Manchester Utd \n")
file.write("Manchester City \n")
file.write("Real Madrid \n")
file.write("PSG \n")
file.seek(0)

for i in range(5):
    if i == 0 or i == 3:
        print("Line %d: " %(i+1), file.readline())
        
    else:
        file.readline()

file.close()