# Конструкция 'Name' in s возвращает просто True или False
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

 # find() возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')