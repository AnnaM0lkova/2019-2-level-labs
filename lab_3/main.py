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
    # NGramTrie(3)
    def __init__(self, n, n_words):
        self.size = n
        self.gram_freqencies = {}
        self.gram_log_probabilities = {}
        self.max_id = n_words

    def fill_from_sentence(self, sentence: tuple) -> str:
        """

        :param sentence:
        :return:

        ('the', 'weather', 'was', 'fine', 'yesterday')
        f()

        """
        error = 'ERROR'

        if sentence is not None and isinstance(sentence, tuple):
            if len(sentence) < self.size:
                return error

            start_position = 0
            end_position = self.size

            while end_position <= len(sentence):
                tri_gramm = sentence[start_position:end_position]

                if tri_gramm in self.gram_freqencies:
                    self.gram_freqencies[tri_gramm] += 1
                else:
                    self.gram_freqencies[tri_gramm] = 1
                start_position += 1
                end_position += 1

            return self.gram_freqencies

    def calculate_log_probabilities(self):
        for gram in self.gram_freqencies:
            all_grams = 0
            for other_gram in self.gram_freqencies:
                if gram[:-1] == other_gram[:-1]:
                    all_grams += self.gram_freqencies[other_gram]
            self.gram_log_probabilities[gram] = math.log(self.gram_freqencies[gram] / all_grams)
        return self.gram_log_probabilities

    '''
        action()
        mass = []

        new_mass = []
        for m in mass:
            if m.isalpha():
                new_m = action(m)
                new_mass.append(new_m)

        new_mass = [action(m) for m in mass if m.isalpha()]


    '''
    def predict_next_sentence(self, prefix: tuple) -> list:
        if isinstance(prefix, tuple) and len(prefix) == self.size - 1:
            prefix = list(prefix)
            pop_prob = [self.gram_log_probabilities[gram] for gram in self.gram_log_probabilities if
                        list(gram)[:-1] == prefix]
            print(pop_prob)
            if len(pop_prob) != 0:
                pop_prob = max(pop_prob)
                for k, v in self.gram_log_probabilities.items():
                    if pop_prob == v and list(k)[:-1] == prefix:
                        prefix.append(k[-1])
            return prefix
        return []


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
    if __name__ == '__main__':
        with open('not_so_big_reference_text.txt', 'r') as f:
            REFERENCE_TEXT = f.read()

        WS = WordStorage()

        result = split_by_sentence(text=REFERENCE_TEXT)
        WS.from_corpus(tuple(result))
        NGR = NGramTrie(3, WS.ID)

        # print(WS.storage)
        # print(WS.get_id_of('The'))
        # print(WS.get_original_by(6))
        encoded_sentences = encode(WS, result)

        print(WS.get_id_of('i'))
        for el in encoded_sentences:
            res = NGR.fill_from_sentence(tuple(el))
        #print(res)
        print(len(NGR.gram_freqencies))
        res = NGR.calculate_log_probabilities()
        print(res)

        sentence = NGR.predict_next_sentence((0, 1))
        print()
        print(sentence)
        for id_of_word in sentence:
            print(WS.get_original_by(id_of_word), end=' ')