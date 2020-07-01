**Question:4**

writeFile=open("fileHandling.txt","w")
string=input("Enter a string:")
writeFile.write(string)
writeFile.close()


readFile=open("fileHandling.txt")
print(readFile.readline())
