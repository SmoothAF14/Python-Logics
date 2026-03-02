#1
template = "Hello <<UserName>>, How are you?"
name = input("Enter your name(minimum 3 characters) : ")
if len(name) < 3:
    print("Name should be minimum 3 characters")
else:
    print(template.replace("<<UserName>>", name))