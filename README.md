# ComputeX API Django Application

This project is a Django-based API application for processing CSV files with basic arithmetic operations. Users can upload a CSV file with numerical data, and the application will compute the result, store it in a database, and return it via an HTTP response.

---

## Features

- **CSV File Upload**: Users can upload CSV files containing columns `A`, `O`, and `B`.
- **Operations**: The app supports arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Result Storage**: Stores the calculated result for each request in the database, along with the user and request details.
- **Authorization Options**: Basic passphrase authorization or JWT-based authentication.
- **Unit Testing**: Includes tests for calculations using Pytest.

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite
- **Testing**: Pytest for unit tests

---
