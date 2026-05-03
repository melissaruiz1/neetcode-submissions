class Solution:
    # We can encode a string by adding the length of the string, followed by a hashtag
    # Use an array then convert to array to save space
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for st in strs:
            encoded.append(str(len(st)))
            encoded.append("#")
            encoded.append(st)
        return "".join(encoded)

    # We decode a string by starting at the first character, and iterating until we find
    # the #. We take all the numbers before it to get the length of the next string.

    5 # H e l l o 5 # W o r l d
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            # find the '#' delimiter
            delim = i
            while s[delim] != '#':
                delim += 1
            
            # extract the word length
            length = int(s[i:delim])
            
            # extract the word
            word_start = delim + 1
            word_end = word_start + length
            decoded.append(s[word_start:word_end])
            
            # move to the next encoded word
            i = word_end
                
        return decoded




