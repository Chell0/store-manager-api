# Store-Manager-API

[![Build Status](https://travis-ci.org/Chell0/store-manager-api.svg?branch=develop)](https://travis-ci.org/Chell0/store-manager-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/4b92c9aaa1b145f726ef/maintainability)](https://codeclimate.com/github/Chell0/store-manager-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Chell0/store-manager-api/badge.svg?branch=develop)](https://coveralls.io/github/Chell0/store-manager-api?branch=develop)


A web application that helps store owners manage sales and product inventory records by allowing them to _CREATE_ sale orders and products, **_FETCH_** all sales and products and **_RETRIEVE_** a single sale order and product.

## Development SetUp

What you need to run this API.

1. Python 3.
2. Virtualenv environment.
3. Postman.

## Installation

How to get your development environment running.

- Clone the repository.
- Unzip the files to your preferred location.
- **cd** into **sore-manager-api then api** folder.
- Install a virtual environment ```pip install virtualenv venv```
- Install the requirements.txt ```pip install -r requierments.txt```
- Install [Postman](https://www.getpostman.com/).

## Running Tests

cd into ```store-manager-api-->api``` RUN ```python run.py```.

_key_: Content-Type value: application/json

To test authentication, add this to the header: Get Token from login endpoint

_key_: Authorization _value_: JWT TOKEN

| Methods | Endpoint| Action |
| --- | --- | --- | 
| GET | http://127.0.0.1:5000/v1/sales | (get all your sales) | 
| POST | http://127.0.0.1:5000/v1/sales | (create a sale order) |
| GET | http://127.0.0.1:5000/v1/sales/id | (get a single sale order by id) |
| GET | http://127.0.0.1:5000/v1/products | (get all your products) |
| POST | http://127.0.0.1:5000/v1/products | (create a product) |
| GET | http://127.0.0.1:5000/v1/products/id | (get a single product by id) |

## Meta

Gabriel Machel - [Twitter](https://twitter.com/Ch3ll0h)

## Contributing

1. Fork it ```yourname/yourproject/fork```
2. Create your feature branch ```git checkout -b feature/fooBar```
3. Commit your changes ```git commit -m 'Add some fooBar'```
4. Push to the branch ```git push origin feature/fooBar```
5. Create a new Pull Request