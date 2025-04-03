contents=["all are my friends","the carrots","the potatos"]
filenames=["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(contents,filenames):
    file=open(f"files/{filename}","w")
    file.write(content)