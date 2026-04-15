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


## Part B
1. Why does `DATABASE_URL` use `mongo` as the hostname instead of `localhost`? What would happen if you kept `localhost`?

`DATABASE_URL` use `mongo` as the hostname instead of `localhost`, because in Docker Compose, all services run on a shared network and can access each other by service name. In this case, mongo is the name of the database container, and the application uses it to find the desired service.

If we leave `localhost`, the application will try to connect to the database inside its own container, where it is missing, so the connection will not be established and a connection error will occur.

2. What does `depends_on` in `docker-compose.yml` do? Does it guarantee MongoDB is fully ready before FastAPI starts — and if not, what would?

`depends_on` in `docker-compose.yml` is used to set the order in which services are started: it ensures that the MongoDB container is started earlier than the FastAPI container. 
However, as I was working, I noticed that this does not guarantee that MongoDB is fully ready to receive connections. Sometimes the app still tries to connect too early.

Thus, `depends_on` controls only the startup order, but not the ready status of the service.

3. What is the purpose of the volume in the `mongo` service? What happens to your data if you remove it and run `docker compose down`?

Volume is used to store MongoDB data outside the container. This allows you to save data between restarts.

If there is a volume, then the data was saved after the containers were stopped and restarted. And if you remove volume and run `docker compose down`, then all previously created data has been deleted.
This is because without volume, data is stored only inside the container, and when it is deleted, it is lost.

4. Why do we copy `requirements.txt` and run `pip install` before copying the rest of the app code in the Dockerfile?

The order of instructions in a Dockerfile affects the Docker layer caching mechanism. If you copy `requirements.txt` and install dependencies first (like `pip install`), this layer can be cached and reused in subsequent builds if the dependencies haven't changed. 
However, if you copy all the code at once, any change to the project causes all dependencies to be reinstalled, increasing build time.

In fact, the order of instructions (first, copy `requirements.txt` and run `pip install`) is used to optimize the build process.