def count_words(text):
    words = text.split()
    n =0
    for i in words:
        n += 1
    return n

def average_word_length(text): 
    letters = 0
    for i in text.split():
        for n in i:
            letters += 1
    avarage = letters/count_words(text)
    return avarage
