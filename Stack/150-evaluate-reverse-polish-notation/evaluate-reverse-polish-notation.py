class Solution:
    def evalRPN(self,tokens):
        st=[]
        for x in tokens:
            if x not in '+-*/':
                st.append(int(x))
            else:
                b=st.pop()
                a=st.pop()
                if x=='+':
                    st.append(a+b)
                elif x=='-':
                    st.append(a-b)
                elif x=='*':
                    st.append(a*b)
                else:
                    st.append(int(a/b))
        return st[0]