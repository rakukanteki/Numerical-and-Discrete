# Contraposition:
# We first converse then inverse.
# Say, if A, then B => if not B, then not A

# Examples:
# 1) If it rains, then I will not go out.


# Function for contrapositive.
def find_contrapositive(sentence):
    words = sentence.split()  # Splitting sentence.

    # Finding index for 'if' and 'then'
    if_index = then_index = -1
    for i, word in enumerate(words):
        if word.lower() == 'if':
            if_index = i
        elif word.lower() == 'then':
            then_index = i
    # Checking if both if_index and then_index are found
    if if_index != -1 and then_index != -1:
        p = " ".join(words[if_index+1 : then_index])
        q = " ".join(words[then_index+1 :])

        # Negating both the p and q
        np = " it is not the case that " + p
        nq = " it is not the case that " + q

        # Making contrapositive statement
        contrapositive_sen = f"If {np} then {nq}"

        return contrapositive_sen
    else:
        return "Please provide a sentence that conveys 'if' and 'then' in it..."


# Main function
original_sentence = "If it rains, then I will not go out"
contrapositive_sentence = find_contrapositive(original_sentence)
print("Original sentence: ", original_sentence)
print("Contrapositive: ",contrapositive_sentence)
