"""
PROBLEM LINK:https://www.hackerrank.com/challenges/no-prefix-set/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

# !/bin/python3

import os
import sys


#
# Complete the contacts function below.
#


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def addName(self, word):
        current_node = self.root
        #print(word)
        length = len(word)
        check = False
        checkforEqual = True
        for letter in range(0, length):
                #print(word[letter], current_node.is_end_of_word, current_node.letter)

            if word[letter] not in current_node.children:
                checkforEqual = False
                current_node.children[word[letter]] = TrieNode(word[letter])
            #print(current_node.children, word[letter], current_node.is_end_of_word, current_node.letter)
            if current_node.is_end_of_word:
                check = True
                break
            #if letter != length - 1:
            current_node = current_node.children[word[letter]]
        #print(arr)
        current_node.is_end_of_word = True
        #print(current_node.children, word[letter], current_node.is_end_of_word)
        #print(arr)

        if check or checkforEqual:
            return word
        else:
            return ""


def checkPrefix(queries):
    #
    # Write your code here.
    #
    trie = Trie()
    word = ""
    for query in queries:
        string = trie.addName(query)
        if string != "":
            word = string
            break
    if word == "":
        print("GOOD SET")
    else:
        print("BAD SET")
        print(word)


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
checkPrefix(arr)
