#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # --- Add test code HERE ---
    Article.all = []  # Clear the lists just in case
    Magazine.all = []

    a1 = Author("J.K. Rowling")
    m1 = Magazine("The New Yorker", "Literature")

    # This line will run the __init__ methods
    art1 = Article(a1, m1, "A New Story")
    art2 = Article(a1, m1, "Another Story")
    # --- End test code ---

    # don't remove this line, it's for debugging!
    ipdb.set_trace()