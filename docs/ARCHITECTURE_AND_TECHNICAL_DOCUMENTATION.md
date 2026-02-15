# 🏗 Architecture & Technical Documentation

## Project Overview

Bath & Kitchen Store is a modular Django e-commerce system built around clean architecture principles and real-world logic.

The goal of the project is not just to display products, but to simulate a realistic online store environment with filtering, search, pagination, cart functionality and relational data integrity.

The project uses:

- Django 6
- PostgreSQL
- Class-Based Views
- Session-based cart logic
- Slug-based routing
- Reusable template partials

---

## Project Structure

The project is divided into four Django apps to maintain separation of concerns.

### catalog

Handles all product-related logic:

- Product model
- Brand model
- Category model
- Filtering logic
- Search logic
- Pagination system

All CRUD operations are implemented using Django Class-Based Views:

- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView

Search is implemented inside `get_queryset()` using Django Q objects.

Pagination is handled via a reusable `_pager.html` partial.

---

### projects

Responsible for showcasing interior design projects.

Main logic:

- ProjectPost model
- Many-to-Many relationship with Product
- Section filtering (Bath / Kitchen)
- total_price() helper method

Example logic:

A ProjectPost may contain multiple related products.
The total_price() method calculates the sum of all related products dynamically.

---

### shopping_cart

Implements session-based cart logic.

Cart data is stored inside:

request.session["cart"]

Cart supports:

- Add to cart
- Update quantity
- Remove item
- Clear cart
- Automatic total price calculation

The cart does not require user authentication.

---

### core

Contains shared logic and validation:

- Custom price validator
- Image size validation (max 15MB)
- Allowed file type validation (jpg, jpeg, png, webp)
- Shared helper functions

---

## Database Relationships

Brand → Product (ForeignKey)  
Category → Product (ForeignKey)  
ProjectPost ↔ Product (ManyToMany)

All relationships are enforced at database level using PostgreSQL.

---

## Model Overview

### Product
Core entity of the system.

Fields include:
- title
- slug
- unique_id
- price
- description
- image
- is_featured
- is_promo

Includes:
get_absolute_url() method for clean redirection.

---

### Category
Used for structuring products into Bath and Kitchen sections.

Fields:
- title
- slug
- section
- description
- category_image

---

### Brand
Represents product manufacturers.

Fields:
- name
- slug
- logo

---

### ProjectPost
Represents interior showcase posts.

Fields:
- title
- slug
- section
- excerpt
- content
- cover_image

Relationship:
Many-to-Many with Product.

Includes:
total_price() method.

---

## View Architecture

All views use Class-Based Views.

Benefits:
- Clean code
- Reusable logic
- Easier maintenance
- Automatic form handling

Delete operations use confirmation templates to prevent accidental deletion.

---

## Filtering & Search Logic

Filtering supports:

- Section (Bath / Kitchen)
- Category
- Brand
- Keyword search
- Sorting by price or title

All filtering happens at the QuerySet level for efficiency.

---

## Security & Validation

- CSRF protection enabled
- Slug-based routing prevents ID exposure
- File validation for image uploads
- Environment variables for sensitive data
- Price constraint validation

---

## Scalability Notes

The modular structure allows:

- Easy feature extension
- Future user authentication
- Order system integration
- Payment gateway integration
- API version development

The architecture is production-ready and extensible.
