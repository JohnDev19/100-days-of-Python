def reverse_sentence(sentence):
  # Splitting the sentence into words and punctuation...
  words = sentence.split(' ')

  # Initializing a list to store reversed words...
  reversed_words = []

  for word in words:
      # Stripping punctuation from the word...
      stripped_word = ''.join(filter(lambda x: x.isalnum(), word))

      # Reversing the stripped word...
      reversed_word = stripped_word[::-1]

      # Combining reversed word with original punctuation...
      reversed_word_with_punct = ''.join(r if not r.isalnum() else r for r, s in zip(reversed_word, word))

      # Adding reversed word to list...
      reversed_words.append(reversed_word_with_punct)

  # Joining reversed words back into a sentence...
  reversed_sentence = ' '.join(reversed_words)

  return reversed_sentence

# Example usage
original_sentence = "Hello, World! This is an example of reversing a string."
reversed_sentence = reverse_sentence(original_sentence)

print("Original Sentence:")
print(original_sentence)
print("\nReversed Sentence:")
print(reversed_sentence)
