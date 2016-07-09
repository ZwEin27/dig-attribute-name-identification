# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-09 10:58:11
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-09 11:14:27

import pygtrie

def load_trie_obj(words):
    trie_obj = pygtrie.CharTrie()
    for word in words:
        trie_obj[word] = word
    return trie_obj

def match_names(word, trie_obj):
    if trie_obj.has_key(word):
        return True
    return False

if __name__ == '__main__':

    test_word = 'hello world'

    words = ['hello', 'world', 'hello world']
    trie_obj = load_trie_obj(words)
    print match_names(test_word, trie_obj)