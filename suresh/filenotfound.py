try:
    file_name=input("Enter the file name to read:")
    with open(file_name,'r')as file:
        content=file.read()
        print("File Content:\n",content)
except FileNotFoundError:
    print("Error: this file was not found")
finally:
    print("file operation is complete")
