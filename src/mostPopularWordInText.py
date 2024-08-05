# My Code
user_text = input('Enter text here: ')

freq_dict = {}
for word in user_text.split():
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

unique_words_count = len(freq_dict)

# Список пар (слово, частота), остортированных по убыванию частоты в тексте
freq_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

print('Unique words count: ', unique_words_count)
print('Most popular word: ', freq_list[0])