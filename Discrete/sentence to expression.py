ans = ""

# Function for negation
negation = ["not", "unless", "n't"]


def negation_check(test_sen, x):
    for i in range(len(negation)):
        if negation[i] in test_sen:
            return "¬ " + x

    return x


# Function for and & or logic
# sen1 = a, sen2 = b, sentence = k
def andOrLogic(a, b, k):
    global ans
    ans += negation_check(a, "x ")
    if "and" in k:
        ans += "∧"
    elif "or" in k:
        ans += "v"
    ans += negation_check(b, " y")

    print(ans)


# Function for 'if'.
def check_if(sentence):
    global ans

    # You can't ride the roller coaster if you are under 4 feet tall
    # unless you are older than 16 years old
    if "if" and "unless" in sentence:
        sen1, sen2 = map(str, sentence.split("if"))
        sen3, sen4 = map(str, sen2.split("unless"))
        ans += "( " + negation_check(sen3, "r")
        ans += " ∧ " + negation_check(sen4, "s") + ")"
        ans += " → " + negation_check(sen1, "q")

    # If you give respect, you earn respect.
    # If you learn how to code, then you will find a good job.
    elif "if" in sentence[0:2]:
        if "then" in sentence:
            sen1, sen2 = map(str, sentence.split("then"))
        elif "," in sentence:
            sen1, sen2 = map(str, sentence.split(","))
        ans += negation_check(sen1, "x")
        ans += " → "
        ans += negation_check(sen2, "y")

    # You will earn money if you work hard.
    elif "if" in sentence:
        sen1, sen2 = map(str, sentence.split("if"))
        ans += negation_check(sen2, "y")
        ans += " → "
        ans += negation_check(sen1, "x")

    print(ans)


# Splitting a sentence
def SplitSentence(sentence):
    sentence = sentence.lower()
    if "and" in sentence:
        sen1, sen2 = map(str, sentence.split("and"))
        # If 'and' found then send it o andOrLogic function
        andOrLogic(sen1, sen2, sentence)
    elif "or" in sentence:
        sen1, sen2 = map(str, sentence.split("or"))
        # If 'or' found then send it o andOrLogic function
        andOrLogic(sen1, sen2, sentence)
    elif "if" in sentence:
        # If 'if' found then send it o check_if function
        check_if(sentence)


# Main function
SplitSentence(input("Enter sentence: "))



