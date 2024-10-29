
# Step 1: Open and read the text file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:100])

# Step 2: Count the number of lines
def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

# Step 3: Count words
def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")

# Step 4: Find the most common word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

# Step 5: Calculate the average word length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# Step 6: Combine Everything into a main function
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")


# Run the analysis
analyze_text('sample.txt')



# Exercise



# 1.Counting the number of unique words in the text file.
def count_unique_words(content):
    words = content.split()
    unique_words = set(words)
    return len(unique_words)

unique_words_count = count_unique_words(content)
print (f"Number of unique words: {unique_words_count}")

# 2.longest word in the txt file
def longest_word(content):
        words = content.split()
        longest_word = max(words, key=len)
        return longest_word

longest_word_content = longest_word(content)
print(f"Longest word: {longest_word_content}")

# 3.Count the occurrences of a specific word (case-insensitive)
def count_word_occurrences(content, word):
    occurrences = content.lower().count(word.lower())
    return occurrences

word = 'global'
word_occurrences =  count_word_occurrences(content, word)
print (f"Specific word occurrences: {word_occurrences}")

# 4.Calculate the percentage of words that are longer than the average word length.
def total_percent_of_words_longer_than_average(content, word):
    words = content.split()
    #calculating the average word length
    average_length = sum(len(word) for word in words) / len(words)
    #counting the words longer than the average word length
    longer_than_average_word = sum(1 for word in words if len(word) > average_length)
    #calculating the percentage
    percentage = (longer_than_average_word / len(words)) * 100
    return percentage
    
total_percentage = total_percent_of_words_longer_than_average(content, word)
print(f"total percentage of words longer than average word length: {total_percentage}")

