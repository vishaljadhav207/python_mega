# Open your computer IDE and place the following in a Python file:
#
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# Then, create a program that:
#
# 1. generates multiple text files by iterating over the filenames list,
#
# 2. and writes the text Hello  inside each generated text file.

filenames = ['doc1.txt', 'report1.txt', 'presentation1.txt']

for filename in filenames:
    file=open(f"files/{filename}","w")
    file.write("Hello")
