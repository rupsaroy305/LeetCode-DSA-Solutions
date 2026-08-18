class Solution:
    def simplifyPath(self,path):
        st=[]
        for x in path.split('/'):
            if x=='' or x=='.':
                continue
            if x=='..':
                if st:
                    st.pop()
            else:
                st.append(x)
        return '/'+'/'.join(st)