# функция для замены букв на верхний регистр.
def str_up():
    word = input()
    up_word = word.upper()

    return up_word


# функция меняет первую букву на верхний регистр.
def first_letter_in_word():
    word = input()
    word_with_up_letter = word[0].upper() + word[1:]

    return word_with_up_letter


print(first_letter_in_word())
