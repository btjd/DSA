from pprint import pprint

class Trie(object):
    def __init__(self, words):
        def make_trie(words):
            root = dict()
            for word in words:
                current_dict = root
                for letter in word:
                    current_dict = current_dict.setdefault(letter, {})
                current_dict['__end__'] = '__end__'
            return root
        self.trie = make_trie(words)
       
    def __repr__(self):
        return str(pprint(self.trie))

    def in_trie(self, word):
        current_dict = self.trie
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        else:
            if '__end__' in current_dict:
                return True
            else:
                return False

if __name__ == "__main__":
    t = Trie(['foo', 'bar', 'baz', 'barz'])
    pprint(t)
    print t.in_trie('baz')
    print t.in_trie('bad')