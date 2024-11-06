# Make sure to update database credentials in settings.py file 

cd > myproject

# commands to run 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


# api checking
Test API Endpoints using Postman:

    GET /api/products/: Fetch all products.
    POST /api/products/: Create a new product.
    GET /api/products/<id>/: Fetch a single product by ID.
    PUT /api/products/<id>/: Update a product by ID.
    DELETE /api/products/<id>/: Delete a product by ID.



