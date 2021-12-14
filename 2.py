def palindrom():
    word = input("Введите проверяемое слово ")
    if word == word[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")


palindrom()

