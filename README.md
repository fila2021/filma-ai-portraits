# Askuala AI Portraits

Django storefront for AI-generated portrait products, prompt bundles, and custom portrait requests. Users can browse, buy, submit briefs, manage orders/requests, and leave reviews in a polished dark/gold UI.

## Features
- Home hero with clear CTAs (browse, bundles, custom request)
- Shop (products) + Bundles (prompt bundles) + Wishlist + Cart with Stripe checkout
- Services with custom request flow
- Orders and Requests dashboards (table view)
- Reviews with star ratings
- Auth (signup/login/logout/profile)
- Dark/light theme toggle
- Responsive layout (desktop, tablet, mobile)

## Tech Stack
- Django 6, SQLite (dev), Stripe Checkout
- HTML, CSS, vanilla JS (no build step)
- Deployed via Heroku (dyno + staticfiles)

## Environment Variables
Create a `.env` (or set in Heroku config):
- `SECRET_KEY` – Django secret key
- `DEBUG` – `True/False`
- `STRIPE_PUBLISHABLE_KEY` – your Stripe publishable key
- `STRIPE_SECRET_KEY` – your Stripe secret key
- `DATABASE_URL` – optional (Heroku Postgres)

## Local Setup
```bash
git clone <repo_url> filma-ai-portraits
cd filma-ai-portraits
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # or create manually with vars above
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
Visit http://127.0.0.1:8000/

## Key URLs
- `/` home
- `/browse/` combined shop + services
- `/bundles/` prompt bundles
- `/shop/` products
- `/cart/`, `/wishlist/`
- `/services/`, `/requests/`
- `/orders/`
- `/accounts/login/`, `/accounts/signup/`
- `/admin/` (staff only)

## Deployment (Heroku)
1. Create app, add Postgres addon.
2. Config Vars: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=<heroku-domain>`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`, `DATABASE_URL`.
3. Files: `Procfile`, `requirements.txt`, `runtime.txt` (if needed).
4. Push code: `git push heroku main`
5. Run: `heroku run python manage.py migrate`
6. Create admin: `heroku run python manage.py createsuperuser`
7. Collect static (Heroku handles via whitenoise/staticfiles on deploy).

## Validation Plan (keep updated)
- HTML: https://validator.w3.org/ — check home, browse, shop/product detail, bundles, cart, checkout success/cancel, requests, orders, reviews after final build.
- CSS: https://jigsaw.w3.org/css-validator/
- Python: `flake8` (PEP8). Do not claim “0 issues” unless run.
- Browser console: check all key pages on desktop & mobile; ensure no missing assets/404s or JS errors.
Record findings in `TESTING.md` (Validation section) with screenshots/notes. Mention any acceptable warnings.

## Testing (manual checklist)
- Auth: signup / login / logout / profile update
- Shop: list, product detail, add to cart, wishlist toggle
- Bundles: add to cart/wishlist, checkout (Stripe session), price shown
- Cart: update qty, remove, clear, confirmation modals
- Checkout: success, cancel, receipts, orders created
- Orders: list (table), detail (product or bundle)
- Services/Requests: list, create request, view/edit if allowed
- Reviews: add review, star rating display
- Theme toggle: dark/light persistence
- Responsive: home, browse, shop, cart, checkout, orders (mobile widths)

Record outcomes and screenshots in `/docs/testing/` (add images) and link them in README when finalized.

## Known Areas to Monitor
- Stripe keys must be set in env; missing keys fallback to non-Stripe flow.
- Product `image_url` should be populated for best display; placeholders used otherwise.
- If adding new migrations, run `python manage.py migrate` locally and on Heroku.

## Credits / Attribution
- All custom Django/JS/CSS written by the project author.
- Icons/illustrations from project assets; replace with licensed media as needed.
- Cite any external snippets/tutorials directly in code comments and here when added.
