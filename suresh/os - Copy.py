import os
if os.path.exists("yohoho.txt"):
    with open("yohoho.txt","r")as file:
        print(file.read())
else:
    print("file does not exists")
    
