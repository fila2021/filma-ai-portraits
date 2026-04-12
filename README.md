# Askuala AI Portraits

Askuala AI Portraits is a Django-based premium AI portraits storefront and custom request platform.  
It allows users to browse portrait products, explore gallery work, request custom AI portrait services, manage accounts, and leave reviews.

## Features

- Premium homepage and storefront design
- Product listing and product detail pages
- Gallery showcase
- Services listing and service detail pages
- Custom request creation and request tracking
- User authentication
- Profile view and edit
- Review system
- Payment success flow
- Premium dark/light theme toggle

## Apps Used

- `home`
- `accounts`
- `gallery`
- `shop`
- `services`
- `payments`
- `reviews`

## Project Structure

- `templates/` — main Django templates
- `templates/includes/` — shared navbar/footer
- `static/css/style.css` — global premium styling
- `static/js/theme.js` — theme toggle logic

## How to Run Locally

1. Activate your virtual environment
2. Run migrations:
   ```bash
   python3 manage.py migrate
   python3 manage.py runserver
   ## Main Pages

- `/` — homepage  
- `/gallery/` — gallery  
- `/shop/` — product listing  
- `/services/` — services  
- `/reviews/` — reviews  
- `/accounts/login/` — login  
- `/accounts/signup/` — signup  

---

## Design Direction

The project was visually refined into a premium storefront experience inspired by high-end digital marketplace patterns:

- dark luxury palette  
- gold accent system  
- serif headings  
- premium cards  
- stronger section hierarchy  
- cleaner CTAs and forms  

---

## Testing Checklist

- Homepage loads correctly  
- Navbar links work  
- Theme toggle works  
- Products display correctly  
- Services display correctly  
- Request creation works  
- Profile page works  
- Review pages work  
- Payment success page loads  
- 404 page displays correctly  

---
