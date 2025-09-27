# PESEL Validator – Django Application

## Overview
This Django web application allows users to input a **PESEL number** (Polish national identification number) and verifies its validity according to the official specification.  
In addition to checking correctness, the app extracts useful information such as **birth date** and **gender** from the PESEL.

---

## Features
- Input a PESEL number via a simple form on the homepage.
- Validate the PESEL according to official rules (length, checksum, and birth date).
- Display additional information:
  - Birth date
  - Gender
- Show detailed error messages if the PESEL is invalid.

---

## Requirements
- Python 3.13+  
- Django 5.2+  
- Poetry (for dependency management)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pesel-validator.git
   cd pesel-validator
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
   
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

---

## Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
   
2. Open your browser and visit:
   ```cpp
   http://127.0.0.1:8000/
   ```
   
3. Enter a PESEL number in the form and submit.
4. View the validation result along with birth date and gender (if valid).

---

## Project structure
```csharp
pesel_validator/
├── manage.py
├── pyproject.toml        # Poetry configuration
├── poetry.lock           # Dependency lock file
├── pesel_validator/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── validator/
│   ├── forms.py          # PESEL input form
│   ├── utils.py          # PESEL validation logic
│   ├── templates/
│   │   └── validator/
│   │       └── home.html # Homepage template
│   └── ...
```

---

## Development notes
* The app uses a clean Django forms + utility function separation for maintainability.
* Templates are organized per app (validator/templates/validator/).
* Validation logic includes:
    * Checksum verification
    * Correct month and birth date decoding
    * Gender extraction from PESEL
