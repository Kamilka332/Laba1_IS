values = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
          'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
          'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
          'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В',
          'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К',
          'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
          'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
          'Э', 'Ю', 'Я', ' ', '.', ':', '!', '?', ',']
print("Введите фразу с клавиатуры:", end="")
if input() == print(values):
    print("Вы ввели неправильные символы, попробуйте еще раз!")
phrase, number = input(), []
print("Зашифрованная фраза: ", end="")
for p in phrase:
    for i in range(len(values)):
        if p in values[i]:
            print(str(i + 1) + str(values[i].index(p) + 1), end=" ")
            number.append([i + 1, values[i].index(p) + 1])
print()

print("Расшифрованная фраза: ", end="")
for n in number:
    print(values[n[0] - 1][n[1] - 1], end="")
