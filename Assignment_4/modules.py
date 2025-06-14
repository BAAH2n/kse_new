import random

def choose_the_word (words):
    x = random.random()
    y = x * len(words)
    z = int(y)
    secret_word = words[z]
    return secret_word

def check_word (secret_word, length_secret, guess):
    result=[]; i=0
    while i < length_secret:
        letter = guess[i]
        if letter==secret_word[i]:
            result.append(f"[{letter.upper()}]")
        elif letter in secret_word:
            result.append(f"({letter})")
        else:
            result.append(f" {letter} ")
        i+=1
    return result