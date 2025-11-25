class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    ## Title Getter

    @property
    def title(self):
        return self._title

    ## Title Setter

    @title.setter
    def title(self, title):
        ## HASATTR
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 6 and 50 characters")

    ## Author getter
    @property
    def author(self):
        return self._author

    ## Author setter
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")

    ## magazine getter
    @property
    def magazine(self):
        return self._magazine

    ## magazine setter
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance magazine class")


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
       if hasattr(self, "_name"):
        raise AttributeError("Author name cannot be changed after set")
       if isinstance(name, str) and len(name) > 0:
        self._name = name


    def articles(self):
        articles_by_author = []  ## New list
        for article in Article.all:
            if (
                article.author == self
            ):  ## IF the article is written by the author then add it to the list
                articles_by_author.append(article)
        return articles_by_author

    def magazines(self):
        magazines = []

        for article in self.articles():
            if article.magazine not in magazines:
                magazines.append(article.magazine)
        return magazines

    def add_article(
        self, magazine, title
    ):  ## Create a new article instance associated with authors name
        if not isinstance(magazine, Magazine):
            raise TypeError("Argument must be a magazine instance")

        new_article = Article(self, magazine, title)
        return new_article


## Aggregate Method


def topic_areas(self):
    categories = []

    # 1. Get the unique list of Magazine objects
    unique_mags = self.magazines()  # Sets automatically remove duplicates

    if not unique_mags:
        return None

    for mag in unique_mags:
        category_name = mag.category ## 

        if category_name not in categories:
            categories.append(category_name) ## Logic allows for magaiznes that share a catergory to be added 

    return categories


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must contain string with 2 - 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def contributors(self):
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)

        return authors

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
