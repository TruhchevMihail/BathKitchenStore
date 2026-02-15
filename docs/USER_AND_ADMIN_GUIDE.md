# ⚡ Developer Cheat Sheet

Quick reference for developers working on the project.

---

## Main Commands

```bash
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py check
```

---

## Key URLs

/  
/products/  
/products/<slug>/  
/categories/  
/projects/  
/cart/  
/admin/

---

## Relationships

Brand → Product  
Category → Product  
ProjectPost ↔ Product  

---

## Important Methods

Product.get_absolute_url()  
ProjectPost.total_price()  

---

## Cart Session Structure

Cart data example:

{
  "product_id": {
    "quantity": 2,
    "price": 120.00
  }
}

Stored in:

request.session["cart"]

---

## Validation Rules

Price:
0.01 – 10000

Image:
Max 15MB  
jpg / jpeg / png / webp

---

## Architecture Notes

- Uses Django Class-Based Views
- Reusable pagination partial
- QuerySet-based filtering
- Slug-based routing
- Session-based cart
- Modular multi-app design

---

## Future Improvements

- User authentication
- Order model
- Payment integration
- REST API
- Docker deployment
