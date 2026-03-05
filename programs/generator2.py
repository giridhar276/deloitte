


def follow(file_path):
    f = open(file_path, "r", encoding="utf-8")
    #f.seek(0, 2)  # jump to end of file (like tail -f)
    try:
        while True:
            line = f.readline()
            if line:
                yield line.rstrip("\n")
    finally:
        f.close()

it = iter(follow("employee_info.csv"))

print("Next log:", next(it))   # waits until a new line appears in app.log
print("Next log:", next(it))
