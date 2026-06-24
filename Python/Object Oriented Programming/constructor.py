
class detail:
        name = "Rahul"
        age = 20
        language = "Python"

        def __init__(self, name, language, age):
                self.name = name
                self.language = language
                self.age = age
                print("creating an object")


Rahul = detail("Rohan", "Java", 30)
print(Rahul.name, Rahul.language, Rahul.age)

