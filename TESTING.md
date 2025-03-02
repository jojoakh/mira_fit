# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| about | about.html | ![screenshot](documentation/testing/validation/html/html-validation-about.png) | Pass: No Errors |
| accounts | add_weight_log.html | ![screenshot](documentation/testing/validation/html/html-validation-add-weight-log.png) | Pass: No Errors |
| accounts | edit_profile.html | ![screenshot](documentation/testing/validation/html/html-validation-profile-edit.png) | Pass: No Errors |
| accounts | edit_weight_log.html | ![screenshot](documentation/testing/validation/html/html-validation-edit-weight-log.png) | Pass: No Errors |
| accounts | profile.html | ![screenshot](documentation/testing/validation/html/html-validation-profile.png) | Pass: No Errors |
| accounts | signup.html | ![screenshot](documentation/testing/validation/html/html-validation-signup.png) | I am aware of this error from the validator and is happening due to allauth. I have attempted to remove the `aria-describedby` in the signup form however I was unable to fix it for that reason error will still show up in the validator. |
| checkout | checkout.html | ![screenshot](documentation/testing/validation/html/html-validation-checkout.png) | Pass: No Errors |
| checkout | checkout_success.html | ![screenshot](documentation/testing/validation/html/html-validation-checkout-success.png) | Pass: No Errors |
| contact | contact_form.html | ![screenshot](documentation/testing/validation/html/html-validation-home.png) | Pass: No Errors - Contact form is on every page. |
| faq | faq.html | ![screenshot](documentation/testing/validation/html/html-validation-faq.png) | Pass: No Errors |
| home | home.html | ![screenshot](documentation/testing/validation/html/html-validation-home.png) | Pass: No Errors |
| plans | plans.html | ![screenshot](documentation/testing/validation/html/html-validation-plans.png) | Pass: No Errors |
| | logout.html | ![screenshot](documentation/testing/validation/html/html-validation-logout.png) | Pass: No Errors |
| | login.html | ![screenshot](documentation/testing/validation/html/html-validation-login.png) | Pass: No Errors |
| | password_reset.html | ![screenshot](documentation/testing/validation/html/html-validation-password-reset.png) | Pass: No Errors |
| | password_reset_done.html | ![screenshot](documentation/testing/validation/html/html-validation-password-reset-done.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/checkout-css-validation.png) | Pass: No Errors |
| profiles | profiles.css | ![screenshot](documentation/profiles-css-validation.png) | Pass: No Errors |
| static | style.css | ![screenshot](documentation/style-css-validation.png) | Pass: No Errors |
