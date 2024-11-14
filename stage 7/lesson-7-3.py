class WordsFinder:
    file_names = []
    def __init__(self,*files):
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for current_file_name in self.file_names:
            with open(current_file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line.lower()
                    for rc in  [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(rc, ' ')
                    line = line.strip().split(' ')
                    for word in line:
                        words.append(word)
                all_words[current_file_name] = words
        return all_words

    def find(self,word):
        result = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            word_number = 0
            for current_word in words:
                word_number += 1
                if word.lower() == current_word.lower():
                    result[file] = word_number
                    return result
            return False

    def count(self,word):
        result = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            word_count = 0
            for current_word in words:
                if word.lower() == current_word.lower():
                    word_count += 1

            result[file] = word_count
            return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
