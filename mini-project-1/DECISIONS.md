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

