# ARTSYSTORE

This repository contains the code for an e-commerce website developed using the Django web framework, with the Stripe payment method integrated. The front end of the website is built using Bootstrap, a popular front-end framework for responsive web design.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Product catalog with search and filtering options
- Shopping cart functionality
- Integration with the Stripe payment gateway for secure and seamless payments
- Order management and tracking
- User profile management
- Admin panel for managing products, orders, and user accounts

## Requirements

To run this project locally, you need to have the following dependencies installed:

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)
- Stripe Python library (version 2.0 or higher)
- Bootstrap (version 4.0 or higher)

## Installation

1. Clone this repository to your local machine or download the zip file.
2. Change to the project's root directory.
3. Create a virtual environment to isolate the project's dependencies.
4. Activate the virtual environment.
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source venv/bin/activate
  ```
5. Install the required Python packages.


## Configuration

1. Create a Stripe account at [stripe.com](https://stripe.com) if you don't have one already.

2. Obtain your Stripe API keys from the Stripe dashboard.

3. In the project's root directory, create a `.env` file and add the following environment variables: Replace `your_django_secret_key` with a secret key of your choice. You can generate a new secret key using Django's `secret_key` module.

4. Run database migrations to set up the database schema.


## Usage

1. Start the development server.

2. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the website.

3. Register a new user account or log in with an existing account.

4. Browse the product catalog, add items to the shopping cart, and proceed to checkout.

5. At the checkout page, you will be redirected to the Stripe payment gateway to complete the payment process.

6. After a successful payment, the order will be placed, and you can view your order details in the user profile or admin panel.

## Contributing

Contributions to this project are welcome. If you find any bugs or want to add new features, please open an issue or submit a pull request with your changes.

## License

 Feel free to use and modify the code for your own purposes.



