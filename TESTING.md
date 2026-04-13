# Testing

Record manual test results here. Use this table format:

| Feature | Action | Expected | Actual | Pass/Fail | Notes |
| --- | --- | --- | --- | --- | --- |
| Signup | Fill form and submit | Account created, redirected to login |  |  |  |
| Login/Logout | Login then logout | User session starts/stops | Pass |  |  |
| Profile edit | Update bio | Changes saved, message shown | Pass |  |  |
| Gallery | Visit /gallery | Images list renders |  |  |  |
| Shop list/detail | View product | Product info loads |  |  |  |
| Product checkout | Buy Now with test card | Redirect to Stripe, success page, order paid | Pass |  |  |
| Services create | Submit custom request | Request created, success page | Pass |  |  |
| Services edit/delete | Edit then delete | Updates applied; deletion removes item | Pass |  |  |
| Reviews (product) | Add/edit/delete review | Review appears/updates/disappears | Pass |  |  |
| Reviews (request) | Add/edit/delete review | Review appears/updates/disappears | Pass |  |  |
| Request payment | Pay for request | Stripe success page, request marked completed | Pass |  |  |
| Responsive check | Resize to mobile | Layout remains readable |  |  |  |

## Validation
- HTML (W3C): pages checked: home, browse, shop detail, bundles, cart, checkout success/cancel, orders, requests, reviews.  
  Findings:  
  -  
- CSS (Jigsaw):  
  Findings:  
  -  
- Python (flake8):  
  Findings:  
  -  
- Browser console (Chrome/Firefox, desktop & mobile):  
  Findings:  
  -  

## Bugs and fixes

List issues found and resolutions:
- Bug: …
  - Fix: …

## Remaining known issues
- …
