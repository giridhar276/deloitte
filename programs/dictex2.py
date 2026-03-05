
# dict of dictionaries
employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


for value in employees.values():
    if "name" in value  and "deparment" in value:
        print(value["name"], value['department'])

print("--------------")

for key,value in employees.items():
    print(value["name"], value['department'])
print("--------------")

for key in employees:
    value = employees[key]
    print(value['name'],value["department"])