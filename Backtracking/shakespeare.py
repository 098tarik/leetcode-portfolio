"""
Inspired by Shakespeare's iconic line,
 you decide to write a function, shakespearify(),
   which takes in a string, sentence, 
   consisting of letters and spaces. 
   For each word in the string, 
   the function chooses if it 
   should "be" or "not be" included in the sentence, 
   returning all possible outcomes. The order of the output strings does not matter.


Example 1: sentence = "I love dogs"
Output: [
         "",
         "I",
         "love",
         "dogs",
         "I love",
         "I dogs",
         "love dogs",
         "I love dogs"
        ]

Example 2: sentence = "hello"
Output: ["", "hello"]

Example 3: sentence = ""
Output: [""]
Constraints:

The sentence consists of lowercase letters and spaces.
The sentence has at most 12 words and at most 100 characters.

                                I      ""
                                            ""      love    

                        love       ""       " "     ""     dogs
                                    "I"                 "love" "love dogs
                    dogs      " "
                            "I Love"

            "I love dogs"

T:O(2^n) where n = len(words)
T:O(n) where n = len(words)

"""


def shakespearify(sentence):
    result = []
    words = sentence.split()

    def visit(word_number, path):
        if word_number == len(words):
            result.append(" ".join(path))
            return
        
        path.append(words[word_number])
        visit(word_number + 1, path)
        path.pop()
        visit(word_number + 1, path)

    visit(0,[])
    return result

sentence = "I love dogs"
print(shakespearify(sentence))