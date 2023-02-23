class Redmi:
    name="Redmi"
    a="Redmi the is origin of  all the models"
class Note(Redmi):
    name="Redmi note"
class Pro(Note):
    name="Redmi note pro"
class Max(Pro):
    name="Redmi note pro max"
ob=Pro()
print(ob.name)
print(ob.a)
