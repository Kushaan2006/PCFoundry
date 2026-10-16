"""Database schemas for the PCFoundry database."""

import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import CollectionInvalid

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
  raise ValueError("Missing MongoDB URI.")

client = MongoClient(uri)
db = client["PCFoundry"]

product_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["name", "brand", "type", "price", "stock", "specs", "ratings"],
    "properties": {
      "name": {"bsonType": "string"},
      "brand": {"bsonType": "string"},
      "type":  {"bsonType": "string"},
      "price":  {"bsonType": "double", "minimum": 0},
      "stock": {"bsonType": "int", "minimum": 0},
      "specs": {"bsonType": "object"},
      "ratings": {"bsonType": "array", "items": {"bsonType": "int", "minimum": 1, "maximum": 5}}
    }
  }
}

review_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["productId", "rating", "username", "isAnonymous", "date", "content"],
    "properties": {
      "productId": {"bsonType": "objectId"},
      "rating": {"bsonType": "int", "minimum": 1, "maximum": 5},
      "username": {"bsonType": "string"},
      "isAnonymous": {"bsonType": "bool"},
      "date": {"bsonType": "date"},
      "content": {"bsonType": "string"}
    }
  }
}

user_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["name", "email", "password", "cart", "saved_builds"],
    "properties": {
      "name": {"bsonType": "string"},
      "email": {"bsonType": "string"},
      "password": {"bsonType": "string"},
      "cart": {"bsonType": "array"},
      "saved_builds": {"bsonType": "array"}
    }
  }
}

try:
  db.create_collection("products", validator=product_validator)
  print("Product schema created.")
except CollectionInvalid:
  db.command({
    "collMod": "products",
    "validator": product_validator
  })
  print("Updated product schemas.")

try:
  db.create_collection("reviews", validator=review_validator)
  print("Review schema created.")
except CollectionInvalid:
  db.command({
    "collMod": "reviews",
    "validator": review_validator
  })
  print("Updated review schemas.")

try:
  db.create_collection("users", validator=user_validator)
  print("User schema created.")
except CollectionInvalid:
  db.command({
    "collMod": "users",
    "validator": user_validator
  })
  print("Updated user schemas.")

db["reviews"].create_index("productId")
db["users"].create_index("email", unique=True)