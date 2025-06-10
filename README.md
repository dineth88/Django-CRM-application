Django CRM Application

https://github.com/user-attachments/assets/79cd47de-320d-4077-9c03-4e968ba572e8

This is a basic Customer Relationship Management (CRM) application built using Django. It allows you to manage customers, products, and orders. Administrators have full control over the system, while customers can view their order history and profile information.

Features
Customer Management: Create, view, update, and delete customer records.
Product Management: Add, view, and manage products available in the system.
Order Management: Create, view, update, and delete customer orders.
User Authentication and Authorization: Separate login and registration for administrators and customers.
Role-Based Access Control: Administrators have access to all features, while customers have limited access to their own data.
Order Filtering: Admins can filter orders based on various criteria.
User Profile Management: Customers can view and update their profile information.
Installation
Follow these steps to set up and run the Django CRM application on your local machine.

Steps
Clone the Repository:
If you haven't already, clone the project repository to your local machine using Git:
```bash
git clone &lt;repository_url>
cd &lt;project_directory>
```
Replace <repository_url> with the actual URL of your GitHub repository and <project_directory> with the name of the cloned directory.

Create and Activate a Virtual Environment (Recommended):
It's good practice to use a virtual environment to isolate project dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On macOS and Linux

venv\Scripts\activate # On Windows
```

Install Dependencies:
Install the required Python packages from the requirements.txt file (if you have one. If not, you'll need to install Django manually):
```bash
pip install django

If you have other dependencies, create requirements.txt first:
pip freeze > requirements.txt
Then install:
pip install -r requirements.txt
```

Make Migrations:
Apply the initial database migrations to set up the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a Superuser (Admin Account):
Create an administrative user to access the admin dashboard:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a username, email address, and password.

Run the Development Server:
Start the Django development server:
```bash
python manage.py runserver
```

Access the Application:
Open your web browser and navigate to http://127.0.0.1:8000/.

### Accessing Admin Dashboard

To access the administrator interface, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created.

Creating a Customer Group
Make sure you create a 'customer' group in the Django admin interface (/admin/auth/group/add/) and assign regular users to this group for proper role-based access control.

Creating Initial Products (Admin)
Log in as an administrator and navigate to the product section (usually accessible from the dashboard) to create initial product entries.

Registering as a Customer
Navigate to the registration page (usually /register/) to create a customer account.

Logging In
Use the login page (/login/) to log in as either an administrator or a customer.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
