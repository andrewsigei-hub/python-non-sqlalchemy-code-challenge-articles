#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    #  Add test code HERE 
    Article.all = []  # Clear the lists just in case
    Magazine.all = []

    a1 = Author("J.K. Rowling")
    m1 = Magazine("The New Yorker", "Literature")

## Intentionally give bad inputs / push the boundaries - All tests should fail
    a_invalid = Author("") # Author must be non empty  
    m_invalid = Magazine("OK", "News") # OK is too short
    art_valid = Article(a1, m1, "Hi") # Hi is too short

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
    