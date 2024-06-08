import sqlite3 

class Article:
        def __init__(self, id, title, content, author_id, magazine_id):
            self.id = id
            self.title = title
            self.content = content
            self.author_id = author_id
            self.magazine_id = magazine_id
            self.save_to_database()
            

        def __repr__(self):
            return f'<Article {self.title}>'
        
        

        def _set_name(self, name):
            if not isinstance(name, str):
                raise TypeError("name must be of type str")
            if len(name) == 0:
                raise ValueError("name must be longer than 0 characters")
            self._name = name

        def set_property_title(self,propertyTitle):
            if not isinstance(propertyTitle, str):
                raise TypeError("propertytitle must be a string")
            if not (5 <= len(propertyTitle) <=50):
                raise ValueError("propertytitle must be between 5 to 50 characters")
        
        def save_to_database(self):
            pass

        @property
        def propertyTitle(self):
            return self.property_title
        
        @propertyTitle.setter
        def propertyTitle(self, value):
            raise AttributeError("Can`t change one set")
        
        @property
        def author(self):
            return self.get_author()
        
        @property
        def magazine(self):
            return self.given_magazine()
        
        def get_author(self):
          conn = sqlite3.connect()
          cursor = conn.cursor()
          query = """
            SELECT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE articles.id = ?
            """
          cursor.execute(query, (self._id,))
          author = cursor.fetchone()
          conn.close()
          if author: 
              return  {'id': author[0], 'name': author[1]}
        
        def given_magazine(self):
          conn = sqlite3.connect()
          cursor = conn.cursor()
          query = """
            SELECT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE articles.id = ?
            """
          cursor.execute(query, (self._id,))
          author = cursor.fetchone()
          conn.close()
          if author: 
              return  {'id': author[0], 'name': author[1]}