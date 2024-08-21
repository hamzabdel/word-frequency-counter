import string

def reading_input(input_file):
    with open(input_file, 'r') as f:
        data = f.read().replace('\n', '')

    translation_table = str.maketrans('', '', string.punctuation)
    cleaned_data = data.translate(translation_table)

    word_list = cleaned_data.split()

    return word_list

def word_counter(word_list): # Takes wordlist given by previous function to find frequency
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

userFile = input("Enter file name: ")

words = reading_input(userFile)
frequencies = word_counter(words)

print(frequencies)

