class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."]

        words_in_morse = list()
        for word in words:
            word_in_morse = ''
            for letter in word:
                # Convert letter into morse representation
                letter_in_morse = morse_code[ ord(letter) - ord('a') ]
                word_in_morse = word_in_morse + letter_in_morse

            # Check if already in the list
            if word_in_morse not in words_in_morse:
                words_in_morse.append(word_in_morse)
        # print(words_in_morse, len(words_in_morse))
        return(len(words_in_morse))

solution = Solution()
solution.uniqueMorseRepresentations(['gary', 'gary', 'peter'])
