path = "C:/Users/lgowda/Desktop/ASI.txt"
file = open(path, "r")
text = file.readlines()
new_file_output= open("new file","w")
for line in text:

    if line.strip() == "5.FIVE":
        continue
    new_file_output.write(line)
