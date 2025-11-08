

text = input("Enter your text: ")
words = text.lower().split()

word_freq = {}

for word in words:
    word = word.strip(".,!?;:()[]{}\"'") 
    if word:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

print("\nWord Frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
