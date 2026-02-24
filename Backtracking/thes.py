"""
Given a non-empty string, sentence, and a non-empty map, synonyms, where each key is a single word in the sentence, and its value is a non-empty list of synonyms, 
return all possible sentences that can be created by replacing the words in the sentence with their synonyms. 
Words without synonyms should remain unchanged. 
The input sentence only contains lowercase letters and spaces, 
while the words in synonyms only contain lowercase letters. 
The order of the generated sentences in the output does not matter.


Example 1:
sentence = "one does not simply walk into mordor"
synonyms = {
  "walk": ["stroll", "hike", "wander"],
  "simply": ["just", "merely"]
}

            one does not simply walk

                        "just"     "merely"
                                        "stroll" "hike" "wander
                "stroll"   "hike"   "wander"

        base case: reached last word in sentence
                    add partial solution to full

        check current word
        if in map:
            for syn in value:
                path.add(syn)
                visit(next)
                path.pop()

        T: O(len(syn) ^ len(words) * n)
        S: O()
             
Output: [
          "one does not just stroll into mordor",
          "one does not just hike into mordor",
          "one does not just wander into mordor",
          "one does not merely stroll into mordor",
          "one does not merely hike into mordor",
          "one does not merely wander into mordor"
        ]

Example 2:
sentence = "walk"
synonyms = {
  "walk": ["stroll"]
}
Output: ["stroll"]

                        stroll         ""

Constraints:

sentence consists of lowercase letters and spaces.
The length of sentence is at most 500 characters.
sentence contains at most 100 words.
The synonyms map contains at most 8 entries.
The length of each synonym list is at most 6.
Each word in sentence or in the synonym lists is at most 10 characters.

"""

def find_syn(sentence, syn):
    words = sentence.split()
    print(words)
    result = []
    def visit_words(word_number, path):
        if word_number == len(words):
            result.append(" ".join(path))
            return
        
        current_word = words[word_number]
        print(current_word)
        if current_word in syn:
            for match in syn[current_word]:
                path.append(match)
                visit_words(word_number + 1, path)
                path.pop()
        else:
            path.append(current_word)
            visit_words(word_number + 1, path)
            path.pop() 

    visit_words(0,[])
    return result

sentence = "one does not simply walk into mordor"
synonyms = {
  "walk": ["stroll", "hike", "wander"],
  "simply": ["just", "merely"]
}

for sen in find_syn(sentence, synonyms):
    print(sen)