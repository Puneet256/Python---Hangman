from chooseWord import chooseWord

word_data = chooseWord()

word = word_data[0]
length = word_data[1]
answer = []
answer_temp = []
lives = 6

print(word)
print("+++++++++++ WELCOME TO HANGMAN +++++++++++\n\n")

for i in range(0,length):
    answer.append("_")
    answer_temp.append("_")
    print(answer[i], end=" ")

while(lives>0):
    user_input = input("\nSelect a Letter: ")

    for x in range (0,length):
        if user_input == word[x]:
            answer_temp[x] = user_input

    if answer_temp != answer:
        for i in range(0,length):
            answer[i] = answer_temp[i]
            print(answer[i], end=" ")

        if ''.join(answer) == word:
            exit("\n\n ========== CONGRATULATIONS. You Win! ==========")

    else:
        lives -= 1
        print("\n\'%s\' is not in the word (or you have already selected it)\nYou have %d lives remaining" % (user_input,lives))

print("========== You are out of lives. You Lose! ==========")
