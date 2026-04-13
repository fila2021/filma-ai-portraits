# Testing — Askuala AI Portraits

## Manual Test Matrix

| Feature | Action | Expected | Actual | Pass/Fail | Notes |
| --- | --- | --- | --- | --- | --- |
| Auth | Signup/Login/Logout | Session starts/stops, redirects correct |  |  |  |
| Profile | Update profile | Data saved, success message |  |  |  |
| Products | List & detail | Products render, pricing visible |  |  |  |
| Wishlist | Add/remove | Heart toggles, persists in session |  |  |  |
| Cart | Add/update/remove/clear | Quantities update, totals correct |  |  |  |
| Checkout | Stripe test payment | Redirect to Stripe, pay, return success |  |  |  |
| Bundles | Add to cart/wishlist | Bundle price from admin, totals correct |  |  |  |
| Orders | View list/detail/receipt | Paid orders show status, receipt link |  |  |  |
| Requests | Create/view/edit/delete | Request stored, status shown |  |  |  |
| Reviews | Add product review | Review saved, shows on product |  |  |  |
| Theme | Toggle dark/light | Persists across pages |  |  |  |
| Responsive | Mobile widths | Layout remains readable |  |  |  |

## Validation
- **HTML:** W3C Validator (home, browse, shop detail, bundles, cart, checkout success/cancel, orders, requests, reviews)  
  Findings:  
  -  
- **CSS:** Jigsaw Validator  
  Findings:  
  -  
- **Python:** `flake8` (PEP8)  
  Findings: (run locally; record any warnings)  
  -  
- **Browser console:** Chrome/Firefox desktop & mobile  
  Findings:  
  -  

## Bugs & Fixes (testing phase)
List issues found during testing and how they were resolved:
- Issue:  
  - Fix:  

## Known Issues
- Stripe required in production; checkout blocked if keys missing.
- No automated test suite yet; manual testing recorded here.

## Screenshots
Place validation/test screenshots in `docs/testing/` and reference them here.
