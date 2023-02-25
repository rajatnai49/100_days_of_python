import random
import requests
from art import vs


def pokemon_stat_compare(highScore):
    def pokemon_res(total_pokemon):
        id = random.choice(total_pokemon)
        res = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{id}")
        print(res.status_code)
        if res.status_code != 204 and res.status_code != 404:
            if res.json() is not None and "stats" in res.json() and "name" in res.json():
                return res.json()
        else:
            pokemon_res(total_pokemon)

    score = 0
    correct = True

    while correct:
        total_pokemon = list(range(1, pokemon_count))
        first_pokemon = pokemon_res(total_pokemon)
        first_pokemon_name = first_pokemon["name"]
        first_pokemon_stats = 0
        for stat in first_pokemon["stats"]:
            first_pokemon_stats += stat["base_stat"]
        print(f"{first_pokemon_name} have total {first_pokemon_stats}")

        second_pokemon = pokemon_res(total_pokemon)
        second_pokemon_name = second_pokemon["name"]
        second_pokemon_stats = 0
        for stat in second_pokemon["stats"]:
            second_pokemon_stats += stat["base_stat"]
        print(f"{second_pokemon_name} have total {second_pokemon_stats}")

        print(f"Pokemon A: {first_pokemon_name}")
        print(vs)
        print(f"Pokemon B: {second_pokemon_name}")

        a_or_b = input("\nWhich pokemon have higher base-stat: ").lower()

        if (a_or_b == 'a' and first_pokemon_stats >= second_pokemon_stats) or (a_or_b == 'b' and first_pokemon_stats <= second_pokemon_stats):
            score += 1
        else:
            highScore = max(highScore, score)
            print(f"Current Score is {score} and high score is {highScore}")
            correct = False
            break

    play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        pokemon_stat_compare(highScore=highScore)
    elif play_again == 'n':
        print("Thanks for playing!")


response = requests.get("https://pokeapi.co/api/v2/pokemon/")
pokemon_count = response.json()["count"]
highScore = 0
pokemon_stat_compare(highScore)
