# Filma AI Portraits

Custom AI portrait studio with ready-made packs and bespoke requests, built on Django.

## Quick start
1. Clone and enter the project.
2. Create/activate venv (Python 3.10+ recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
4. Set env vars (Stripe test keys):
   ```bash
   export STRIPE_SECRET_KEY=sk_test_...
   export STRIPE_PUBLISHABLE_KEY=pk_test_...
   ```
5. Migrate and run:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Features
- Accounts with profile edit
- Gallery listing
- Shop products with Stripe Checkout
- Services: custom request CRUD with price preview
- Reviews for products and custom requests
- Admin for all models

## Environment variables
- `STRIPE_SECRET_KEY` (required for live Stripe Checkout)
- `STRIPE_PUBLISHABLE_KEY` (required)

## Stripe test instructions
- Use test mode keys from Stripe Dashboard → Developers → API keys.
- Test card: `4242 4242 4242 4242`, any future expiry, any CVC, any ZIP.
- Product checkout: open a product page → Buy Now → complete Checkout.
- Request checkout: create a custom request → Pay with Stripe → success/cancel pages.

## Running tests
```bash
python manage.py test
```

## Tech stack
- Django 6
- Stripe Checkout
- SQLite (dev)
- Vanilla JS for price preview

## Todo (remaining)
- Testing documentation
- Deployment instructions (Render/Heroku)
- Responsive polish & accessibility pass
