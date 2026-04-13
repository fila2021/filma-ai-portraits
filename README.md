# Askuala AI Portraits

Full‑stack Django application for browsing, purchasing, and requesting AI‑generated portrait products and prompt bundles through a premium, responsive UI.

## 🎯 Purpose & Users
- **Purpose:** Provide a professional storefront for AI portrait products, prompt bundles, and custom portrait requests with clear e‑commerce and request tracking.
- **Target users:** Creators and individuals wanting ready-made AI portraits, prompt bundles, or personalised AI portrait services; non‑technical users who need a guided flow.

## 🚀 Features
- Shop: product listing, detail, wishlist, cart, Stripe checkout.
- Bundles: prompt bundles with cart/wishlist and pricing from admin.
- Services/Requests: submit and track custom portrait requests.
- Orders & Requests dashboards (table view) with bundle support.
- Reviews with star ratings.
- Auth: signup, login, logout, profile.
- UI/UX: dark/gold theme, centered hero CTAs, responsive layout.

## 🧠 UX Decisions
- Clear entry points on the hero (Shop / Bundles / Custom Request).
- Minimal-friction checkout; confirmation modals for cart actions.
- Table layouts for orders/requests for quick scanning.
- Empty/fallback states for missing data and images.
- Consistent typography and spacing across desktop/mobile.

## 🏗️ Data Model
- **User** (auth)
- **Product** (store items)
- **ServicePackage** (service offerings)
- **CustomRequest** (user submissions)
- **Order** (product or bundle purchases; bundle_label/count stored)
- **Review** (product or request feedback)
Relationships: User→Orders (1:m), User→CustomRequests (1:m), Product→Reviews (1:m).

## 🛠 Tech Stack
- Django 6, SQLite (dev) / PostgreSQL (Heroku)
- HTML, CSS, vanilla JS
- Stripe Checkout
- WhiteNoise for static files
- Deployment: Heroku

## ⚙️ Environment Variables
Set in `.env` (template provided) or Heroku config:
```
SECRET_KEY=
DEBUG=
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
DATABASE_URL=           # set by Heroku Postgres
ALLOWED_HOSTS=
```

## 💻 Local Setup
```bash
git clone <repo_url> filma-ai-portraits
cd filma-ai-portraits
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # fill values
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
Visit http://127.0.0.1:8000/

## 🌐 Deployment (Heroku)
```bash
heroku create askuala-ai
heroku addons:create heroku-postgresql:essential-0
heroku config:set SECRET_KEY=... DEBUG=False ALLOWED_HOSTS=askuala-ai.herokuapp.com \
  STRIPE_PUBLISHABLE_KEY=... STRIPE_SECRET_KEY=...
git push heroku main
heroku run -- python manage.py migrate
heroku run -- python manage.py createsuperuser
heroku run -- python manage.py collectstatic --noinput
heroku ps:restart
```

## 🧪 Testing & Validation
- Manual flows: auth, shop/cart, bundles, checkout (Stripe test), orders, requests, reviews, responsive.
- Validation tools planned: W3C HTML, Jigsaw CSS, flake8 (PEP8), browser console (desktop/mobile).
- Testing summary and screenshots are included in `TESTING.md` (Validation section), with supporting assets in `docs/testing/`.

## 🐞 Bugs & Fixes (notable)
- Duplicate `image_url` migration / nullability conflict → cleaned model, added migration, applied on Heroku.
- Review redirect failing for products → now routes to ID-based product detail.
- Bundles showing €0 in cart/checkout → now pull price/label from `PromptBundle` and hydrate carts.
- Orders for bundles missing → create bundle orders without product FK; updated templates to display bundle info.
- CSS not updating on Heroku → ensured WhiteNoise manifest storage, collectstatic, and cache-bust on stylesheet.
- Admin link needed separate tab → set `target="_blank"` for staff admin link.
- Stripe was bypassed / auto-paid fallback → Stripe now mandatory in production; missing keys show user error.
- DisallowedHost / 400 → ALLOWED_HOSTS set to Heroku domain via config vars.
- Service images not showing → render service cards with background-image when `image_url` is present.

## 📁 Structure
```
home/ accounts/ shop/ services/ payments/ reviews/ gallery/
templates/ static/
```

## 🔒 Security
- Secrets via env vars; DEBUG=False in production; ALLOWED_HOSTS set.
- CSRF protection enabled.
- WhiteNoise compressed manifest for static assets.

## 📈 Future Improvements
- Automated tests (pytest)
- Advanced product filtering/search
- Email notifications
- Admin analytics
- Improved review moderation

## 🙌 Credits
- Developed by Filmawit Gebreegziabher
- Django, Stripe, Heroku
Resources used:
- Django Documentation
- Code Institute learning materials
- Heroku Documentation
- Cloudinary Documentatio

Images and content used for educational purposes.

Project developed by the author as part of the backend development assessment.

Thank You for Visiting Askuala AI!

