import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if not texts or not isinstance(texts, list):
        return []
    clean_corpus = []
    signs = [',', '-', '—', '«', '»', ':', ';', '"', "'", "#", "$", '(', ')', '&']
    for one_text in texts:
        if one_text and isinstance(one_text, str):
            one_text = one_text.replace('?',".")
            one_text = one_text.replace('!',".")
            for i in signs:
                one_text = one_text.replace(i," ")
            while "  " in one_text:
                one_text = one_text.replace("  "," ")
            while '<\n>' in one_text:
                one_text = one_text.replace("<\n/>", " ")
            while '<br />' in one_text:
                one_text = one_text.replace("<br />", " ")
            clean_token_text = []
            words = one_text.split(" ")
            for word in words:
                new_word = ""
                if not word.isalpha():
                    for i in word.lower():
                        if i.isalpha():
                            new_word += i
                    if new_word:
                        clean_token_text.append(new_word.lower())
                else:
                    clean_token_text.append(word.lower())
            clean_corpus += [clean_token_text]
    return clean_corpus
    pass


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        pass

    def calculate_tf(self):
        pass

    def calculate_idf(self):
        pass

    def calculate(self):
        pass

    def report_on(self, word, document_index):
        pass


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    print(test_texts)
    '''
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
    '''
