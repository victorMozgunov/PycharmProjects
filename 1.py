import sys
def get_word():
    max_attempts = 3
    global word
    for attempt in range(max_attempts):
        word = input("Введите слово: ")
        if word.isalpha():
            return word
        else:
            print("Повторить ввод!")
    else:
        print("Выполнено %s неудачных попыток. Выход из программы!" % max_attempts)
        sys.exit()

def is_palindrome(word):
    global what_is
    word_lower = word.lower()
    what_is = word_lower==word_lower[::-1]
    return what_is

def create_message(word, what_is):
    if what_is:
        prefix = ""
    else:
        prefix = "не "
    return "Слово %s — %sпалиндром" % (word, prefix)

def check_palindrome():
    get_word()
    is_palindrome(word)
    msg = create_message(word, what_is)
    return msg

print(check_palindrome())