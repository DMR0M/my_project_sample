import re


class Words:
    def __init__(self, text):
        self.text = text
        self.word_list = ['The', 'one', 'perfectly', 'divine']
        self.w_list_copy = [w for w in self.word_list]
        self.locs = list(set([(m.start(), m.end()) for word in self.word_list
                              for m in re.finditer(word, text)]))

    def locations(self):
        return self.locs


if __name__ == '__main__':
    txt = "The oneperfectly divine thing, the oneglimpse of God's paradisegiven" \
          "on earth, is to fight a losingbattle - and notlose it."

    w = Words(txt)
    print(w.locs)
