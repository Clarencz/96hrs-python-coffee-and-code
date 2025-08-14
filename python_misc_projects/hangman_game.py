import random

with open ('B:\96hrs-python-coffee-and-code\python_misc_projects\wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]
allowed_guesses = 5
guesses = []
done = False


while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(f"{letter}", end='')
        else:
            print("_", end="")
    print("")
    
    guess = input(f"can you guess a letter in word {allowed_guesses} next guess...").lower()
    guesses.append(guess)
    if guess.lower() not in word.lower():
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break
        
    done = True
    for letter in word:
        if letter.lower() not in guess.lower():
            done = False
        