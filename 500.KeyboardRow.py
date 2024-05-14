# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

def findWords(words):
    rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

    result = []
    for word in words: 
        wordL = word.lower()
        for row in rows: 
            if all(char in row for char in wordL):  # Checks if all the characters in word are present in any of the row... if all of them are persent in one row we break the nested loop.
                result.append(word)
                break

    return result

words = ["Hello","Alaska","Dad","Peace"]
ans = findWords(words)

print(ans)


## 97.14%

