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
    frequencies = {}
    new_text = ''
    if text is None:
        return frequencies
    if not isinstance(text, str):
        text = str(text)
    for symbol in text:
        if symbol.isalpha() or symbol == ' ':
            new_text += symbol
    new_text = new_text.lower()
    words = new_text.split()
    for key in words:
        key = key.lower()
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value + 1
        else:
            frequencies[key] = 1
    return frequencies


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
    if frequencies is None:
        frequencies = {}
        return frequencies
    for word in list(frequencies):
        if not isinstance(word, str):
            del frequencies[word]
    if not isinstance(stop_words, tuple):
        return frequencies
    for word in stop_words:
        if not isinstance(word, str):
            continue
        if frequencies.get(word) is not None:
            del frequencies[word]
    return frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    :param
    """
    if not isinstance(top_n, int):
        frequencies = ()
        return frequencies
    if top_n < 0:
        top_n = 0
    elif top_n > len(frequencies):
        top_n = len(frequencies)
    top_words = sorted(frequencies, key=lambda x: int(frequencies[x]), reverse=True)
    best = tuple(top_words[:top_n])
    return best


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    """
    Read text from file
    """
    file = open(path_to_file)
    counter = 0
    text = ''
    if file is None:
        return text
    for line in file:
        text += line
        counter += 1
        if counter == lines_limit:
            break
    file.close()
    return text


def write_to_file(path_to_file: str, content: tuple):
    """
    Creates new file
    """
    file = open(path_to_file, 'w')
    for i in content:
        file.write(i)
        file.write('\n')
    file.close()
