# форматирование строк с помощью конкатенации
import self

actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")


# python умеет подставлять пользовательские значения в строки с помощью функции .format().
# Синтаксис выглядит примерно так:
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# Форматирование строк с помощью f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

print(f"{2+3}")

# неправильно:
# Дважды считывать атрибут — это плохая практика, потому что при повторном считывании
# текст на странице может измениться, и вы получите неактуальный текст об ошибке.
assert self.catalog_link.text  == "Каталог", \
    f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"

# правильно:
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"