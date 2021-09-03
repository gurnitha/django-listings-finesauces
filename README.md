#### BUILDING AND DEPLOYING FULLY FUNCTIONAL LISTINGS ECOMMERCE

SOURCE:
Django Made Easy, 2nd Edition by Peter Vought
 

### ---------------
### 1 Initial setup
### ---------------

#### 1.1 Initial commit and create local repository

        NOTE:
        All requirements setup have been installed prior initiating this projec

        (venv3932) λ git init
        (venv3932) λ git add .
        (venv3932) λ git status
        ...

                new file:   .gitignore
                new file:   README.md
        (venv3932) λ git commit -m "1.1 Initial commit and create local repository"


### ---------------------------------
### 2 Starting the e-commerce project
### ---------------------------------

#### 2.1 Creating a Django project

        new file:   finesauces/__init__.py
        new file:   finesauces/asgi.py
        new file:   finesauces/settings.py
        new file:   finesauces/urls.py
        new file:   finesauces/wsgi.py
        new file:   manage.py
        
#### 2.1.1 Running our local development server
###  2.2 Database and Updating project settings
#### 2.2.1 Create database
#### 2.2.2 Connecting the project with the database
#### 2.3 Initial migration
#### 2.4 Remote repository

### -------------------------------
### 3 Creating listings application
### -------------------------------

#### 3.1 Activating listings application
#### 3.2 Designing listings models
#### 3.3 Creating and applying migrations
###  3.4 Creating administration site
#### 3.4.1 Creating superuser
#### 3.4.2 Accessing administration site
#### 3.4.3 Adding models to the administration site
#### 3.4.4 Customizing how models are displayed
###  3.5 Displaying our categories and products
#### 3.5.1 Building our product list view
#### 3.5.2 Creating template for our product list
#### 3.5.3 Adding URL pattern for our view
#### 3.5.4 Filtering by category
#### 3.5.5 Product detail page
#### 3.5.6 Adding reviews
#### 3.6 Local and remote repository

### ---------------
### 4 Shopping cart
### ---------------

#### 4.1 Sessions
#### 4.2 Storing shopping cart in session
#### 4.3 Shopping cart form and views
#### 4.4 Displaying our cart
#### 4.5 Adding products to the cart
#### 4.6 Updating product quantities in cart
###  4.7 Shopping cart link
#### 4.7.1 Setting our cart into the request context

### ------------------
### 5 Customers orders
### ------------------

#### 5.1 Creating order models
#### 5.2 Adding models to the administration site
#### 5.3 Creating customer order
###  5.4 Integrating Stripe payment
#### 5.4.1 Adding Stripe to our view
#### 5.4.2 Using Stripe elements
#### 5.4.3 Placing an order
###  5.5 Sending email notifications
#### 5.5.1 Setting up Celery
#### 5.5.2 Setting up RabbitMQ
#### 5.5.3 Adding asynchronous tasks to our application
#### 5.5.4 Simple Mail Transfer Protocol (SMTP) setup

### -------------------------------
### 6 Extending administration site
### -------------------------------

###  6.1 Adding custom actions to the administration site
#### 6.1.1 Exporting data into .xlsx report
#### 6.1.2 Changing order status
###  6.2 Generating PDF invoices
#### 6.2.1 Installing WeasyPrint
#### 6.2.2 Creating PDF invoice template
#### 6.2.3 Rendering PDF invoices
#### 6.2.4 Sending invoices by email
#### 6.3 Admin site styling

### -------------------
### 7 Customer accounts
### -------------------


###  7.1 Login view
#### 7.1.1 Messages framework
#### 7.1.2 Django LoginView
#### 7.2 Logout view
###  7.3 User registration
#### 7.3.1 Updating product review functionality
#### 7.4 Password change views
#### 7.5 Password reset views
#### 7.6 Extending User model
#### 7.7 Creating user profile section
#### 7.8 Linking orders to customers
#### 7.9 Displaying customer orders

### ---------------------------
### 8 Deploying to DigitalOcean
### ---------------------------

#### 8.1 VPS access and security
#### 8.1.1 Creating Droplet
#### 8.1.2 Creating SSH key
#### 8.1.3 Logging into Droplet
#### 8.1.4 Creating a new user and updating security settings
#### 8.2 Installing software
#### 8.2.1 Database setup
#### 8.3 Virtual environment
#### 8.3.1 Settings and migrations
#### 8.4 Gunicorn setup
#### 8.5 NGINX setup
#### 8.6 Domain setup
#### 8.7 Setting up an SSL certificate

### Conclusion
Reference