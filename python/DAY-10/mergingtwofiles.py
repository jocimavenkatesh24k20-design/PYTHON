with open ("DAY-10/Merge1.txt","r") as f1, open("DAY-10/Merge2.txt","r") as f2:
    text=f1.read() + "\n" + f2.read()
with open("DAY-10/Mergedfile.txt","w") as f:
    f.write(text)