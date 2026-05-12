text ="i love deep learning and natural language processing"
# split the text into words
words = text.split()

# build a vocabulary of unique words
vocab = set(words)

# create a mapping of words to indices
words_to_indices = {word: index for index, word in enumerate(vocab)}
# create a mapping of indices to words
indices_to_words = {index: word for index, word in enumerate(vocab)}

window_size = 1 
# create training data
training_data = []
for i in range(len(words)):
    target_word = words[i]
    context_words = []
    
    # get the context words within the window size
    for j in range(-window_size, window_size + 1):
        if j != 0 and 0 <= i + j < len(words):
            context_words.append(words[i + j])
    
    # add the target word and its context words to the training data
    for context_word in context_words:
        training_data.append((target_word, context_word))


        context_words.append((words_to_indices[target_word],
                      words_to_indices[context_word]))
        


impoer tourch 