# Text on New Line

File = open("CardValues.txt", "w")

Flag = True
while Flag == True:
    Name = input("Enter the name of invited guest: ")
    if Name == "No":
        Flag = False
    else:
        File.write(Name + "\n")

File.close()

File = open("CardValues.txt", "a")
File.write("Muneeb" + "\n")
File.close()

File = open("CardValues.txt", "r")
isPresent = False
for Line in File:
    if Line.strip() == "Rohaan":
        isPresent = True
        print("Already Invited")

File = open("CardValues.txt", "a")
if isPresent == False:
    File.write("Rohaan" + "\n")
File.close()
