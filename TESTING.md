# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| profiles | profiles.html | ![screenshot](documentation/html-profiles-validation.png) | Pass: No Errors |
| accounts | signup.html | ![screenshot](documentation/testing/validation/html/html-validation-signup.png) | I am aware of this error from the validator and is happening due to allauth. I have attempted to remove the `aria-describedby` in the signup form however I was unable to fix it for that reason error will still show up in the validator. |
| checkout | checkout.html | ![screenshot](documentation/html-checkout-validation.png) | Pass: No Errors |
| contact | contact_form.html | ![screenshot](documentation/html-contact-validation.png) | Pass: No Errors |
| faq | faq.html | ![screenshot](documentation/testing/validation/html/html-validation-faq.png) | Pass: No Errors |
| home | home.html | ![screenshot](documentation/testing/validation/html/html-validation-home.png) | Pass: No Errors |
| plans | plans.html | ![screenshot](documentation/html-plans-validation.png) | Pass: No Errors |
|accounts | login.html | ![screenshot](documentation/html-login-validation.png) | Pass: No Errors |
| home | review.html | ![screenshot](documentation/html-review-validation.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/checkout-css-validation.png) | Pass: No Errors |
| profiles | profiles.css | ![screenshot](documentation/profiles-css-validation.png) | Pass: No Errors |
| static | style.css | ![screenshot](documentation/style-css-validation.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |

| checkout/js | stripe_elements.js | ![screenshot](documentation/js-stripe-element-validation.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| profiles | urls.py | ![screenshot](documentation/profile-urls-pep8-validation.png) | Pass: No Errors |
| profiles | views.py | ![screenshot](documentation/profile-views-pep8-validation.png) | Pass: No Errors |
| profiles | admin.py | ![screenshot](documentation/profile-admin-pep8-validation.png) | Pass: No Errors |
| profiles | signal.py | ![screenshot](documentation/profile-signals-pep8-validation.png) | Pass: No Errors |
| profiles | models.py | ![screenshot](documentation/profile-model-pep8-validation.png) | Pass: No Errors |
| profiles | forms.py |  ![screenshot](documentation/profile-form-pep8-validation.png) | Pass: No Errors |
| home | urls.py | ![screenshot](documentation/home-urls-pep8-validation.png) | Pass: No Errors |
| home | views.py | ![screenshot](documentation/home-view-pep8-validation.png) | Pass: No Errors |
| home | admin.py | ![screenshot](documentation/home-admin-pep8-validation.png) | Pass: No Errors |
| home | context_processors.py | ![screenshot](documentation/home-context-processors-pep8-validation.png) | Pass: No Errors |
| home | models.py | ![screenshot](documentation/home-models-pep8-validation.png) | Pass: No Errors |
| home | forms.py |  ![screenshot](documentation/home-view-pep8-validation.png) | Pass: No Errors |
| checkout | forms.py | ![screenshot](documentation/checkout-form-pep8-validation.png) | Pass: No Errors |
| checkout | models.py | ![screenshot](documentation/checkout-model-pep8-validation.png) | Pass: No Errors |
| checkout | forms.py | ![screenshot](documentation/checkout-form-pep8-validation.png) | Pass: No Errors |
| checkout | models.py | ![screenshot](documentation/checkout-model-pep8-validation.png) | Pass: No Errors |
| checkout | urls.py | ![screenshot](documentation/checkout-urls-pep8-validation.png) | Pass: No Errors |
| checkout | views.py | ![screenshot](documentation/checkout-view-pep8-validation.png) | Pass: No Errors |
| checkout | admin.py | ![screenshot](documentation/checkout-admin-pep8-validation.png) | Pass: No Errors |
| contact | forms.py | ![screenshot](documentation/contact-form-pep8-validation.png) | Pass: No Errors |
| contact | models.py | ![screenshot](documentation/contact-model-pep8-validation.png) | Pass: No Errors |
| contact | urls.py | ![screenshot](documentation/contact-url-pep8-validation.png) | Pass: No Errors |
| contact | views.py | ![screenshot](documentation/contact-view-pep8-validation.png) | Pass: No Errors |
| contact | admin.py | ![screenshot](documentation/contact-admin-pep8-validation.png) | Pass: No Errors |
|  | custom_storages.py | ![screenshot](documentation/custom-storage-pep8-validation.png) | Pass: No Errors |
| faq | urls.py | ![screenshot](documentation/faq-urls-pep8-validation.png) | Pass: No Errors |
| faq | views.py | ![screenshot](documentation/faq-view-pep8-validation.png) | Pass: No Errors |
| mira_fit | settings.py | ![screenshot](documentation/settings-pep8-validation.png) | Pass: No Errors |
| mira_fit | urls.py | ![screenshot](documentation/mira-fit-urls-pep8-validation.png) | Pass: No Errors |
| mira_fit | views.py | ![screenshot](documentation/mira-fit-views-pep8-validation.png) | Pass: No Errors |
|  | manage.py | ![screenshot](documentation/manage-pep8-validation.png) | Pass: No Errors |
| plan | admin.py  | ![screenshot](documentation/plan-admin-pep8-validation.png) | Pass: No Errors |
| plans | models.py | ![screenshot](documentation/plan-model-pep8-validation.png) | Pass: No Errors |
| plans | urls.py | ![screenshot](documentation/plan-urls-pep8-validation.png) | Pass: No Errors |
| plans | views.py | ![screenshot](documentation/plan-views-pep8-validation.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Plans | FAQ | Profile | Edit Profile | Logout | Login | Register | Checkout | Checkout Success | 404 Page | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/homepage.png) | ![screenshot](documentation/fitness-plan.png) | ![screenshot](documentation/faq-page.png) | ![screenshot](documentation/profile-page.png) | ![screenshot](documentation/edit-profile-page.png) | ![screenshot](documentation/sign-out.png) | ![screenshot](documentation/login-page.png) | ![screenshot](documentation/signup-page.png) | ![screenshot](documentation/checkout.png) | ![screenshot](documentation/payment-success-message.png) | ![screenshot](documentation/404-error.png) | Works as expected |
| Edge | ![screenshot](documentation/homepage-edge.png) | ![screenshot](documentation/plan-page-edge.png) | ![screenshot](documentation/faq-edge.png) | ![screenshot](documentation/profile-edge.png) | ![screenshot](documentation/edit-profile-edge.png) | ![screenshot](documentation/sign-out.png) | ![screenshot](documentation/login-edge.png) | ![screenshot](documentation/signup-edge.png) | ![screenshot](documentation/checkout-edge.png) | ![screenshot](documentation/payment-success-message.png) | ![screenshot](documentation/404-page-edge.png) | Works as expected |




