word_guess = input("Give us a starting word: ").lower()
blank_fill = list(word_guess)
my_list = ['_' for _ in blank_fill]

lives = len(word_guess)  # or set as len(word_guess) for dynamic difficulty

while '_' in my_list and lives > 0:
    player_guess = input("Guess a letter to complete the word: ").lower()

    if player_guess in blank_fill:
        # Reveal all occurrences
        for i in range(len(blank_fill)):
            if blank_fill[i] == player_guess:
                my_list[i] = player_guess
        print("✅ Correct:", ' '.join(my_list))
    else:
        lives -= 1
        print(f"❌ Wrong! You have {lives} lives left.")
        print("Current state:", ' '.join(my_list))

if '_' not in my_list:
    print(f"\n🎉 You won! The word was: {word_guess}")
else:
    print(f"\n💀 Game over! The word was: {word_guess}")
