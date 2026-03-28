1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

ODM (Object-Document Mapper) is a library that allows you to work with MongoDB documents as with regular Python objects.

We use Beanie to make writing code easier and safer: instead of complex raw queries, we use objects and methods (insert(), find(), update()), while Beanie checks types, automatically serializes data, and manages indexes. This reduces the chance of errors and speeds up development.

2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?

The `Database` class wraps Beanie methods to make working with the model easier. It makes the code in routes cleaner, allows you to reuse the logic of working with the database and add error handling or logging in one place.

3. What happens if `initialize_database()` is not called on startup? What would break and why?

If `initialize_database()` is not called at startup, Beanie will not know which models to use. Any method call will generate an error, because the ODM hasn't yet been initialized.
FastAPI will be able to start, but all database operations will fail.

4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?

The `Event` is the main Beanie document that fully describes how data is stored in MongoDB. It is needed for data manipulation (saving and retrieving data from a database).

`EventUpdate` is a Pydantic class for updates. It usually contains only those fields that can be changed via the API, and they may be optional.

We use two classes, because they solve different problems.
