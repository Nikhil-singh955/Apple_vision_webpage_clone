def sort_words_alphabetically(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Sort the words alphabetically
    words.sort()

    # Display the sorted words
    for word in words:
        print(word)

# Input a sentence from the user
user_sentence = input("Enter a sentence: ")

# Call the function to sort and display words
sort_words_alphabetically(user_sentence)
