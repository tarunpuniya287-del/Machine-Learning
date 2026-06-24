marks = {
    "Tarun": 89,
    "Harry": 65,
    "Vishal": 68,
    
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry": 89})
print(marks)

print(marks.get("Tarun"))
print(marks["Tarun"])