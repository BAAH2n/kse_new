import modules as m

tries = 6
words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
secret_word = m.choose_the_word(words)
lenght_secret = len(secret_word)


print(f"""Welcome to Wordle!"
Guess the {lenght_secret}-letter word. You have {tries} tries.""")

while tries!=0:
    guess = input(f"Attempt {(7 - tries)}/6 – Enter guess: ").lower()

    if len(guess)!= lenght_secret:
        print(f"Wrong length. Expected {lenght_secret}")
        continue
    elif guess == secret_word:
        print("You win!!!")
        break
    else:
        result = m.check_word (secret_word, lenght_secret, guess)
    
    print("Result:", ' '.join(result))
    tries = tries - 1
else:
    print(f"You lose! The word was: {secret_word}")