import string
import os

#! Answer for Q1
def count_words(filename):
    '''
    Input -> String or file path to ‘sample.txt’
    Output -> Words and their count

    Takes filepath or string as input,
        if filepath, then get words and count from the file of the path,
        if not filepath and valid string, then get words and count from the input string.
    '''
    wordcount = {}
    if filename is None:
        return wordcount

    if type(filename) != str:
        raise TypeError

    if os.path.exists(filename):
        # If the input is the filepath
        with open(filename, 'r') as file:
            # Open the file in read mode, then use the lower() method to transform all text in the string to lowercase, because the "Word" = "word"
            text = file.read().lower()

            # Use translate() method to remove all punctuation characters from the string.
    else:
        # If the input is test string
        text = filename.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))
    words = sorted(text.split())

    # Takes each word in the text and update the dictionary to store words and counts
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount



# A method to output result to a text file.
def write_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write(f"{key}: {value}\n")


#! Answer for Question 3
def find_most_common_word(wordcount):
    '''
    Loop through all the words and update the max count. As we are using dictionary and each count,
    there are no algorithms that are faster than this because, to get max count we need at least one loop.
    '''
    max_count = 0
    most_common_word = ''
    for word, count in wordcount.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    return (most_common_word, max_count)


def prepend_text_to_file(filename, text):
    '''
    To display most common word and count at the top of the text file,
    Move the file pointer back to the beginning of the file using the seek() method with an offset of 0.
    and write the new text followed by the old text to the file using the write() method.
    '''
    with open(filename, 'r+') as file:
        old_text = file.read()
        file.seek(0)
        file.write(text + old_text)



if __name__ == '__main__':
    filename = 'sample/sample.txt'
    wordcount = count_words(filename)
    write_dict_to_file(wordcount, 'sample/output.txt')

    most_common_word, max_count = find_most_common_word(wordcount)
    pre_text = f'The most common word: {most_common_word}, count: {max_count}\n'
    prepend_text_to_file('sample/output.txt', pre_text)