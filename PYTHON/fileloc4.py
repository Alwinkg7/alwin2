f=open("test.txt","w")
f.write("sample file\n")
f.write("This sample\n\n")
f.write("have a name\n")
f=open("test.txt","r")
str=f.read()
print("read strings: ",str)
f.close()
print(f.name,"is closed")