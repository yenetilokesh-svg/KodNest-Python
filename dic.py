# {Key:Value}, mutable, key cannot be duplication

student = {
    'name' : "Amit",
    "age" : 21,
    "Course" : "Computr Science",
    "Tech" : ["Computer Science", "Python", "SQL"]
}
student.update({'cgpa' : 8.5})
print(student["age"])
print(student, type(student), len (student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))

print(student.pop("Course"))
student.popitem() # last item
student.clear() # remove all items
del student
#print(student)

student = {
    "name": "Rahul",
    "age": 23,
    "Tech" : ["Pyhton", "SQL"]
}

student.setdefault("age", 22)
print(student)

keys = ["name", "age", "course"]
y = 0

student = dict.fromkeys(keys, y)
print(student)

my_dict = student.copy()
print(my_dict)
my_dict.update({'name': "Amit"})
print(my_dict)