# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the
# .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# 1. Write a function that can censor a specific word or phrase from a body of text, and then return the text.
# Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one.
# Mr. Cloudy doesn’t care how you censor it, he just wants it done.

def censor_word(text, word):
    block = ""
    for n in range(0, len(word)):
        if word[n] == " ":
            block += " "
        else:
            block += "*"
    return text.replace(word, block)

# print(censor_word(email_one, "learning algorithm"))


# 2. Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases,
# and then return the text.
# Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.

proprietary_terms = ["personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her", "she"]

def censor_list(text, list_of_words):
    for word in list_of_words:
        print("Now replacing {0}".format(word))
        block = ""
        for n in range(0, len(word)):
            if word[n] == " ":
                block += " "
            else:
                block += "*"
#        text = text.replace(word, block)
        text_lowered = text.lower()
        word_lowered = word.lower()
        context = [idx for idx, char in enumerate(text_lowered) if char == word_lowered[0]]
        for i in context:
            capture = text_lowered[i : i+len(word_lowered)]
#            print(capture)
            if capture == word_lowered:# and text[i-1] == " " and text[i+len(word)+1] == " ":
#                char_before = text[i-1]
#                print(char_before)
#                if char_before == " " or char_before == "\n":
#                    char_after = text[i+len(word)]
#                    print(char_after)
#                    if char_after == " " or char_after == "\n" or char_after == "s":
                capture = text[i : i+len(word)]
#                        print(capture)
#                        print("Char_before : '{0}' and char_after : '{1}'".format(char_before, char_after))
                text = text.replace(capture, block)
    return text

print(censor_list(email_two, proprietary_terms))

# 3. The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think.
# He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and
# remove unnecessary instances of ‘negative words.’”
# Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice,
# as well as censoring everything from the list from the previous step as well and use it to censor email_three.

# negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]



# 4. This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you,
# “our company would be ruined! Censor it! Censor it all!”
# Write a function that censors not only all of the words from the negative_words and proprietary_terms lists,
# but also censor any words in email_four that come before AND after a term from those two lists.



# 5. Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.
# Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:

#    Handle upper and lowercase letters.
#    Handle punctuation.
#    Censor words while preserving their length.

