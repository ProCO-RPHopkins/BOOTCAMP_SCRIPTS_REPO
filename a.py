def strip_words(words):
    split_words = words.split()
    new_words = []

    # I could define the suffix as well: suffix = "ing"
    # If there was more than one suffix, I would have to run through if, elif, elses

    for word in split_words:
        if word.endswith("ing"):
            new_word = word[:len("ing")]
            new_words.append(new_word)
        else:
            new_words.append(new_word)
    result = " ".join(new_words)
    return result
input_words = "having toying running"
output = strip_words(input_words)
print(f"Modified words: {output}")


def strip_words(words):
    split_words = words.split()
    new_words = []
    
    for word in split_words:
        if word.endswith("ing"):
            new_word = word[:len("ing")]
            new_words.append(new_word)

    result = " ".join(new_words)
    return result

input_words = "having trying flying"
output = strip_words(input_words)
print(f"The new words are: {output}")


