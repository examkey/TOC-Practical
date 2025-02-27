#word Tokenization of letters
word ="word"
char_tokens=list(word)
print(char_tokens)

#Sentence Tokenization of letters
sentence ="Hello,world!"
import string
cleaned_sentence="".join(char for char in sentence if char not in string.punctuation  and char!=' ')
char_tokens=list(cleaned_sentence)
print(char_tokens)

#Paragraph tokenization of words
paragraph="This is a simple paragraph.it contains several eorrs."
word_tokens=paragraph.split()
print (word_tokens)

#paragraph tokenization of senteance
paragraph="This is simple a paragraph. it contains several words."
word_tokens=paragraph.split(".")
print(word_tokens)
