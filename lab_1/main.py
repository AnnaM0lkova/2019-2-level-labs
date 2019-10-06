"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


test_text = """
I have no idea what backward sweep of memory had brought the matter fresh to his mind , or what freak had caused him to desire that I should recount it; but I hasten, before another cancelling telegram may arrive, to hunt out the notes which give me the exact details of the case and to lay the narrative before my readers.
It was, then, in the spring of the year 1897 that Holmes’s iron constitution showed some symptoms of giving way in the face of constant hard work of a most exacting kind, aggravated, perhaps, by occasional indiscretions of his own. In March of that year Dr. Moore Agar, of Harley Street, whose dramatic introduction to Holmes I may some day recount, gave positive injunctions that the famous private agent lay aside all his cases and surrender himself to complete rest if he wished to avert an absolute breakdown. The state of his health was not a matter in which he himself took the faintest interest, for his mental detachment was absolute, but he was induced at last, on the threat of being permanently disqualified from work, to give himself a complete change of scene and air. Thus it was that in the early spring of that year we found ourselves together in a small cottage near Poldhu Bay, at the further extremity of the Cornish peninsula.
It was a singular spot, and one peculiarly well suited to the grim humour of my patient. From the windows of our little whitewashed house, which stood high upon a grassy headland, we looked down upon the whole sinister semicircle of Mounts Bay, that old death trap of sailing vessels, with its fringe of black cliffs and surge-swept reefs on which innumerable seamen have met their end. With a northerly breeze it lies placid and sheltered, inviting the storm-tossed craft to tack into it for rest and protection.
Then come the sudden swirl round of the wind, the blustering gale from the south-west, the dragging anchor, the lee shore, and the last battle in the creaming breakers. 
"""

stop_words = ('a', 'the')

def read_from_file(path_to_file: str, lines_limit: int) -> str:
    """

    :param path_to_file: <str> путь к файлу с пометкой("чтение")
    :param lines_limit: <int> максиманьное число строк,которое берется из файла;ввод изначально
    :return:
    """
    try:
        file = open(path_to_file, 'r')
    except Exception as error:
        print('Ошибка в read_from_file: ', error)
        return ''

    result_text = ''
    n_line = 1
    for line in file:
        if n_line > lines_limit:
            return result_text
        else:
            result_text += line
            n_line += 1


def calculate_frequences(text: str) -> dict:

    """

        :param text: <str> некоторое кол-во строк,с которым будут проведены операции
        :return: <dict> функция возвращает изменненый текст в виде словаря
        """
    signs = ['.', ',', '?', '!', '-', '—', '«', '«', ':', ';', '"', "'"]
    text_mono = text.lower()
    for sign in signs:
        text_mono = text_mono.replace(sign, '')
    text_mono.strip()

    word_list = text_mono.split()

    result_dict = {}
    for word in word_list:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """

        :param frequencies: <dict> частота слов в тексте в виде словаря
        :param stop_words: <tuple> запрещенные слова
        :return: <dict> очищенный частотный словарь
        """
    for stop_word in stop_words:
        if stop_word in frequencies.keys():
            frequencies.pop(stop_word)
    return frequencies



def get_top_n(frequencies: dict, top_n: int) -> tuple:
    if top_n > len(frequencies):
        print('В словаре меньше {} элементов'.format(top_n))
        return ()

    top_n_words = []
    max_freq = 0
    max_value = {}

    for i in range(top_n):
        for item in frequencies.items():
            if item[1] > max_freq:
                max_freq = item[1]
                max_value = item
        top_n_words.append(max_value)
        frequencies.pop(max_value[0])
        max_freq = 0
        max_value = ()

    return tuple(top_n_words)


if __name__ == '__main__':

    text = read_from_file(path_to_file='data.txt', lines_limit=4)
    print(text)
    res = calculate_frequences(text=text)
    print(res)
    res = filter_stop_words(res, stop_words=stop_words)
    print(res)
    res = get_top_n(res, top_n = 5)
    print(res)





