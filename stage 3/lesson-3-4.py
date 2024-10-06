def single_root_words(root_word,*other_words):
    same_words = list()
    for single_word in other_words:
        if (root_word.lower() in single_word.lower()
            or single_word.lower() in root_word.lower()):
            same_words.append(single_word)
        # Можно было бы решить и через count, но такое решение выглядит более
        # громоздким и менее читаемым
        # if (single_word.lower().count(root_word.lower()) > 0
        #     or root_word.lower().count(single_word.lower()) > 0):
        #     same_words.append(single_word)
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)