"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''

class WordStorage:

    def __init__(self):
        self.storage = {}
        self.ID = 0

        # word1 key1
        # word2 key2
    def put(self, word: str) -> int:

        if word not in self.storage and isinstance(word, str):
            self.storage[word] = self.ID
            self.ID += 1
            return self.ID - 1
        else:
            return self.storage[word]


    def get_id_of(self, word: str):
        if isinstance(word, str):
            return self.storage.get(word)
        else:
            return None



    def get_original_by(self, id: int):
        for k, v in self.storage.items():
            if v == id:
                return k
        return None

    def from_corpus(self, corpus: tuple):
        for sentence in corpus:
            for word in sentence:
                self.put(word)


class NGramTrie:
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    cipher = []
    for sentence in corpus:
        pre_list = []
        for word in sentence:
            word = storage_instance.get_id_of(word)
            pre_list.append(word)
        cipher.append(pre_list)

    return cipher


def split_by_sentence(text: str) -> list:
    if not isinstance(text, str):
        return []
    signs = [',', '-', '—', '«', '»', ':', ';', '"', "'","#","$", '(', ')', '&']
    ending_signs = ['.','!','?']
    short_words = ['St.','Mr.','Mrs.','Ms.','Dr.']
    text = text.replace('\n', ' ')
    for i in signs:
        text = text.replace(i, '')
    while '  ' in text:
        text = text.replace('  ',' ')
    for el in short_words :
        text = text.replace(el, el.replace('.', ''))
    sentences = []
    cut_start_pos = 0
    n_all_elements = len(text)
    for n_elem, element in enumerate(text):
        if n_elem == n_all_elements - 1:
            sentence = text[cut_start_pos:n_elem]
            sentences.append(sentence)
            break
        if element in ending_signs:
            if text[n_elem+1] == ' ':
                if text[n_elem+2].isupper():
                    sentence = text[cut_start_pos:n_elem]
                    sentences.append(sentence)
                    cut_start_pos = n_elem + 2
    # list.insert(pos, x)
    final_sentences = []
    symbol = '</s>'
    start_symbol = '<s>'
    for sentence in sentences:
        new_sentence = sentence.split()
        new_sentence.append(symbol)
        new_sentence.insert(0, start_symbol)
        final_sentences.append(new_sentence)

    return final_sentences


if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
