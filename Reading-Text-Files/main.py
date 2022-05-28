# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, encoding="utf8") as f:
        returned_lines = f.readlines()

        strings_and_occurrences(returned_lines)
        print(returned_lines)

    return returned_lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}


def strings_and_occurrences(strings):
    counts = dict()
    words = strings.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        print(counts)
        return counts


count_words()
