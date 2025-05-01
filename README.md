
# Poets API

A RESTful API for accessing classical Persian poetry and literature, including works from Hafez, Khayyam, Moulavi, and Sa'adi.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
  - [Running Locally Without Docker](#Running-Locally-Without-Docker)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Access to classical Persian poetry from renowned poets
- Random poem selection functionality
- Filter poems by category and specific numbers
- RESTful API design with JSON responses
- Support for Hafez's ghazals, ghete, robaee, ghaside, and montasab
- Support for Khayyam's robaee and tarane
- Support for Moulavi's works from Shams and Masnavi
- Access to Golestan hekayat by bab and hekayat numbers

---

## Requirements

- Python (3.9-slim)
- Django & Django REST Framework

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/poets-api.git
cd poets-api
```

---

## Running the Application

### Running Locally Without Docker

If running locally:
### 1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply Migrations:

```bash
python manage.py makemigrations
python manage.py migrate --fake-initial
```

### 4. Create superuser
```bash
python manage.py createsuperuser
```

### 5. Run the Django Server:

```bash
python manage.py runserver
```

---

## API Endpoints

### You can see complete documentation of [Poets API Endpoints](endpoints.md) in the endpoints.md file.

---

## Contributing

Contributions are welcome! Please submit pull requests or open issues. Make sure to update tests and documentation accordingly.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.