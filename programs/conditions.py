# simple if
if 1 < 2 :
    print("true")
# if-else
name = "python"
if name.startswith("p"):    
    print("its python")
    print("inside if")
    print("still inside if ")
else:
    print("its someother language")
######################################
if name.isupper():
    print("string is upper")

######################################
lang = input("Enter any language :")
if lang == "python":
    print("you are learning python")
elif lang == "java":
    print("you are learning java")
elif lang == "oracle":
    print("you are learning oracle")
else:
    print("you are learning tool")
