# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| profiles | profiles.html | ![screenshot](documentation/html-profiles-validation.png) | Pass: No Errors |
| accounts | signup.html | ![screenshot](documentation/html-signup-validation.png) | I am aware of this error from the validator and is happening due to allauth. I have attempted to remove it in the signup form however I was unable to fix it for that reason error will still show up in the validator. |
| checkout | checkout.html | ![screenshot](documentation/html-checkout-validation.png) | Pass: No Errors |
| contact | contact_form.html | ![screenshot](documentation/html-contact-validation.png) | Pass: No Errors |
| faq | faq.html | ![screenshot](documentation/faq-html-validation.png) | Pass: No Errors |
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

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Contact | Plans | FAQ | Profile | Edit Profile | Checkout | 404 Page | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/home-mobile.png) | ![screenshot](documentation/contact-mobile.png) | ![screenshot](documentation/plan-mobile.png) | ![screenshot](documentation/faq-mobile.png) | ![screenshot](documentation/profile-mobile.png) | ![screenshot](documentation/edit-profile-mobile.png) | ![screenshot](documentation/checkout-mobile.png) | ![screenshot](documentation/404-page-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/home-tablet.png) | ![screenshot](documentation/contact-tablet.png) | ![screenshot](documentation/plan-tablet.png) | ![screenshot](documentation/faq-tablet.png) | ![screenshot](documentation/profile-tablet.png) | ![screenshot](documentation/edit-profile-tablet.png) | ![screenshot](documentation/checkout-tablet.png) | ![screenshot](documentation/404-page-tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/homepage.png) | ![screenshot](documentation/contact.png) | ![screenshot](documentation/fitness-plan.png) | ![screenshot](documentation/faq-page.png) | ![screenshot](documentation/profile-page.png) | ![screenshot](documentation/edit-profile-page.png) | ![screenshot](documentation/checkout.png) | ![screenshot](documentation/404-page-edge.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | some minor warnings |
| Contact | ![screenshot](documentation/lighthouse-contact-mobile.png) | ![screenshot](documentation/lighthouse-contact-desktop.png) | some minor warnings |
| Plans | ![screenshot](documentation/lighthouse-plan-mobile.png) | ![screenshot](documentation/lighthouse-plan-desktop.png.png) | Some minor warnings |
| FAQ | ![screenshot](documentation/lighthouse-faq-mobile.png) | ![screenshot](documentation/lighthouse-plan-desktop.png) | Some minor warnings |
| Profile | ![screenshot](documentation/lighthouse-profile-mobile.png) | ![screenshot](documentation/lighthouse-profile-desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| All Pages | | | | | |
| | The footer should contain quick links, social media icons, and  copyright. | Checked the footer section. | The footer displayed all expected elements: quick links, and social media icon. | Test concluded and passed | ![screenshot](documentation/footer.png) |
| | Logo should be visible on the header. | Loaded the homepage. | The logo was displayed as expected in the header section. | Test concluded and passed. | ![screenshot](documentation/logo.png) |
| | Newsletter subscription form should accept input and provide feedback | Entered an email address in the newsletter form. | The form accepted the input, and feedback was provided upon submission. | Test concluded and passed. | ![screenshot](documentation/newsletter-success-message.png) |
| | Quick links should be visible and clickable in the footer. | Tested each quick link by clicking on it. | All quick links navigated to their respective pages correctly. | Test concluded and passed. | ![screenshot](documentation/quick-links.png) |
| | Responsive navigation should adjust for smaller screens with a toggle menu. | Resized the browser window to a smaller width. | The navigation adjusted and displayed a toggle menu correctly. | Test concluded and passed. | ![screenshot](documentation/mobile-navbar.png) |
| | Responsive navigation should expand to show links when the menu is toggled. | Clicked on the menu toggle. | The navigation expanded and displayed all links as expected. | Test concluded and passed. | ![screenshot](documentation/sidebar.png) |
| | Social media links should be visible and linked correctly in the footer. | Clicked on each social media icon. | Each icon correctly linked to the corresponding social media page. | Test concluded and passed. | ![screenshot](documentation/social-media-links.png) |
| | Navigation for unauthenticated users should show "Login" and "Register". | Logged out and viewed the home page. | The navigation correctly displayed "Login" and "Register" for unauthenticated users. | Test concluded and passed. | ![screenshot](documentation/unauthenticated-user.png) |
| Home | | | | | |
| | The Home Page section should display a clear, motivational message with an appropriate background. | Checked the section on page load. | The page displayed correctly with text and image. | Test concluded and passed. | ![screenshot](documentation/homepage.png) |
| | The 'Client Reviews' section should showcase client feedback with images and ratings. | Viewed client reviews on the homepage. | Client reviews displayed correctly with text, and star ratings as expected. | Test concluded and passed. | ![screenshot](documentation/review.png) |
| Plans | | | | | |
| | If the user is unauthenticated and clicks "Purchase," they should be redirected to the login page. | Tested by clicking "Purchase" as an unauthenticated user. | The user was redirected to the login page as expected. | Test concluded and passed. | ![screenshot](documentation/login-page.png) |
| | If the user is authenticated and clicks "Purchase," they should be redirected to the checkout page. | Tested by clicking "Purchase" as an authenticated user. | The user was redirected to the checkout page correctly. | Test concluded and passed. | ![screenshot](documentation/checkout.png) | 
| | If the user has already purchased a specific plan, the user gets a message when the user click on the plan saying you have already perchased this plan. displayed correctly as expected. | Test concluded and passed. | ![screenshot](documentation/already-purchased.png) |
| FAQ | | | | | |
| | The "Frequently Asked Questions" section should display a list of questions with expandable accordion items for each category. The questions should expand to show the answers when clicked. | Clicked on different FAQ categories and questions to expand them. | The FAQ section displayed correctly, showing answers upon clicking. | Test concluded and passed. | ![screenshot](documentation/faq-page.png) |
| Login | | | | | |
| | The login form should accept email and password inputs, have a "Remember Me" option, and provide links to "Forgot Password?" and "Sign up." | Tested the login form with valid and invalid credentials, and clicked on both links. | The form accepted inputs as expected. On invalid login, an error message was displayed; "Forgot Password?" and "Sign up" links redirected correctly. | Test concluded and passed. | ![screenshot](documentation/login-page.png) |
| | The "Sign up" link should redirect to the registration page. | Clicked the "Sign up" link. | The link redirected correctly to the registration page. | Test concluded and passed. | ![screenshot](documentation/signup-page.png) |
| | The "Update Personal Information" form should allow users to update their profile details, phone number, address, date of birth, current weight, height, and goal weight. The form should have "Save" and "Delete Account" buttons. | Tested updating various fields in the personal information form. | The form displayed all fields correctly, allowing the user to input or change data. The "Save" button was enabled, and the "Delete Account" button was visible. | Test concluded and passed. | ![screenshot](documentation/edit-profile-page.png) |
| 404 Page | | | | | |
| | When a user navigates to a non-existent URL within the site, a custom 404 error page should be displayed, providing a message and a "Back to Home" button. | Navigated to a wrong URL within the site to trigger the 404 page. | The 404 error page appeared correctly with a friendly message, and a "Back to Home" button that redirects to the homepage. | Test concluded and passed. | ![screenshot](documentation/404-page-edge.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a **new user** I can **create an account and signup with my email** so that ****I can access my dashboard**. | ![screenshot](documentation/signup-page.png) |
| As a **new user**, I want to **read success stories and testimonials** so that **I can trust the effectiveness of the coaching services.** | ![screenshot](documentation/review.png) |
| As a **new user**, I want to **be able to message for any queries I have before purchasing a plan**, so that I **can make an informed decision.** | ![screenshot](documentation/contact.png) |
| As a **new user**, I want to **be able to access a comprehensive FAQ section**, so that I **can quickly find answers to common questions about the platform and its services without needing to contact support.** | ![screenshot](documentation/faq-page.png) |
| As a **registered user**, I want to **update my profile information**, so that my **information remains accurate and relevant.** | ![screenshot](documentation/edit-profile-page.png) |
| As a **registered user**, I want to **securely pay for my selected training package using Stripe**, so that I can **access my plans and coaching services.** | ![screenshot](documentation/checkout.png) |
| As a **registered user**, I want to **contact my coach for support** so that I **can get help when I need it.** | ![screenshot](documentation/contact.png) |
| As a **registered user**, I want to **be able to reset my password if I forget it**, so that I **can regain access to my account securely.** | ![screenshot](documentation/password-reset.png) |
| As a **registered user**, I want to **receive a confirmation message after successfully purchasing a training plan**, so that I **know my payment was processed and I have access to the purchased plan.** | ![screenshot](documentation/payment-success-message.png) |
| As a **registered user**, I want to **be able to see which training plans I have already purchased**, so that I **don’t accidentally buy the same plan again.** | ![screenshot](documentation/order-history.png) |
| As a **new or registered user**, I want to **be able to subscribe to the newsletter**, so that I **can receive monthly updates about the latest news in the fitness world.** | ![screenshot](documentation/newsletter.png) |
| As a **registered user**, I want to **delete my profile**, so that **my personal information is no longer stored in the system.** | ![screenshot](documentation/delete-profile-page.png) |
| As a **registered user**, I want to **be able to add a new weight log entry**, so that **I can track my progress over time.** | ![screenshot](documentation/weight-log.png) |
| As an **admin**, I want to **create, manage and update plans** so that **users can see the up-to-date plans and services at the current time** | ![screenshot](documentation/admin-plan.png) |
| As an **admin**, I want to **view orders** so that **I can keep track of all payments made.** | ![screenshot](documentation/admin-order.png) |
| As a **site admin** I can **view and manage newsletter subscribers** so that I can send newsletter to all subscribers. | ![screenshot](documentation/admin-newsletter.png) |


|