words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "and": "و",
}

sentence = "I love python and AI"

words_list = sentence.lower().split()

translated_sentence = []
translated_count = 0
untranslated_count = 0

for word in words_list:
  if word in words:
    translated_sentence.append(words[word])
    translated_count += 1
  else:
    translated_sentence.append(f"[{word}]")
    untranslated_count += 1

print(" ".join(translated_sentence))

print(f"تعداد کلمات ترجمه شده: {translated_count}")
print(f"تعداد کلمات ترجمه نشده: {untranslated_count}")