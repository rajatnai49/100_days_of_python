def tip_calculator():
    tip = input("How much tip you want to give?")
    people = input("How many people are there?")
    per_person = float(tip)/float(people)
    return "Per person you have " + str(per_person)
print(tip_calculator())