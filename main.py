def main():
  while True:
    answer_bruh = input("Пойдем пить пиво? ")
    if ['да', 'ты еще спрашиваешь', 'конечно'] in anwser_bruh.lower():
      print("Успех!!!")
      break
    elif ['нет', 'не', 'я лох'] in anwser_bruh.lower():
      print("минус вайб")
      break
    else:
      print("Я глупый повтори пж")

if __name__ == '__main__':
  main()
