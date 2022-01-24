
from wordcloud import wordcloud

def create_wordcloud(word_dict,image_file):
  cloud = wordcloud.WordCloud()
  cloud.generate_from_frequencies(word_dict)
  cloud.to_file(image_file)

def create_word_list(file_name):
  text_file = open(file_name, "r")
  file_data = text_file.read().replace("\n", " ")
  #keep only alphanumeric data
  alphanumeric_data=""
  for chr in file_data:
    if chr.isalpha() or chr.isspace():
      alphanumeric_data=alphanumeric_data+chr
  word_list = alphanumeric_data.split(" ")
  return word_list

def create_word_dictionary(word_list):
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary

def clean_dictionary(word_dictionary,uninteresting_words):
    new_dictionary = word_dictionary.copy()

    for word in word_dictionary:
        if word.lower() in uninteresting_words:
            del new_dictionary[word]
    return new_dictionary


word_list=create_word_list("myFile.txt")
word_dictionary=create_word_dictionary(word_list)
uninteresting_words = ('a', 'the', 'to', 'if','and','or','no','of','for','is')
new_dictionary=clean_dictionary(word_dictionary,uninteresting_words)
create_wordcloud(new_dictionary,"my_file.jpg")
