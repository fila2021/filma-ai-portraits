# Deployment Guide — Askuala AI Portraits

## 1) Production settings
- In `filma_ai_portraits/settings.py`: set `DEBUG = False` and add your domain to `ALLOWED_HOSTS`.
- Do **not** commit secrets; use environment variables (`.env` locally, config vars on Heroku).

## 2) Environment variables
Set these in Heroku config (and locally via `.env`):
- `SECRET_KEY`
- `DEBUG` (False on Heroku)
- `ALLOWED_HOSTS` (your Heroku domain)
- `STRIPE_PUBLISHABLE_KEY`
- `STRIPE_SECRET_KEY`
- `DATABASE_URL` (from Heroku Postgres)

## 3) Prepare the app
```
pip install -r requirements.txt
python3 manage.py collectstatic --noinput   # Heroku runs this automatically
python3 manage.py migrate
python3 manage.py createsuperuser
```

## 4) Heroku steps
1. Create the app: `heroku create askuala-portraits`
2. Add Postgres: `heroku addons:create heroku-postgresql:hobby-dev`
3. Set config vars (see above).
4. Push code: `git push heroku main`
5. Run migrations: `heroku run python3 manage.py migrate`
6. Create admin: `heroku run python3 manage.py createsuperuser`
7. Open: `heroku open`

## 5) Stripe test checkout
- Use Stripe test keys.
- Test card: `4242 4242 4242 4242`, any future expiry, any CVC, any ZIP.
- Verify: success page shows orders paid; order list shows the new order.

## 6) Post-deploy checklist
- Verify static assets load (no 404s in console).
- Check key pages: home, browse, shop detail, bundles, cart, checkout, success/cancel, orders, requests, reviews.
- Confirm HTTPS redirect (Heroku handles via router).
- Confirm `DEBUG=False` and `ALLOWED_HOSTS` set.

## 7) Local run (quick)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # fill keys
python3 manage.py migrate
python3 manage.py runserver
```

Document any deviations or remaining warnings in README/TESTING before submission.
