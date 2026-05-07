class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            encoded_arr.append(str(len(s)))
            encoded_arr.append("#")
            encoded_arr.append(s)
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        #    5 # H e l l o 5 # W o r l d "
        #                  i j
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
        
            str_len = int(s[i:j])
            i = j + 1 + str_len
            output.append(s[j+1: i])
        return output


        




