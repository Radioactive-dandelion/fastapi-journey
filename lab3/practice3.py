from fastapi import FastAPI

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain", "experience": 10, "specialty": "Leadership"},
    {"id": 2, "name": "Alice", "role": "Engineer", "experience": 8, "specialty": "Mechanical"},
    {"id": 3, "name": "Bob", "role": "Scientist", "experience": 5, "specialty": "Biology"}
]


# TODO: Define a Pydantic model for the crew member with:
# - name
# - role
# - experience
# - specialty


# TODO: Define a POST endpoint receiving a crew member model
# Use the code provided in the description to handle the database and response