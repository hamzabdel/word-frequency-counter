import string
import requests

# Function to read the file and remove punctuation
def reading_input(input_file):
    with open(input_file, 'r') as f:
        data = f.read().replace('\n', '')

    translation_table = str.maketrans('', '', string.punctuation)
    cleaned_data = data.translate(translation_table)

    word_list = cleaned_data.split()

    return word_list

# Function to count word frequencies
def word_counter(word_list):
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Function to find the most frequent word in the dictionary
def find_most_frequent_word(word_count):
    return max(word_count, key=word_count.get)

# Function to send the most frequent word to the Mistral model via the local API
def send_to_mistral(word):
    api_url = "http://localhost:11434/api/generate"

    # Prepare the request payload
    data = {
        "model": "mistral",
        "prompt": f"Generate a sentence using the word '{word}'"
    }

    # Send the POST request to Mistral
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        return response.json()  # Assuming the API returns a JSON response
    else:
        return f"Error: {response.status_code}, {response.text}"

# Main script execution
userFile = input("Enter file name: ")

# Read the file and get the word list
words = reading_input(userFile)

# Count the word frequencies
frequencies = word_counter(words)
print(f"Word Frequencies: {frequencies}")

# Find the most frequent word
most_frequent_word = find_most_frequent_word(frequencies)
print(f"Most Frequent Word: {most_frequent_word}")

# Send the most frequent word to the Mistral model for processing
mistral_response = send_to_mistral(most_frequent_word)
print(f"Mistral's Response: {mistral_response}")
