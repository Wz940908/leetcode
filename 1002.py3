class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        x=list(A[0])
        
        for item in A:
            y=[]
            for i in item:
                if i in x:
                    x.remove(i)
                    y.append(i)
            x=y
        return y
