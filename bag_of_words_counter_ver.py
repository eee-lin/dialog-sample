from collections import Counter

from tokenizer import tokenize

def calc_bow(tokenized_texts):
  counts = [Counter(tokenized_text) for tokenized_text in tokenized_texts]
    sum_counts = sum(counts, Counter())
    vocabulary = sum_counts.keys()

    bow = [[count[word] for word in vocabulary] for count in counts]

    return bow