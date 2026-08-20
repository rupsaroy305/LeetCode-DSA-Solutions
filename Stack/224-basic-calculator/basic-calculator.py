class Solution:
    def calculate(self,s):
        st=[]
        num=0
        sign=1
        ans=0

        for c in s:
            if c.isdigit():
                num=num*10+int(c)

            elif c in '+-':
                ans+=sign*num
                num=0
                sign=1 if c=='+' else -1

            elif c=='(':
                st.append(ans)
                st.append(sign)
                ans=0
                sign=1

            elif c==')':
                ans+=sign*num
                num=0
                ans*=st.pop()
                ans+=st.pop()

        return ans+sign*num