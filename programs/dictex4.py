


students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]

for item in students:
    print(item['name'])
    print("-----------")

    for key,value in item['marks'].items():
        print("Subject:",key)
        print("Marks:",value)
        print()

#######################################
for item in students:
    print(item['name'])
    print("-----------")
    print(list(item['marks'].values()))