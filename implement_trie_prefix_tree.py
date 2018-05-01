class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
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
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
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
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
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
