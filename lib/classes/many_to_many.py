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
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass


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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
