# SE T38 - Semantic Similarity (NLP)
# Compulsory Task 1

import spacy
from tabulate import tabulate

nlp = spacy.load('en_core_web_md')

# Example 1 from the PDF notes
# Similarity with spacy

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("\n=== Similarity with spacy (md) ===\n")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Notes on similarities
# 1. "cat" and "monkey" was most similar
# - this may be due to both being animals the the other word is a fruit.
# 2. "cat" and "banana" was least similar, while "monkey" and "banana" are more similar
# - So we can assume that the model understands that a monkey eats a banana but a cat does not.

# Completing bullet point 2 of task
# START ===============================================
# initialise the similarity score for word pairs
sim_score = []
# initialise vector of words for comparison
tokens = nlp("cat monkey chimpanzee ape dog fish mouse tiger lion pet feline tail whiskers purr tail kitty mog tom garfield kitten tomcat cataclysm banana milk queen tree fat mat bat hat black white")
print("\n=== CT1: Example of your own similarity with spacy (md) ===\n")

# loop through the vector to compare each word against all the words in the the vector to get a similarity score, but avoid duplicate comparisons by limiting the inner loop
for token1 in range(1): #range(len(tokens)):
    for token2 in range(token1+1, len(tokens)):
        sim_score.append(
            [tokens[token1].text, 
            tokens[token2].text, 
            tokens[token1].similarity(tokens[token2])
            ])

# Create a pretty table to display the similarity score
# Initialise header of table
header = ['Word 1', 'Word 2', 'Similarity']

# create table
table = tabulate(sim_score, headers = header, tablefmt = 'mixed_grid')

print(table)

# COMMENTS ===============================================
# 1. Similarity scores are symmetric, that is A ~ B = B ~ A
# 2. cat has a higher similarity to chimpanzee than an ape even though a chimpanzee is a type of ape. This seems to suggest that spacy picks up characteristics within an animal type to score similarity
# 3. A similarity of 1 was given between 'cat' and 'dog', but not between 'cat and 'fish'.
# 4. Similarity scores are not transitive. (cat, fish) = 0.2928 and (fish, dog) = 0.2928, but (cat, dog) = 1. Interestingly (cat, fish) = (dog, fish), but (cat, monkey) = 0.394524, (monkey, fish) = 0.297627 and (cat, fish) = 0.2928, so if a score of 1 is present there seems to be some semi-transitive property present.
# 5. (cat, kitten) = 1, but (cat, feline) = 0.363244 and (cat, tomcat) = 0.0859843. Scoring age high but gender low.
# 6. (cat, tiger) = (cat, lion) = 0.310771 which is lower than (cat, chimpanzee) = 0.48249, indicating cat genealogy is not considered high.
# 7. Surprisingly, (cat, mouse) = 0.185806 < (cat, fish) = 0.2928 < (cat, dog) = 1.
# 8. (cat, pet) = 1
# 9. Physical features of a cat are not scored high nor are similar sounding words.

# FINISH ===============================================

# Example 2 from the PDF notes
# Working with vectors


tokens = nlp('cat apple monkey banana ')

print("\n=== Working with vectors (md) ===\n")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Example 3 from the PDF notes
# Working with sentences

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
'Hello, there is my car',
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print("\n=== Working with sentences (md) ===\n")
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
