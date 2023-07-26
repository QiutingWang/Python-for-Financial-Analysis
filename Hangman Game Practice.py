import random
import hangman_stage
import word_list

lives=6
chosen=random.choice(word_list.word_list)
print(chosen)

display=[]
for i in display(len(chosen)):
    display += '_'
print(display)

##guess the letter
game_over=False
while not game_over:
    guess_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen)):
       #get the letter
        letter=chosen[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display) #if the letter is correct, put the letter in the position.

    if guess_letter not in chosen:
        lives -= 1
        if lives == 0:
            game_over=True
            print("You Lose! ")

    if '_' not in display: #all blanks are filled in
        game_over=True
        print("You Win! ")
    print(hangman_stage.stages[lives])#triphthong


## project to make prediction: basic ideas--Efficient seeking
# 1. RNN based model (GRU, LSTM)-->nlp prediction调参很麻烦 或者 HMM 或者transformer-based(attention, encoder, decoder)里mask trick，但是很吃GPU。。。
# 2. Extract useful information the known words, then make prediction
#   substring找pattern频率weighted combination of n-gram model
#   assume independence找conditionally最可能出现的letter
#   Assume prefix, suffix, use greedy search to remove the unselected word