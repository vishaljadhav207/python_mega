import glob

myFiles=glob.glob("../files/*.txt")
print(myFiles)

for filepath in myFiles:
    with open(filepath,"r")as file:
        print(file.read())