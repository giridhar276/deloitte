try:
    with open("languages.txt","w") as fobj:
        fobj.write("python\n")
        fobj.writelines(["unix","java","oracle\n"])
except Exception as err:
    print(err)



try:
    with open("languages.txt","w") as fobj:
        fobj.write("python\n")
        fobj.writelines(["unix","java","oracle\n"])
except TypeError as err:
    print("Invalid operation ",err)
except ValueError as err:
    print("Invalid input",err)
except (IndexError,KeyError) as err:
    print("Invalid idnex or invalid dictionary",err)
except Exception as err:
    print(err)




try:
    with open("languages.txt","w") as fobj:
        fobj.write("python\n")
        fobj.writelines(["unix","java","oracle\n"])
except Exception as err:
    print(err)
else:
    for val in range(1,10):
        fobj.write(str(val) + "\n")
finally:
    print("end of the code")
