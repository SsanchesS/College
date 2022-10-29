def flipFirstEl(mas):
   mas = mas.split()
   mlen = len(mas)
   if mlen == 0 or mlen == 1:
      return mas
   else:
      el1 = mas[0]
      ellast = mas[-1]
      mas[0] = ellast
      mas[-1] = el1
      return mas

# print(flipFirstEl(input("Введите данные для того, чтобы перевернуть 1 и последний элемент: ")))
