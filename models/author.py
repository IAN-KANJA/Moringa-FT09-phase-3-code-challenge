import sqlite3


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.save_to_database()

    def __repr__(self):
        return f'<Author {self.name}>'
    

    def _set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("id must be of type interger")
        self._id = id

    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be of type string")
        if len(name) == 0:
            raise ValueError("name must be longer than 0 characters")
        self._name = name

    def _save_to_database(self):
        pass


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value,str):
          raise AttributeError("Cannot change the id once set")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value):
         raise AttributeError("Cannot change the name once set")    
        
    def articles(self):
        conn = sqlite3.connect()
        cursor = conn.cursor()
        query = """
        SELECT articles.id, articles.title
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE authors.id = ?
        """
        cursor.execute(query, (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return [{'id': article[0], 'title': article[1]} for article in articles]

    def magazines(self):
        conn = sqlite3.connect()
        cursor = conn.cursor()
        query = """
        SELECT DISTINCT magazines.id, magazines.name, magazines.category
        FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE articles.author_id = ?
        """
        cursor.execute(query, (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return [{'id': magazine[0], 'name': magazine[1], 'category': magazine[2]} for magazine in magazines]
    def article_titles(self):
        conn = sqlite3.connect()
        cursor = conn.cursor()
        query = """
        SELECT title
        FROM articles
        WHERE magazine_id = ?
        """
        cursor.execute(query, (self._id,))
        titles = cursor.fetchall()
        conn.close()
        if not titles:
            return None
        return [title[0] for title in titles]

    def contributing_authors(self):
        conn = sqlite3.connect()
        cursor = conn.cursor()
        query = """
        SELECT authors.id, authors.name, COUNT(articles.id) as article_count
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        GROUP BY authors.id, authors.name
        HAVING article_count > 2
        """
        cursor.execute(query, (self._id,))
        authors = cursor.fetchall()
        conn.close()
        if not authors:
            return None
        return [Author(author[0], author[1]) for author in authors]