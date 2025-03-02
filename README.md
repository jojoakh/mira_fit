# [Mira Fit](https://mira-fit-9ed22057d1a1.herokuapp.com/)

Welcome to Mira Fit, an innovative online platform designed to offer personalized fitness plans that users can follow from the comfort of their own home. It provides a seamless experience for fitness enthusiasts of all levels, offering comprehensive plans that are customized to fit individual needs, preferences, and goals. The platform will include a variety of features, including weight logging, and in-app purchases for premium plans.

### Mission 

To provide accessible, affordable, and tailored fitness solutions that empower individuals to take control of their health and wellness journey.

### Target Audience

- **Beginners**: Those who are just starting out in fitness and require a supportive community, clear instructions, and easy-to-follow plans to begin their health journey.
- **Fitness Enthusiasts**: Individuals who are dedicated to their fitness journey and seek structured workout plans and expert guidance to take their routines to the next level.
- **Busy Professionals**: People with a demanding lifestyle who need flexible and customized coaching options that can seamlessly fit into their daily routines.
- **Advance Trainers**: Experienced trainers looking to expand their reach and offer their services through an innovative online platform.

### Benefits 

- **Personalized Fitness Plans**: Mira Fit offers tailored workout plans that are designed to meet individual fitness goals, whether it's weight loss, muscle gain, or overall health improvement.

- **Progress Tracking**: Users can easily track their fitness progress over time, monitoring improvements in strength, endurance, and other key metrics to stay motivated.

- **Integrated Nutrition Guidance**: Mira Fit integrates with Essence Cuisine to provide users with meal plans that complement their fitness goals, making it easier to achieve results through both exercise and nutrition.

- **Flexibility and Convenience**: Whether you're at home, at the gym, or on the go, Mira Fit offers flexibility to workout anytime and anywhere, without the need for a fixed schedule.

![screenshot](documentation/responsive-mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://mira-fit-9ed22057d1a1.herokuapp.com/)

## UX

### Color Scheme


- `#f4f7fa` used throughout the site as the background colour.
- `#e91a66` used for buttons through out the site.
- `#a4104b` used as hover button.
- `#19011f` used all throughout the site, mainly for the navbar and footer.

I used [coolors.co](https://coolors.co/f4f7fa-e91a66-a4104b-19011f) to generate my colour palette

![screenshot](documentation/colour-palette.png)

### Typography

- [Font Awesome](https://fontawesome.com) icons were used for the social media icons in the footer.

## User Stories

### New Site Users

- As a **new user**, I want to **be able to create a new account with my personal information**, so that **I can access fitness plans and track my progress**.

- As a **new user**, I want to **browse available fitness plans with descriptions and prices**, so that **I can choose the best plan for my goals**.

- As a **new user**, I want to **read reviews and testimonials from other users**, so that **I can trust the effectiveness of the plans**.

- As a **new user**, I want to **be able to access a comprehensive FAQ section**, so that **I can quickly find answers to common questions about the platform and its services without needing to contact support**.

- As a **new user**, I want to **subscribe to the newsletter**, so that **I can receive fitness tips, updates, and promotions via email**.

- As a **new user**, I want to **be able to contact customer support through a contact page**, so that **I can ask questions or report any issues I encounter on the site**.


### Registered Site Users

- As a **registered user**, I want to **update my profile information**, so that **my information remains accurate and up to date**.

- As a **registered user**, I want to **securely pay for my selected fitness plan using Stripe**, so that **I can start using my purchased plan immediately**.

- As a **registered user**, I want to **see a confirmation message after successfully purchasing a plan**, so that **I know my payment was processed and I have access to the purchased plan**.

- As a **registered user**, I want to **view my order history**, so that **I can keep track of my purchases and know which plans I have access to**.

- As a **registered user**, I want to **be prevented from repurchasing a plan I have already bought**, so that **I do not accidentally pay twice for the same plan**.

- As a **registered user**, I want to **log my weight over time**, so that **I can track my fitness progress and stay motivated****.

- As a **registered user**, I want to **see my past weight logs in a history section**, so that **I can analyze my progress over time**.

- As a **registered user**, I want to **delete my account if I no longer wish to use the platform**, so that **my personal information and purchase history are removed from the system**.

As a **registered user**, I want to **contact customer support through the contact page**, so that **I can ask for help if I have any issues with my account or purchases**.

### Admin Users

- As an**admin**, I want to **manage user's newsletter subscriptions,** so that **I can ensure only subscribed users receive newsletters and promotions**.

- As an **admin**, I want to **view a list of all purchases made by users,** so that **I can analyze sales and revenue**.

- As an **admin**, I want to **integrate Stripe for handling payments** so that **users can pay for plans and make payments securely**.
- As an **admin**, I want to **create, manage and edit and delete plans** so that ****users can see the up-to-date plans and services at the current time**.

- As an **admin**, I want to **receive and manage user inquiries from the contact page**, so that **I can respond to questions or issues reported by users**.

## Wireframes

| Page | Desktop | 
| --- | --- |
| Home | ![screenshot](documentation/homepage-wireframe.png) | 
| Contact | ![screenshot](documentation/contact-page-wireframe.png) |
| Plan | ![screenshot](documentation/fitness-plan-wireframe.png) | 
| Signup | ![screenshot](documentation/signup-wireframe.png) | 
| Login | ![screenshot](documentation/login-wireframe.png) |  
| Profile | ![screenshot](documentation/profile-wireframe.png) | 

## Features

There are many features on the website which are easy to follow and navigate, creating a nice user experience.

### Existing Features

#### Navbar & Sidebar

- **Navbar**
    - The navigation bar is prominently displayed on every page, improving the user experience by offering easy access to all sections of the website and boosting the visibility of important pages.

![screenshot](documentation/navbar.png)

- **Sidebar**
    - Mobile users, will have access to the *sidebar*, this provides the same benefits as the navigation bar allowing users to easily access all pages of the site on mobile devices.

![screenshot](documentation/sidebar.png)

#### Footer

- **Quick Links Section**
    - The footer includes prominent social media links, allowing users to connect with Mira Fit across multiple platforms like Facebook, Instagram, Twitter, LinkedIn, and YouTube. This integration helps build a community around the brand and keeps users engaged with the latest updates and content from Mira Fit.

![screenshot](documentation/quick-links.png)

- **Social Media Link**
    - A quick links section in the footer provides easy access to the most important pages on the site. This section is especially useful for users who may need to quickly navigate to another part of the site without returning to the top of the page.

![screenshot](documentation/social-media-links.png)

#### Home Page

 - **Home**

    - **Home Image**: The homepage features a captivating image of women working out with a welcome to Mira Fit message, it is the first thing users see when they visit the site. showing the users what the site is all about.

![screenshot](documentation/homepage.png)

   - **About Us**:  This section explains what the site is about, what we offer, our personalized plan, supportive community, and our help for users to track their progress and set personal goals. 

![screenshot](documentation/about-us.png)
![screenshot](documentation/what-we-offer.png)

- **Client Reviews**: The Client Reviews section features testimonials from satisfied clients, which are essential for building social proof, and each review is accompanied by a star rating.

![screenshot](documentation/review.png)

- **Newsletter Section**:
 This section has a newsletter subscription form which is a valuable tool for maintaining communication with users. By subscribing, users receive monthly updates on fitness trends, promotions, and news. This feature is crucial for user retention and driving ongoing engagement.

![screenshot](documentation/newsletter.png)


#### Fitness Plan Page

- The Fitness Plan Page presents the different packages available, each with a clear breakdown of what’s included and the associated cost. This section is designed to help users easily compare the options and choose the one that best fits their needs. The use of distinct cards for each plan, along with prominent pricing, makes this information easy to digest.

![screenshot](documentation/fitness-plan.png)

#### Contact Page

- The Contact page section invites users to get in touch for more information or inquiries, with a link to check out FAQ section for common questions before filling the contact form. This section is designed to facilitate easy communication between potential clients and Mira Fit, enhancing the user experience by providing a straightforward way to ask questions.

![screenshot](documentation/contact.png)

    
    