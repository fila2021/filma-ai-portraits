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

## User stories (abbreviated)
- As a visitor, I can browse gallery images and shop packs without logging in.
- As a user, I can sign up, log in, and edit my profile.
- As a customer, I can create, view, edit, and delete custom requests with clear feedback.
- As a customer, I can buy a product pack and see order/payment status.
- As a customer, I can pay for a custom request via Stripe Checkout.
- As a customer, I can leave, edit, or delete reviews on products or my requests.

## Database schema (summary)
- accounts.Profile (1–1 User): display_name, bio, instagram_handle.
- gallery.GalleryImage: title, image_url, category, caption, is_featured.
- shop.Product: title, slug, description, price, image_url, is_active.
- services.ServicePackage: name, description, base_price, number_of_images, turnaround_days, platform_type, is_active.
- services.CustomRequest: user FK, package FK, platform_type, style_choice, prompt_details, extra_notes, total_price, status, timestamps.
- payments.Order: user FK, product FK, price_snapshot, status, stripe_session_id, timestamps.
- payments.Payment: user FK, optional order/custom_request, amount, currency, status, stripe_payment_intent/session_id, paid_at, timestamps.
- reviews.Review: user FK, optional product/custom_request FK, rating, comment, created_at.

## Deployment (example: Render)
1. Set env vars: `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=<your-domain>`.
2. Add build command: `pip install -r requirements.txt`.
3. Add start command: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn filma_ai_portraits.wsgi:application`.
4. Use persistent SQLite or switch to Postgres (preferred) and set `DATABASE_URL`.
5. Verify Stripe webhooks if you add them; otherwise test Checkout with test card.

### Postgres (recommended)
- Install `psycopg2-binary` or `psycopg` in production.
- Set `DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME`.
- Use `django-environ` or `dj-database-url` (optional) to parse; or configure `DATABASES` manually in settings.

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
