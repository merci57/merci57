import string

def word_frequencies(sentence):
    # Remove punctuation and normalize the sentence to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty dictionary to store word counts
    word_count = {}
    
    # Count the frequency of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Example usage
sentence = "Hello world, hello Python. Hello everyone!"
result = word_frequencies(sentence)
print(result)