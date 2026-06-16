class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            temp_encoded = str(len(s)) + '#' + s
            encoded += temp_encoded     # we could also do encoded+=str(len(s)) + '#' + s in short 
                   
        return encoded


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            length=0
            j=i
            while s[j] != "#":
                j+=1                    # finding the delimiter
            length = int(s[i:j])
            word = s[j+1:j+1+length]  # slicing the word 
            i=j+1+length            #updating the index
            result.append(word)            

        return result

