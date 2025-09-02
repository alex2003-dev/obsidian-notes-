# Simple text analyzer
sentence = input("Type a sentence: ")
sentence = sentence.strip()

if sentence == "":
    print("Ты ничего не написал.")
else:
    # Calculate sentence length
    length = len(sentence)

    # Split into words
    words = sentence.split()
    word_count = len(words)

    # Get first and last character
    first_letter = sentence[0]
    last_letter = sentence[-1]

    # Print banner
    print("+" + "-" * 40 + "+")
    print("| Sentence: " + sentence)
    print("| Length:", length)
    print("| Words:", word_count)
    print("| First letter:", first_letter)
    print("| Last letter:", last_letter)
    print("+" + "-" * 40 + "+")
