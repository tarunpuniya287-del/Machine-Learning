try:
    class detail:
        name = "Rahul"
        age = 20
        language = "Python"
        
    tarun = detail()
    print(tarun.name, tarun.age)

    class Company:
        MNC = "Google" # This is a class attribute
        NC = "Infosys"

    Big_startup = Company()
    office = "Accenture" # This is a object/Instance attribute
    print(office, Big_startup.MNC, Big_startup.NC)
    # Here office is object attribute and MNC and NC are class attribute as they directly belong to the class

    # now talking about instance attribute 
    class Company:
        MNC = "Google" 
        NC = "Infosys"
    # Now question is which one will print google or Amazon the answer is amazon because in Instance ya object attribute it will prefecrence over class attribute 
    Big_startup = Company()
    Big_startup.MNC = "Amazon"
    print(f"The name of the comapany will be:", Big_startup.MNC , "\nThe big firm is:", Big_startup.NC)
    
    class detail:
        name = "Rahul"
        age = 20
        skill = "Python"

        def getInfo(see):
            print(f"The language tarun knows {see.skill}. The age of tarun is {see.age}")
        def greet(see):
            print("Good Morning")
    tarun = detail()
    skill = ["SQL", "Web dev", "Data Science"]
    print(f"The skill gained rahul:", skill,"\n", tarun.age, tarun.name )
    tarun.getInfo()
    tarun.greet()
except:
    print("There is a error in a code:")
    







