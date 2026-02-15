# QUICK REFERENCE

## PROJECT OVERVIEW

4 apps, 4 models, 28+ views, session-based cart, PostgreSQL

## APPS

**Catalog** - 14 views, 6 forms  
Products, categories, brands with filtering and search

**Projects** - 5 views, 2 forms  
Showcase projects with related products (M2M)

**Shopping Cart** - 6 views  
Session-based cart system

**Core** - Utilities and error handlers

## DATABASE

Brand → Product (FK)  
Category → Product (FK)  
ProjectPost ↔ Product (M2M)

Price validation: 0.01-10000  
Image validation: 15MB max, jpg/jpeg/png/webp only

## USEFUL COMMANDS

```bash
python manage.py runserver           # Start dev server
python manage.py migrate             # Apply migrations
python manage.py createsuperuser     # Create admin user
python manage.py check               # Check for errors
```

## KEY URLS

`/` Home  
`/products/` All products  
`/products/<slug>/` Product detail  
`/categories/` Browse categories  
`/catalogue/` Browse brands  
`/projects/` Projects  
`/cart/` Shopping cart  
`/admin/` Admin panel

## TECH STACK

Django 6.0.2, PostgreSQL, Bootstrap 5, Python 3.13

## DOCUMENTATION

`README.md` - Main doc  
`FULL_DOCUMENTATION.md` - Complete reference  
`PRACTICAL_GUIDE.md` - How to use  

All in `docs/` folder (except README.md)

