# FinGen API - Django Quotation and Invoice Management System

FinGen API is a Django application for managing quotations, invoices, and ledger accounts.

## Getting Started 

1. Clone the repository:

    ...bash
    git clone https://github.com/KamauDev-maker/FinGen-API.git
    cd FinGen-API
    ...

2. Create a virtual environment and install dependencies:

    ...bash
    python3 -m venv virt
    source virt/bin/activate
    pip install -r requirements.txt
    ...

3. Apply migrations:

    ...bash
    python3 manage.py migrate
    ...

4. Run the development server:

    ...bash
    python3 manage.py runserver
    ...

## API Endpoints

## Create Quotation

- **Endpoint:** '/api/quotations/'
- **Method:** POST
- **Request Paylod Example:**

    ...json

    {
        
      "customer_name": "Sammy Keen",
      "number_of_items": 4,
      "price": 30.0
    }
    ...

- **Response Example:**

    ...json

    {

        "id": 2,
        "customer_name": "Sammy Keen",
        "number_of_items": 4,
        "price": 30.0,
        "invoice_number": "INV-2",
        "issue_date": "2023-12-21",
        "due_date": "2024-01-20",
        "total_amount": "120.00",
        "is_paid": false,
        "quotation": 2
    }

### Created Invoices

- **Endpoint:** 'api/invoices/'
- **Method:** GET
- **Response Example (GET):**

    ...json

    [

        {

            "id": 1,
            "customer_name": "Sammy Keen",
            "number_of_items": 4,
            "price": 30.0,
            "invoice_number": "INV-1",
            "issue_date": "2023-12-21",
            "due_date": "2024-01-20",
            "total_amount": "120.00",
            "is_paid": false,
            "quotation": 1
        },
    ]

### List Created Ledger Account

- **Endpoint:** '/api/ledger-accounts/'
- **Method:** GET
- **Response Example (GET):**

    ...json

    {
        "total_amount": 120.0,
        "ledger_accounts": [

            {
                "id": 1,
                "number_of_items": 4,
                "price": 30.0,
                "customer_name": "Sammy Keen",
                "balance": "120.00",
                "last_updated": "2023-12-21T14:40:07.543665Z"
            },
        ]
    }      

## Technology Stack

- Django
- Django Rest Framework

## License

Copyright (c) 2023 [Oscar Kamau](https://github.com/KamauDev-maker)  