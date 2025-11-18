class Article:

    # 1. This is the CLASS VARIABLE.
    # It will hold all Article instances.
    all = []

    def __init__(self, author, magazine, title):  # Refers to the new article
        self.author = author
        self.magazine = magazine
        self.title = title

        # 2. 'self' is the new Article instance.
        # We add it to the shared 'all' list.
        Article.all.append(self)

    # Now future relationship methods can look through Article.all to answer questions like:
    # "Which articles belong to this author?"
    # "Which articles belong to this magazine?"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        # Immutable: use the hasattr check
        if not hasattr(self, "_title"):
            if isinstance(title, str) and 5 <= len(title) <= 50: # Validation of data (between 5 and 50 characters)
                self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        # Mutable: just check the type
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        # Mutable: just check the type
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine


class Author:
    def __init__(self, name):
        # Calls @name.setter
        self.name = name

    @property
    def name(self):
        # This is the getter
        return self._name

    @name.setter
    def name(self, name):
        # Check for immutability
        if not hasattr(self, "_name"):
            # Checks validation rules:
            if isinstance(name, str) and len(name) > 0:
                # If valid set the private variable
                self._name = name
            else:
                # This is for bonus round
                pass

    def articles(self):
        # Returns a lst of all articles written by this author
        # Filter the SSOT
        return [article for article in Article.all if article.author == self ]

    def magazines(self):
        # Returns a unique list of magazines this author has contributed to
        my_articles = self.articles() # Gets all my articles

        my_magazines = [article.magazine for article in my_articles] # Gets magazine for each article

        return list(set(my_magazines)) # Uses set to only get unique magazines

    def add_article(self, magazine, title):
        # A new article and associates it with author
        # self is the author insatnce 
        # Automatically runs Article.__init__
        # And add the new article to article.all

        return Article(self, magazine, title)

    def topic_areas(self):
        #Returns a unique list of categories from the author's magazines
        # 1. Get all my unique magazines
        my_magazines = self.magazines()
        
        # 2. Handle the "None" case (tested in test_topic_areas_are_unique)
        if not my_magazines:
            return None
            
        # 3. Get the category from each magazine
        categories = [mag.category for mag in my_magazines]
        
        # 4. Return the unique list
        return list(set(categories))


class Magazine:

    # 1. This is the CLASS VARIABLE for Magazine.
    # It will hold all Magazine instances.
    all = []

    def __init__(self, name, category): # Initialisises a new object with all its required data 
        self.name = name
        self.category = category

        # 2. 'self' is the new Magazine instance.
        # We add it to the shared 'all' list.
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Mutable: Just Validate the new value
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        # Mutable: just validate the new value
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        # Returns a lis of all articles published in this magazine
        return [ article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Returns a unique list of authors who wrote this magazine 
        my_articles = self.articles()
        my_authors = [article.author for article in my_articles]
        return list(set(my_authors))

    def article_titles(self):
        # Returns a list of titles for this magazines articles
        #Returns a list of titles for this magazine's articles"""
        my_articles = self.articles()
        
        # Handle the "None" case (tested in test_article_titles)
        if not my_articles:
            return None
            
        return [article.title for article in my_articles]

    def contributing_authors(self):
        """
        Returns a list of authors who have written
        more than 2 articles for this magazine.
        """
        # This one is trickier! We need to count.
        
        author_counts = {}
        my_articles = self.articles()
        
        # 1. Loop through all my articles and count each author
        for article in my_articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
                
        # 2. Filter that dictionary
        #    Give me the author for each (author, count) pair
        #    if the count is greater than 2
        result = [author for author, count in author_counts.items() if count > 2]
        
        # 3. Handle the "None" case (tested in test_contributing_authors)
        return result if result else None
