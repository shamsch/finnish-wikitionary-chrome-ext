from wiktionaryparser import WiktionaryParser

# Create the WiktionaryParser object
wtp = WiktionaryParser()

# Load the Wiktionary page for the word "dog"
word = wtp.fetch("koira", "Finnish")

# Print the word
print(word)
