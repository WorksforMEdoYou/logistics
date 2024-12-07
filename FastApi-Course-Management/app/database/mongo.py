from pymongo import MongoClient

# making the mongodb conncetion at "mongodb://localhost:27017/course_management"
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client['course_management']