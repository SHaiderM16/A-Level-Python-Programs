# Filing

# Reading From File

File = open("CardValues.txt", "r")

# Read single line
FirstLine = File.readline()
print(FirstLine)

# Read entire file
Text = File.read()
print(Text)

# Read entire file using readline()
for i in range (0, 60, 1):
    WholeText = File.readline()
    print(WholeText)

File.close()
