# Orange Seller

**Orange Seller** is a Django project that demonstrates advanced ORM features, including custom querysets, validations, and optimized views tailored for managing a fictional orange-selling marketplace. This project showcases Django’s powerful Object-Relational Mapping (ORM) capabilities, with a focus on creating complex queries, enforcing custom validation rules, and presenting filtered data efficiently.

## Project Features

- **Custom Validations**: Implements unique validation rules for data integrity, ensuring only valid entries are saved to the database. These validations add an extra layer of control, essential for maintaining high-quality data.

- **Advanced Querysets**: Leverages Django’s ORM to create complex queries that retrieve and filter data based on specific conditions. This includes custom annotations, aggregate functions, and condition-based filtering for managing seller and product data effectively.

- **Optimized Views for Querysets**: Contains views designed specifically to handle custom querysets, delivering data in a clear, user-friendly format. These views serve as endpoints to showcase filtered data based on project needs.

## Project Purpose

The primary goal of **Orange Seller** is to enhance understanding of Django ORM and explore the potential of custom queries and validations. By enforcing validation logic, the project ensures data consistency and reliability, making it ideal for developers interested in creating structured, data-driven applications in Django.

## Technologies Used

- **Python** - For core development
- **Django** - As the web framework
- **Jalali Date Library** - For handling date-specific queries and validations

## Key Components

### 1. Custom Validation
This project includes model-level custom validation functions, adding specific rules for data control. These rules ensure that only compliant data entries are saved.

### 2. Querysets for Custom Filtering
Using Django’s ORM, various queryset functions are created to filter sellers based on distinct criteria, such as:
   - Sellers with multiple registered products
   - Sellers who meet defined product-to-price ratios
   - Sellers filtered based on time-based order criteria

### 3. Views for Displaying Query Results
Each queryset has a corresponding view, simplifying the display of filtered data for user access. These views improve usability by organizing and presenting data according to the project’s objectives.

## Setup Instructions

### 1. Clone this repository:
   ```bash
   git clone https://github.com/AfshinMoussavi/Orange-Seller.git
   ```
   
### 2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Apply migrations:
  ```bash
  python manage.py migrate
  ```

### 4. Create a superuser for accessing the Django admin:
  ```bash
  python manage.py createsuperuser
  ```

### 5. Run the development server:
  ```bash
  python manage.py runserver
  ```

### 6. Visit the local server at http://127.0.0.1:8000/ to explore Orange Seller.
