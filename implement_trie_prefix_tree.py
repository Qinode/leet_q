class Trie:
    def __init__(self):
        self.val = None
        self.children = {}

    def insert(self, word):
        if word is None or word == '':
            return
        else:
            node = self
            length = 0
            while length < len(word):
                if word[length] in node.children:
                    node = node.children[word[length]]
                    length += 1
                else:
                    break

            while length < len(word):
                node.children[word[length]] = Trie()
                node = node.children[word[length]]
                length += 1

            node.val = word

    def search(self, word):
        if word is None or word == '':
            return True
        else:
            length = 0
            node = self
            while length < len(word):
                if word[length] in node.children:
                    node = node.children[word[length]]
                    length += 1
                else:
                    break

            if length != len(word):
                return False
            else:
                return node.val == word

    def startsWith(self, prefix):
        if prefix is None or prefix == '':
            return True
        else:
            node = self
            length = 0
            while length < len(prefix):
                if prefix[length] in node.children:
                    node = node.children[prefix[length]]
                    length += 1
                else:
                    break
            return length == len(prefix)
