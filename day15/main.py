def word_count_tool(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    words = text.split()
    total_words = len(words)
    unique_words = len(set(words))
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")

    print("\nWord frequency:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")


if __name__ == "__main__":
    file_name = input("Enter the file name or path: ")
    word_count_tool(file_name)
