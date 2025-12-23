class Book1:
    def __init__(self,title,author,isbn,genre):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.genre=genre

class Book2:
    def __init__(self,title,author,isbn,genre):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.genre=genre
    
    def __str__(self): 
        return f"{self.title} by {self.author} \n Isbn number : {self.isbn} Genre: {self.genre}"
    



b1=Book1("Alchemist","Paulo Coelho","87432832","Philosophical fiction")
print(b1)
print(str(b1))


b2=Book2("Alchemist","Paulo Coelho","87432832","Philosophical fiction")
print(b2)

b3=Book2("Python Tutorial","guido van rossum","79867678","Technical manual")
print(str(b3))