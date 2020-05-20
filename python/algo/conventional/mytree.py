#encoding=utf8
import numpy as np
from collections import defaultdict
# Trie
trie = {}
def make_trie(words):
    for w in words:
        t = trie
        for c in w:
            t = t.setdefault(c,{})
        t[None] = None
    return trie
def query(word):
    t = trie
    for c in word:
        if c in t:
            t = t[c]
        else:
            return False
    return None in t

make_trie(['abc','bca','bcd'])
print(trie)
print(query('hello'))
print(query('bcd'))

##############################################
