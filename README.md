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

### 404 Page

- The 404 page informs users that the requested page is not found and provides navigation options to return to the home page. This enhances site usability by preventing dead ends and guiding users back to functional areas, ensuring a smooth browsing experience.

	![screenshot](documentation/404-error.png)

#### Fitness Plan Page

- The Fitness Plan Page presents the different packages available, each with a clear breakdown of what’s included and the associated cost. This section is designed to help users easily compare the options and choose the one that best fits their needs. The use of distinct cards for each plan, along with prominent pricing, makes this information easy to digest.

![screenshot](documentation/fitness-plan.png)

#### Contact Page

- The Contact page section invites users to get in touch for more information or inquiries, with a link to check out FAQ section for common questions before filling the contact form. This section is designed to facilitate easy communication between potential clients and Mira Fit, enhancing the user experience by providing a straightforward way to ask questions.

![screenshot](documentation/contact.png)

#### FAQ Page

- The FAQ section is designed with an accordion layout, which organizes frequently asked questions into expandable panels. This structure makes it easy for users to find answers to their specific questions without having to scroll through long blocks of text. The accordion is divided into multiple categories.

![screenshot](documentation/faq-page.png)


#### Profile Page

- **User Profile Overview**

	- The profile page provides a comprehensive overview of the user's personal information and fitness metrics. It includes sections for personal information, weight log, and order history.
    	![screenshot](documentation/profile-page.png)

- **Edit Profile Page and delete**

	- The profile edit page allows users to manage and update their personal information, making it easy for users to keep their profiles up-to-date. It includes essential functionalities like secure data handling, navigation back to the profile overview, and an option to delete the account, giving users full control over their personal data.

		![screenshot](documentation/edit-profile-page.png)
        ![screenshot](documentation/delete-profile-page.png)

#### Registration Section

- **Sign up Form**
	- The sign-up form provides a comprehensive and user-friendly registration experience for new users. 

		![screenshot](documentation/signup-page.png)

- **Email Verification**

	- After a sign up an email is sent to the user for email verification with instructs on how to verify their email to finalize the registration process.

	![screenshot](documentation/email-verification.png)

- **Login Form**

	- The login form is designed to provide a seamless and user-friendly experience for users trying to access their accounts. 

	![screenshot](documentation/login-page.png)

- **Reset Password Form**

	- The password reset form allows users to securely reset their passwords if they have forgotten them. It features a clean and straightforward interface, requiring only the user's email address to initiate the password reset process.then the user gets an email with steps on how to reset their password.

	![screenshot](documentation/password-reset.png)
    ![screenshot](documentation/change-password-page.png)
    ![screenshot](documentation/password-changed.png) 

### Checkout

- **Checkout Page**

	- The checkout page provides a streamlined and user-friendly interface for completing purchases. It features two main sections: "Checkout Details" and "Order Summary." In the "Checkout Details" section, users can enter their personal and payment information, including their fullname, email, phone number, and credit card details. The "Order Summary" section displays a clear breakdown of the selected training plan, its description, and the total cost, ensuring transparency and accuracy before finalizing the payment. This layout ensures a smooth and efficient checkout process, enhancing the overall user experience.

	![screenshot](documentation/checkout.png)

- **Payment Successful**

	- The payment successful page confirms the completion of a user's purchase in a clear and reassuring manner. It features a confirmation message that thanks the user for their purchase and notifies them that a confirmation email has been sent to their specified email address. Below the confirmation, the "Purchase Details" section provides specific information about the purchased training plan, including the order number, plan name, access details, name, and email. 

	![screenshot](documentation/payment-success-message.png)

### Future Features

- **Live Chat With Trainers**
 
    - The Live Chat with Trainers feature will provide users with real-time access to fitness experts, creating a more interactive and engaging experience. This functionality will allow users to ask questions directly to trainers, receive instant feedback on their workout plans, and get personalized advice tailored to their fitness goals.

- **Forum or Community Section** 

    - The Forum or Community Section will serve as a dedicated space where users can interact, learn, and share their fitness journeys. It will allow users to ask fitness-related questions, and share personal experiences. The platform will encourage discussions on various topics, including diet, exercise routines, and motivation strategies, helping users stay engaged and informed.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed   site.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
- [![Logo](https://img.shields.io/badge/Logo-grey?logo=google-chrome&logoColor=24aae3)](https://logo.com/) used to create the logo for the website.
- [![Mermaid](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://www.mermaidchart.com/) used for creating ERD diagrams.
- [![Djecrety](https://img.shields.io/badge/Djecrety-grey?logo=djecrety&logoColor=FF3670)](https://djecrety.ir/) tool used for generating django secret keys.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=balsamiq&logoColor=000000)](https://balsamiq.com/) used to create wireframes in early development.

### Database Schema

Below is the database schema for the **Mira Fit** project.

I have used [mermaidchart](https://www.mermaidchart.com/) to generate an ERD.

```mermaid
erDiagram
    USER {
        int id
        string full_name
        string email
        string password
    }

    PROFILE {
        int id
        int user_id
        string phone
        string gender
        date date_of_birth
        float height
        float weight
        float goal_weight
    }

    PLAN {
        int id
        string name
        float price
        text description
    }

    ORDER {
        int id
        int user_id
        int plan_id
        string order_number
        float amount
        date created_at
    }

    WEIGHTLOG {
        int id
        int user_id
        date entry_date
        float weight
    }

    REVIEW {
        int id
        int user_id
        int plan_id
        int rating
        text comment
        date created_at
    }

    SUBSCRIPTION {
        int id
        int user_id
        int plan_id
        string status
        date start_date
        date end_date
    }

    CONTACT {
        int id
        string name
        string email
        string subject
        text message
        date created_at
    }

    NEWSLETTER_SUBSCRIPTION {
        int id
        string email
        date subscribed_at
    }

    USER ||--o{ PROFILE : has
    USER ||--o{ ORDER : places
    PLAN ||--o{ ORDER : includes
    USER ||--o{ WEIGHTLOG : logs
    USER ||--o{ REVIEW : writes
    PLAN ||--o{ REVIEW : receives
    USER ||--o{ SUBSCRIPTION : subscribes 
    PLAN ||--o{ SUBSCRIPTION : offers
```

### Agile Development Process

#### GitHub Projects

[GitHub Projects](https://github.com/jojoakh/mira_fit/projects?query=is%3Aopen) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

![screenshot](documentation/github-projects.png)

#### GitHub Issues

[GitHub Issues](https://github.com/jojoakh/mira_fit/issues?q=is%3Aissue%20state%3Aclosed) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

![screenshot](documentation/github-issues.png)

#### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

### Ecommerce Business Model
This website operates on a Business-to-Customer (B2C) model, selling products directly to individual customers. The platform follows a straightforward B2C approach, focusing on one-time purchases rather than subscription-based services.

Currently, the site is in its early development phase, but it already includes features such as a newsletter subscription and social media integration to enhance marketing efforts.

Leveraging social media platforms like Facebook can help foster a community of engaged users while increasing site traffic and brand awareness. Similarly, the newsletter feature allows the business to send updates, including special offers, new product arrivals, changes in business hours, upcoming events, and other essential announcements to its audience.

These strategies help strengthen customer engagement, boost sales, and ensure users stay informed about the latest developments.

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://ci-jb-fit-73ac55dce174.herokuapp.com/

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://mira-fit-9ed22057d1a1.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a Facebook business account.

![screenshot](documentation/facebook-page.png)
![screenshot](documentation/facebook-page-two.png)

### Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://ci-jb-fit-73ac55dce174.herokuapp.com/).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]  
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store static files and images online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-peak-performance` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-peak-performance` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for peak-performance static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-peak-performance".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-peak-performance") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-peak-performance` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-peak-performance`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://jb-ci-boutique-ado-0fd50c244260.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or peak-performance
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | profile page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Bootstrap](https://getbootstrap.com/docs/5.2/components/accordion/) | FAQ page | interactive accordion |
| [Fitness Planner](https://www.fitnessmealplanner.com/) | entire page | used as inspiration when building the website. |
| [Chart](https://www.chartjs.org/docs/latest/) | profile page | helpful chart tool used to visual weight progress. |
| [GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | readme | implementing the ERD diagram |
| [Code Institute](https://codeinstitute.net/se/) |  entire page | Inspiration from boutique ado project |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com/photo/group-of-women-doing-work-out-863926/) | home | image | background |
| [Flaticon](https://www.flaticon.com/free-icon/monitoring-app_17974198?term=track+fitness+progress&page=1&position=4&origin=search&related_id=17974198) | home page | image | Progress icon |
| [Flaticon](https://www.flaticon.com/free-icon/setting_14963021?term=goal+setting&page=1&position=39&origin=search&related_id=14963021) | home page | image | personalization icon |
| [Flaticon](https://www.flaticon.com/free-icon/supporting_12370055?term=community+support&page=1&position=29&origin=search&related_id=12370055) | home page | image | Community icon |
| [Font Awesome](https://fontawesome.com/icons/youtube?f=brands&s=solid) | footer | image | youtube icon |
| [Font Awesome](https://fontawesome.com/icons/instagram?f=brands&s=solid) | footer | image | Instagram icon |
| [Font Awesome](https://fontawesome.com/icons/x-twitter?f=brands&s=solid) | footer | image | Twitter icon |
| [Font Awesome](https://fontawesome.com/icons/facebook?f=brands&s=solid) | footer | image | Facebook icon |
| [Font Awesome](https://fontawesome.com/icons/linkedin?f=brands&s=solid) | footer | image | Linkedin icon |



### Acknowledgement

- I would like to thank my lovely husband for being there all the time i needed his help and for supporting me to take this step into software development.
- I would like to thank my mentor, **Rory Patrick Sheridan** for his support throughout the development of this project.

    