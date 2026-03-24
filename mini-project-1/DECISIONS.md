# DECISIONS.md

## Pydantic Field Types
For Pydantic Field Types I chose `int`, `str`, `date`, `time`, `Enum`.
- `int` was chosen for "id" and "age" because unique personal identifiers and age are numeric values;
- `str` was chosen for "patient names", "doctor names" and "diagnosis" because they are text data;
- `date` and `time` were chosen for appointment dates and times because regular numeric values ​​are not suitable for these fields;
- `Enum` was chosen for the acceptance "status" because the "status" field can only accept a limited set of values.
(Accepted values for "status": "scheduled", "completed", "cancelled")

## Validation Rules
For Validation Rules I used: `min_length` and `max_length`, `ge` and `le`, `@validator`, Optional.
- `min_length` and `max_length` were used to protect "name" fields from empty or too long values (with value 2 for `min_length` and with value 50 for `max_length`);
- `ge` (great or equal) and `le` (less or equal) were used for "age" to prevent negative or unrealistic values ​​from being entered (with value 0 for `ge` and with value 120 for `le`);
- `@validator` was used for the "date" field so that the appointment date could not be set in the past;
- Optional was used for "diagnosis" to indicate that a field can have a value or be None. In the case of diagnosis, this field is optional and may not be filled in immediately, but can be filled in later.

## Async Endpoint
- For `GET /patients/` and `DELETE /items/{id}` I used `asyncio.sleep(1)` and `asyncio.sleep(3)` to simulate an asynchronous delay, as if the server is waiting for some operation to complete (for example, a request to a database or external API). This demonstrates how the server can handle other requests concurrently without blocking work.

## Database
1. What is `@contextmanager` and why do we use it instead of a plain function here?

The `@contextmanager` decorator allows you to create context-controlled blocks using the `with` operator. In this project, it is used to manage the lifecycle of a database connection.

Instead of manually opening and closing the database connection at each endpoint, we define the `managed_db()` function, which automatically:
- opens a connection `(connect_to_db)`;
- creates a table if necessary `(create_table)`;
- returns the database object for use;
- closes the connection after the operation is completed `(close)`.

This ensures that the database connection is always closed correctly, even if an error occurs. Using a simple function would require manually calling `close()` at each endpoint, which is fraught with errors and can lead to resource leaks.

2. What does `check_same_thread=False` do and why is it necessary in a FastAPI application?

The `check_same_thread=False` parameter allows you to use an SQLite connection in multiple threads.

FastAPI is an asynchronous framework capable of processing multiple requests simultaneously, potentially in different threads. By default, SQLite restricts the connection to the thread that created it. Without setting `check_same_thread=False`, this will cause runtime errors when multiple queries attempt to access the database at the same time.

In this project, since each endpoint can be executed asynchronously, we need to disable this restriction to ensure that the database is working correctly with simultaneous access.

3. What happens to your data when the server restarts — with the old list vs. with SQLite?

When using the old Python list stored in RAM `(patients = [])`, all data is stored in RAM. This means that every time the server is restarted, the list is reset, and all previously added data is lost.

In SQLite, data is stored in a file `(sqlite.db)` on disk. This means that even when the server is restarted, all previously saved patient data remains available. The database saves data between runs, making it a much more realistic and reliable data storage solution compared to an in-memory list.