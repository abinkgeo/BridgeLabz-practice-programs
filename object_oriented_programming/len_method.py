class Paragraph:

    def __init__(self,text):
        self.text=text
    

    def __len__(self):
        return len(self.text.split())
    



p1=Paragraph("Hello World I Love Python")
print(len(p1))

p2=Paragraph("Python len is one of the various magic methods in Python programming language")

print(len(p2))

