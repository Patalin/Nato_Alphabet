# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import pandas

my_data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_my_data = {row.letter: row.code for (index, row) in my_data.iterrows()}

my_word = input("Type your word: ").upper()
phonetic_words = [dict_my_data[letter] for letter in my_word]
print(phonetic_words)


