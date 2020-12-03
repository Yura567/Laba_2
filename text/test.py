import collections
text = input("Введьть текст: ")
choose = input("Виберіть варіант 'a' чи 'b': ")
number = int(3)
result = text.split()
if choose == "a":
 for word in result:
    if len(word) <= number:
      result.remove(word)
      print(result)
elif choose == "b":
  result = collections.Counter(text)
  print(result)