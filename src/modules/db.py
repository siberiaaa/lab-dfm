import pymongo

uri = "mongodb+srv://pyapp:jrNQOkI36Gs04PrL@dave.qhyzhzr.mongodb.net/?retryWrites=true&w=majority&appName=Dave"

client = pymongo.MongoClient("uri")

# Podemos acceder a la BD
db = client.personascrud

# Y tuego podemos acceder a tas colecciones
collection = db.personas