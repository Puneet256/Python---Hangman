from random import randint
import csv

def chooseWord():
    with open('wordbank.csv') as words:
        for rows in words:
            row = rows.rstrip().split(', ')

    chosen_word = row[randint(0,len(row))]
    word_len = len(chosen_word)
    return chosen_word, word_len
