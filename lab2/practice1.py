from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

#TODO: Define a POST endpoint to add a new crew member at the path "/add_crew/"
# - The function should parse the incoming JSON request body to extract the name and role of the new crew member
# - Create a new ID for the new crew member by finding the maximum ID in the database and adding 1, or using 1 if the database is empty
# - Add the new member to the mock database with the new ID
# - Return a JSON response with the new crew member's ID and details