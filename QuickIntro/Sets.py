def extract_unique_words(paragraph):
    words = paragraph.lower().split()
    unique_words = set(words)
    return unique_words


def find_common_words(set1, set2):
    return set1.intersection(set2)


def find_unique_words(set1, set2):
    return set1.difference(set2)


def display_results(common, unique1, unique2):
    print("Comparison Results:")
    print("\nCommon Words:")
    for word in common:
        print(word)

    print("\nUnique Words in Paragraph 1:")
    for word in unique1:
        print(word)

    print("\nUnique Words in Paragraph 2:")
    for word in unique2:
        print(word)


paragraph1 = "Python is a great programming language. Python is popular and powerful."
paragraph2 = "Python is widely used in data science. Data science is an exciting field."


unique_words1 = extract_unique_words(paragraph1)
unique_words2 = extract_unique_words(paragraph2)


common_words = find_common_words(unique_words1, unique_words2)
unique_to_paragraph1 = find_unique_words(unique_words1, unique_words2)
unique_to_paragraph2 = find_unique_words(unique_words2, unique_words1)


display_results(common_words, unique_to_paragraph1, unique_to_paragraph2)
