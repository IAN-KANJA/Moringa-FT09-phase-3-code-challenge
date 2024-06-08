import sqlite3
class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.save_to_database

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    
    def set_id(self, id):
        try:
            if isinstance(id) !=id:
                raise TypeError
        except (ValueError, TypeError) :
            raise TypeError ("id must an integer")
        self._id = id 

    def set_name(self,name):
      if not isinstance(name  ,str):
          raise TypeError("name musy be a string")
      if not (2 <= len(name) <= 16):
          raise TypeError("name must be between 2 and 16 characters")

    def set_category(self , category):
      if not isinstance(category ,str):
          raise TypeError("category must be a string")
      if not len == 0:
          raise ValueError("category length above 0 characters")
      self._category =category  

    def save_to_database(self):
        pass    
            
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        raise AttributeError("Cannot change the id once set") 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._set_name(value)

    @property
    def category(self):
        return self._category   

    @category.setter
    def category(self, value):
        self._set_category(value)

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

    

    def contributors(self):
        conn = sqlite3.connect()
        cursor = conn.cursor()
        query = """
        SELECT DISTINCT authors.id, authors.name
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE articles.magazine_id = ?
        """
        cursor.execute(query, (self._id,))
        contributors = cursor.fetchall()
        conn.close()
        return [{'id': author[0], 'name': author[1]} for author in contributors]
   