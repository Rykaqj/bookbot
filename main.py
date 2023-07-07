with open("books/frankenstein.txt") as f:
   file_contents = f.read()

def count_words(contents):
   words = contents.split()
   return len(words)

words_count = count_words(file_contents)

print(words_count)

def words_dict(contents):
   words = contents.lower().split()
   concat_strings = ''.join(words)
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   words_list = []

   for char in alphabet:
      counted = get_count(char, concat_strings)
      words_list.append({"char" : char, "count" : counted})
   return words_list

def get_count(char, string):
   count = 0
   for letter in string:
         if char == letter:
            count += 1
   return count

file_dictionary = words_dict(file_contents)
sorted_descending_letters = sorted(file_dictionary, key=lambda x: x["count"], reverse=True)

print("--- Begin report of books/frankenstien.txt")
print(f"{words_count} words found in the document")
print()
print()
for letter in sorted_descending_letters:
   print(f"The '{letter['char']}' was found {letter['count']} times")