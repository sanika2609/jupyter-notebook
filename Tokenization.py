# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required resources
nltk.download('punkt')

# Example text
text = "Hello! This is an example of tokenization. Tokenization breaks text into words or sentences."

# Tokenize the text into words
word_tokens = word_tokenize(text)
print("Word Tokens:", word_tokens)

# Tokenize the text into sentences
sentence_tokens = sent_tokenize(text)
print("Sentence Tokens:", sentence_tokens)
