with open("./Input/Names/invited.txt") as invited:
    name_list = (invited.readlines()) 

with open("./Input/Letter/starting.txt") as file:
    content = file.read()

    for name in name_list:
        name = name.strip()
        new = content.replace("[name]", name)
        with open(f"./Output/Send/letter_for_{name}.txt", mode="w") as file_path:
            file_path.write(new)
