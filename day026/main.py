import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
input_word = input("Enter a word: ").upper()
ans = [nato_dict[letter] for letter in input_word]
print(ans)
