import random

word_list = ['anas', 'python', 'india', 'advance']
word_list_choose = random.choice(word_list)
# print(f"Chosen word is {word_list_choose}")

display = []
for i in word_list_choose:
    display.append('_')

print(display)

life = 6
while '_' in display:
    guess_letter = input('Guess the word:\n').lower()
    num = 0
    if life > 0:
        if guess_letter in word_list_choose:
            for letter in word_list_choose:
                num += 1
                if guess_letter == letter:
                    display[num-1] = guess_letter
        else:
            life-=1
    else:
        print("You lose")
        break
    print(display)
    print(f"You have {life+1} life left")
else:
    print("You win")