class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Store each character in a key, value pair dictionary
        char_dict = dict()
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] = char_dict[c] + 1

        lng_palin_len = 0
        have_odd_num_char = False
        # print(char_dict)
        for val in char_dict.values():
            # Even character is avalible for making palindrome
            if val % 2 == 0:
                lng_palin_len = lng_palin_len + val
                
            # (Odd number character - 1) is avalible for making palindrome
            else:
                if not have_odd_num_char:
                    have_odd_num_char = True
                lng_palin_len =  lng_palin_len + (val - 1)

        # We can put one character in the middle of palindrome string
        if have_odd_num_char:
            lng_palin_len = lng_palin_len + 1

        print(lng_palin_len)
        return lng_palin_len

solution = Solution()
solution.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
