

class TrieTree(object):
    def __init__(self):
        self.size=0
        self.childern=[None]*26
    def insert(self,word):
        node=self
        for w in word:
            index=ord(w)-97
            node.size+=1
            if node.childern[index]==None:
                node.childern[index]=TrieTree()
            node=node.childern[index]
    def search(self,word):
        node=self
        for w in word:
            index=ord(w)-97
            if node.childern[index]==None:
                return 0
            else:
                node=node.childern[index]
        return node.size


tt=TrieTree()
tt.insert('abc')
tt.insert('abbcc')
print(tt.search('ab'))
print(tt.search('a'))