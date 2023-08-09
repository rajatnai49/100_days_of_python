import random
from data_set import adjectives, nouns


def generate_character_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return adjective + ' ' + noun


def main():
    print(generate_character_name())


if __name__ == "__main__":
    main()
