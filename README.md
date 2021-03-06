<div align="center">
<h1>True Essence </h1>
<img src="https://i.ibb.co/3Mvxtp2/about-us1.jpg"  href="https://.herokuapp.com/" target="_blank" rel="noopener" alt="True Essence"
    aria-label="True Essence" /><br>
</div> 
<br>

[True Essence](https://.herokuapp.com) was created by Lee-Ann Clark.
A beautiful site that takes one back to nature and its True Essence.

In today's fast-paced world filled with man-made medications, there has been a shift, where people are coming back to nature and what she can provide for us.
In the way of medications for all sorts of ailments from headaches to more deeper-seated problems. It is nice to be able to find a place that caters 
for all the natural ingredients from oils to soaps to ways of easings one's mind.

This is how True Essence was born.

## HOW TO USE
This project requires STRIPE payments and USER AUTHENTICATION 

### Card Payments
- credit card number and details 4242 4242 4242 4242 04/25 123 12345 
- this can be used when making a purchase in the online store.

### Standard User
- To register you will need to confirm your email address.
- Register and login to be able to load a blog post yourself.
- once logged in you will be able to see your previous purchases. If you have not yet purchased anything, go ahead and give it a try.

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
        - [True Essence Goals](#True-Essence-goals)
    - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [About Page](#about-page)
        - [Online Shop Page](#online-shop-page)
        - [Blog Page](#blog-page)
        - [Contact Page](#contact-page)
        - [Login Page](#log-in-page)
        - [Register Page](#register-page)
        - [Add Product Page](#add-product-page)
        - [Edit Product Page](#editing-product-page)
        - [Delete Product Modal](#delete-product-modal)
        - [Log Out page](#log-out-page)
        - [404 Page](#404-page)
        - [500 Page](#500-page)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Disclaimer](#disclaimer)

----

# UX

## Goals

### Visitor Goals

The target audience for True Essence is:

- Anyone who is looking for a natural way to heal or medicate themselves.
- Anyone who enjoys being in nature and wants to plant and grow their own essential plants.
- Anyone who enjoys soap or candle making can now be shown how to do it with oils.
- Anyone who wants to learn how to make soaps or candles.
- Anyone who is looking to find information on plants, medical ideas or soaps and candles that is all in one place.

User goals are:

- To have a place where naturally made products can be purchased, knowing that they are 100% natural.
- To be able to find the latest tips in essential gardening and natural recipes easily.
- To be able to contact the company should you have feedback or a concern.
- To be able to shop online safely
- To be able to have items delivered at a nominal fee or free dependant on the sum spent.
- To have a place where a blog can be found filled with information.
- To be able to add comments

Some extra goals users might have:

- Be inspired to learn to make your own soaps, oils and candles.
- Something the whole family can learn and get involved in.
- Spend more time outdoors as a family or with the kids learning to grow essential plants.
- Learning about the health properties of plants.

True Essence meets these user needs in that:

- The recipes here and all of our products are 100 % naturally made.
- Our new blog is filled with tips and help and recipes on all things "Essential".
- This is wonderful in that there are always new and improved ideas to try and recipes to inspire all.
- Our online store is safe and uses a program that protects your data, so you can shop with confidence.
- With every new order the delivery amount is adjusted depending on the sale amount. Meaning delivery could be free.
- We now have a weekly blog that is filled with information on gardening, medical and recipes.
- The user can add comments to the blogs, this helps us to know what the user wants in the next blog. 

### Business Goals

- To give the user the ease and convenience of shopping in our online store.
- To give the user the option to increase their shopping to obtain "Free Delivery".
- To give the user the peace of mind that their payment details are safe.
- To give the user a place to learn/read about new ideas on essential gardening.


Business Owner goals are:
- To give be able to grow our(the company) brand and customer base
- To grow the business in areas such as getting customers to come and see the farm
- To grow the business so that we can offer lessons and classes in all things "Essential".

True Essence meets these user needs in that:

- The user has access to the online store and can make purchases from the store. 
- If the user has logged in, they have access to see their previous purchases under "My Profile page"
- When the user is purchasing items from the online store, they can see what their total spent is and how much they need to spend to get "Free Delivery".
- If the user has the correct validated login they can add products to the store.
- The Add-Product page is clearly structured and laid out in an easy to understand way. The user has the option to Add their Product, if they are satisfied they can then save their product or delete it.
- The user interface for the input of products has been controlled to validate input. For example, the correct URL format is required for the image input.
- Setting input field types to `min length, `max length,` number`, `URL etc makes sure the user is prompted when the data they have added is incorrect.
- To make navigation easy for the user, buttons have been provided on the pages to help direct should they get stuck. For example, cancel, edit, add-recipe etc.

### True Essence Goals

- To provide an easy to navigate site, where people can purchase their favourite oils and keep track of what they have ordered previously in the profile section.
- To provide a site that is knowledgable in the growing and nurturing of essential oil plants.
- To provide a site that is knowledgable in the making of scented soaps and candles.
- To grow the brand of True Essence by way of the online shop.
- To create a regular customer base with the online shop

## User Stories

### Visitor Stories

As a visitor to True Essence I would expect/want/need:
1. To easily find what I am looking for, I want the site layout to make sense, as varying ages have varying understanding so I don't want to be confused or put off using it. 

2. The information to be laid out in a way that is easy for me to navigate and understand, so I may find what I need quickly and efficiently.

3. The ability to search through the products to find what I need. Then to be able to click and get more detailed information.

4. The ability to search through the blog posts to find what I need. Then to be able to click and get more detailed information.

5. To be able to filter the products and blog posts by name, description or category and find the item that is best suited for my needs.

6. As someone keen on learning new things, I want to be able to find a recipe that is easy and quick and fun to make.

7. As a user I want my details to be safely kept and not reused or sold.

8. As a user accessing this site from smaller devices such as a mobile phone or tablet, I want the site to be responsive so that it is still easy to navigate. 

9. As a user I want to be able to see a record of my previous purchases.

## Design Choices
True Essence is an informative and interesting site with products from oils to candles and diffusers. 
Everything you and your home need.

The following design choices were made with this in mind:

### Colours
<div align="center">
    <img src="https://i.ibb.co/R289T81/True-Essence-Colors.png" alt="True Essence Palette" aria-label="True Essence Colors">
<br>
</div>

- The home page is crisp in white header and with yellow lemons and green leaves.
- The navbar background is kept white all the way through, with a soft lavender as the page overlay for all other pages
- The product cards have clear white background with black writing on them which show up nicely on the lavender overlay.
- The blog posts are on a white card with an image of the category.
- The post links are done in blue so they show up nicely and can be seen straight away in the blog snippet.
- In the footer, two colours were used. A soft pink and a darker purple. This makes the footer stand out more and adds contrast to the page.

### Styling
- All **buttons** on the site fit the bootstrap button styling in size and shape, I kept the colours of blue and red for the edit and delete buttons and black for the rest of the buttons. 
- Bootstrap **cards** were utilized on the products page to display the product selection.
- Bootstrap **cards** were utilized on the blog page to display the category selection, with a link to each category selection page on it. 
- hover effects
    - Some subtle **shadows** have been added to the navbar dropdown menus. Links have been underlined. All this gives a positive user experience.

## Wireframes
- [Home Page](https://share.balsamiq.com/c/xiVDhooqR3LYUWTqw3Dzm2.png)
- [About Page](https://share.balsamiq.com/c/pygzqN9TQbkoyQgJpBLFtv.png)
- [Product Dropdown Page](https://share.balsamiq.com/c/gdSMSR97bJzp9NYYQNhU55.png)
- [Blog Page](https://share.balsamiq.com/c/janNSJ7VVkZbnJESHL611T.png)
- [Blog Page mobile](https://share.balsamiq.com/c/pMDSn8U2hom6Vk86kLWqpP.png)
- [Add Blog](https://i.ibb.co/JnW9qH4/add-blog.png)
- [Edit Blog](https://i.ibb.co/HDmDqxw/Edit-Blog.png)
- [Delete Blog](https://i.ibb.co/ZJrSWJg/Delete-Blog.png)
- [Login Page](https://share.balsamiq.com/c/6rbmvPZYXBjk2fz13CBoCQ.png)
- [Register Page](https://share.balsamiq.com/c/7XeodstNwnijxVnMkpVkvj.png)

# Features
 
## Custom JavaScript
- In the blog section the main imagery was not the same height. By customising the js of the page, it made things look nicer. 
- By defining js on the blog.html page using the class selector for those images, improves the user experience.

## Existing Features

### Elements on every page
- Navbar
- The navigation bar features the True Essence logo in the top left corner.

- For visitors to the site who are not logged in, list items links are available for them to use.
    1. Home (The logo itself)
    2. Products (drop-down menu of products)
    3. Blog Posts(Read-Only)
    4. Log In
    5. Register 
    6. Shopping Bag

- For users who are logged in, the list items are as follows: 
    1. Home (The logo itself)
    2. Products (drop-down menu of products)
    3. Blog Posts
    4. Add New Blog
    5. Shopping Bag
    6. Product Management
    7. Profile page
    8. Log Out
    
- Python determines if the user is logged in or not by checking `if 'user' in session` and passes this data to Jinja to display the correct welcome message on the profile page to the user.
- The navbar is collapsed into a burger icon on small and medium screens, so that menu items do not start overlapping content or headings. 

- Footer
    - The footer features:
        - A list of quick links users might need when viewing the footer and wanting to return to a particular page.
        - Social Media Links 
        - Copyright information.

### Home Page
<div align="center">
<img src="https://i.ibb.co/G7K3mMc/Home-Page.png" alt="True Essence Home Page on all major screen sizes" >
</div>
<br>

**Hero Image**
- True Essence home page features a cheerful and colourful hero image that has bright colours. Bright yellow lemons and green leaves surround an essential oils bottle.
- This image is coded as a background-image in CSS and set to `background-size: cover;` so that it is responsive and doesn't distort or stretch. 

**Search Bar**
- On the top of each page is a Search Bar that was coded in using `Text Index Searching`. The search bar has a search button on the left side of the search bar.
- The user can search through a set of parameters such as `Product Name` or  `item description` to find the products they are looking for.

### Products Page
<div align="center">
<img src="https://i.ibb.co/wgy7T1P/Products-Page.png" alt="True Essence Product Page on all major screen sizes" >
</div>
<br>

**Dropdown Product List**
- This dropdown list is found in the navbar. It is a dropdown list of all products under the online shop nav. At the top is `Candles`, then `Soaps`, `Diffusers`, `Oils`, `New Arrivals` and then `Special Occasions. 
- Each selection takes you to the product page of all products added in that category.

### Blog Post Page
<div align="center">
<img src="https://i.ibb.co/S3kM37h/Blog-Posts.png" alt="True Essence Product Page on all major screen sizes" >
</div>
<br>

**Dropdown Blog List**
- This dropdown list is found in the navbar. It is a dropdown list of all Blog Posts under the Our Blog nav. At the top is `All`, then `Gardening`, `Medical`, `Recipes`, and `Add Post`. 
- Each selection takes you to the blog post page of all posts added in that category.

### Log In Page
<div align="center">
<img src="https://i.ibb.co/V9HVTKv/Sign-in.png" alt="True Essence Login Page page on all major screen sizes" >
</div>
<br>

- The login page features a simple **form** where the user enters their username and their password. If the user enters an incorrect password or username a flash message will inform the user of this.
  The user once logged in will receive a welcome message and be directed to their profile page. 
- The profile page a page for that specific user. All the previous purchases that this user has ever purchased will be on this page. This page is unique to the user.
- The user then has the option to add, edit or delete blog posts. These buttons will appear only on the session users profile page on the blog post. The user will not be able to edit or delete blog posts that were not added by the user.
- If the user does not have a username or password the user is directed to the registration page.

### Register Page
- The Register page is also a simple **form** whereby the user has to choose a username and password.
 - Once the user name and password have been entered and are not duplicates of what is already there, the site will direct you to your blank profile page. Now you are ready to start adding blogs and purchasing products.

 ### Add Post Page
- This can only be accessed if you are logged in as a user.
- The Add Post page is a **form** that gives the user the selection of which category they want the post to show in. 
- The user then can select an image and add it to the body box where the post will appear. The Post can be edited and made to appear as any normal post.
- Validation of the `<input>` fields is handled in different ways. The input `type` attributes are set to `text`, and `url`.
- Limits are placed on both min and max lengths of input accepted.

### Editing Post Page
- Once a new post has been added and the user wants to edit his /her post, they can log in to their profile page and on their post will be 2 buttons.  One for `Edit` and the other for `Delete`. 
- The edit button allows the user to edit the post and then at the bottom of the post will be an update button. The user can then update once the editing is complete.
- Upon successful completion, a message will state that the post has been successfully updated. 

### Delete Post
- Should the user decide that they want to **DELETE** the post and they click on delete button, a page will appear with a message asking if the user is sure that want to delete this? if the user clicks on the "Delete" button below the post will be deleted. 
- This page is a safety net to ensure the user doesn't remove all the information they entered.
- Users have to be logged in to be able to delete posts.

### Add Comment Page
- The user can add a comment to any blog post.
- Once the user has added a comment click on the blog post and see the comment below that post.

### Log Out Page
- The logout page allows users to end their session.
- It provides a way for users to prevent others from updating their posts or using their information..

### 404 Page
<div align="center">
<img src="https://i.ibb.co/c25f3Cr/404.png" alt="True Essence 404 Page page on all major screen sizes" >
</div>
<br>
- This page has the page header and looks like the other pages except that it has a 404 message and and image so the client is not left confused.
- The message is " Sorry, The page you are looking for cannot be found."

### 500 Page
- This page is very similar to the 404 page and has a message of " Sorry, An error has occurred. We've let our techs know and hope to fix it soon."

## Features Left to Implement
 - The Features Left To Implement is a section that will grow in time as the site itself grows.

- Workflow for comments so admin can approve and edit them before they are public
- restrict the ability to edit/delete posts to users that created them
- update logged in user ability to manage own posts and own comments
- update admin user ability to manage all posts and comments
- update search on the blog page for keywords in blogs, not products
- allow users to like or unlike blog posts
 
 # Information Architecture
 - The blog model, the comments model and the contact model were created to add to the basic structure of the project.
 - The blog model allows the user to use the full CRUD operations. Once logged in they can create their own blog, edit and delete the blog and read their own and other blogs as well.
 - Having a blog section then needs to have a comments section as well. People like to let you know what they are thinking.
 - The comments section appears under each blog and the user can then leave a comment on the blog they have read.
 - The contact model is a smaller model that allows the user to get in contact with True Essence via email and receive a response in turn.

### Database Choice

As this website is a student project and where I am in the course I had the opportunity to use db.sqlite3 in conjunction with gitpod and Heroku.
Easy access to relational data was made possible as inner objects were used inside the data structure so it could be easily accessed and looped through where needed.

### Data Storage Types

The types of data stored for my project are:
- ObjectId
- String
- Boolean
- Object

### CRUD

- CRUD was used in the development of this site. Create, Read, Update and Delete. The following sections used CRUD.

## Blog  Categories
- The categories are used to organize blogs by common types. They are hard-wired to be Medical, Gardening and Recipes.
    - **Create** Blog Posts are added when accessing the /Add-Post only if the user is logged in.
    - **Read** The Blog Post categories are shown as a drop-down when adding a blog.
    - **Update**  Categories cannot be updated at this point
    - **Delete** Categories cannot be deleted at this point

### Users
- The USERS collection helps tie blogs to users of the website and to manage access to certain functionalities on the site.
    - **Create** User Id's are created when the user registers for the first time. The user can then return with their login data.
    - **Read** Users are displayed on the profile page and used in determining if a user can add, update or delete blog posts.
    - **Update** User records are updated each time they make a purchase.  
    - **Delete** users are not deleted at this time.

### Blog Posts
- The Blog Post collection stores data on all Blogs entered.
    - **Create** New Blogs can be added by many new users that are logged in, to the Blog list.
    - **Read**  The Blogs can be read by many users but not changed in any way unless the user is the session user.
    - **Update**  Blog Posts can only be updated if the user is the session user and has added that particular blog.
    - **Delete**  Blog Posts can only be deleted if the user is the session user and has added that particular blog themselves.

## ERD 
- This is an Entity Relationship Diagram of how the database collections interact.
[ERD](https://i.ibb.co/4pL5CY4/ERD.png)
<br>

# Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Imgbb](https://imgbb.com) to store external images for this project that were not entered into the database.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- Heroku for deployment
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [CSS3](https://www.w3schools.com/w3css/default.asp) - used to style DOM appearance. 
- [HTML5](https://www.w3schools.com/html/default.asp) -  used to define DOM elements. 
- [JQuery](https://jquery.com) - used to initialize handlers for user-interactive elements such as Bootstrap framework pieces like checkboxes, date pickers, menu toggles.
- [JavaScript](https://www.javascript.com/)  -  used to help handle challenge member entry.
- [Python](https://www.python.org/) the project back-end functions are written using Python. Django and Python are used to build route functions.
- [Django](https://docs.djangoproject.com/en/3.0/) Object Relational Mapper, HTML templating, URL routing, Form validation, Authentication, Admin and Security, does a lot of the heavy lifting for a website without much developer input 
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

[Back To Table of Contents](#table-of-contents)

# Defensive Programming
- To prevent everyone from adding posts and being able to delete them at will this code was added.
  @method_decorator(login_required, name='dispatch')
- By using this means that the user has to be logged in to be able to post or edit or delete a post that they have created.

## Testing

### Validation Testing
- [CSS Validator](https://jigsaw.w3.org/css-validator/) 
- [HTML Validator](https://validator.w3.org/)

### Automated Testing
- [Lighthouse Report](https://i.ibb.co/QrPcDw1/lighthouses-report.png)

### Manual Testing
- [browserstack](https://live.browserstack.com/)

- Tested accross mobile devices and web browsers.
- Web Browsers - 
    - [Opera](https://i.ibb.co/SBtyqC9/opera.png)
    - [Firefox](https://i.ibb.co/sFYT7dj/firefox.png)
    - [Micro Edge](https://i.ibb.co/xsrvq3m/edge.png) 
    - [Windows 10](https://i.ibb.co/BzrB7Y4/windows-10.png)

- Mobile phones/tablets - 
    - [Samsung S4](https://i.ibb.co/Wy3h9PH/samsung-S4.png) 
    - [IPhone 7](https://i.ibb.co/KKZ3vmS/Iphone-7.png) 
    - [Google Phone](https://i.ibb.co/Lx3Bhkt/google-phone.png)
    - [Galexy Tablet](https://i.ibb.co/2KQQ918/galaxy-tablet.png) 
    - [Xiaomie](https://i.ibb.co/K6hNhhS/xiaomi.png)


| Feature Tested                                | Steps Taken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Navigation                                    | 1. Land on home page<br>2. Click every navigation link and make sure you go where you should                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| User Registration                             | 1. Fill out registration form.<br>2. See notification about user is registered and validation email sent.<br>3. Click validation link<br>4. log in<br>5. Verify navigation menus changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Products                                      | verify each products has<br>1. image, name, price, category, rating<br>2. product cards in same row are same size                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Product Detail & Add to Bag                   | 1. Click each product's image from Products page to get to detail page<br>2. verify click the product image and view detail page to verify<br>   a. image, name, price, category, rating, description<br>   b. see quantity box that works<br>   c. add 1 or 2 to bag then click keep shopping<br>3. Verify item is in bag layer with correct quanity.<br>4. Click Keep Shopping Button                                                                                                                                                                                                                                                                                                                                                               |
| Bag Functionality                             | Once products is in bag, verify info is correct:<br>1. Image<br>2. Name<br>3. Quantity<br>4. Totals are good                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Checkout - not logged in                      | 1. add 2 usb diffusors to cart<br>2. verify bag info math is good<br>3. click secure checkout from bag layer<br>4 verify math is good on bag page, no delivery charge<br>5. update quantity to 1, verify delivery charge is there in bag and page.<br>6. close bag layer.<br>7. update to 2. Verify changes, close layer.<br>8. click secure checkout button.<br>9. verify form is not filled out.<br>10. Click complete order without filling in data. <br>11. fill in name, click submit and repeat process so you check validation<br>on each required field.<br>12. submit order.<br>13. verify notifcation confirmation email matches what you entered.<br>14. verify confirmation # matches page, layer and email.<br>15. verify math in email. |
| Checkout - logged in<br>no past orders        | 1. add 1 lavendar candles to cart<br>2. verify bag info math is good<br>3. click secure checkout from bag layer<br>4. verify delivery charge<br>5. verify form is not filled out.<br>10. Click login button & login<br>11. click bag and get back to checkout form page.<br>12. verify email is filled out but no other info.<br>13. fill out the form, make secure save button is checked, and click complete.<br>14. verify email, page and notification layer match                                                                                                                                                                                                                                                                                |
| Checkout Process<br>Logged In with Saved Info | 1. add 2 lavendar candles to cart<br>2. verify bag info math is good<br>3. click secure checkout from bag layer<br>4. verify no delivery charge<br>5. verify form is filled out except for full name and creditcard<br>10. Click login button & login<br>11. click bag and get back to checkout form page.<br>12. verify email is filled out but no other info.<br>13. fill out the form, make secure save button is checked, and click complete.<br>14. verify email, page and notification layer match                                                                                                                                                                                                                                              |
| Blog Post Page                                | 1. Log out, click blogs all navigation<br>2. Verify imagery and posts are nice and you see 3 categories of posts ordered by<br>oldest to newest<br>3. click blogs gardening. Verify only gardening posts.<br>4. Click blogs medical, verify only medical posts.<br>5. Click Blogs Recipes, verify only recipe blogs.<br>6. Click add Post, verify you are taken to login page.<br>7. Login, verify you are at an Add post form                                                                                                                                                                                                                                                                                                                        |
| Add Blog Post                                 | 1. log in<br>2. Click "add a Post" from Our Blog in navigation.<br>3. Click POST Button<br>4. If validation error is hit, fill in that form element and then Click POST until<br>form submits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Edit Blog Post                                | 1. find the post you just created.<br>2. Edit it.<br>3. See that required fields are auto populated.<br>3. Add a header image.<br>4. See that the image is on the detail page now.<br>5. Edit it again. <br>6. Add in some fancy body stuff.<br>7. See how cool the editor is.<br>8. Click the post button. <br>9. Validate the updates you made to the body carried over.<br>                                                                                                                                                                                                                                                                                                                                                                        |
| Delete Blog Post                              | 1. Find the post you just updated.<br>2. Delete it.<br>3. Verify it is truly not on the Our Blog All page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Add A Comment to a Blog                       | 1. Make sure you are logged out.<br>2. Click on Growing Lavender Blog.<br>3. Click on an Add Comment Link.<br>4. Type in your comment.<br>5. Click on the Growing Lavender Blog again.<br>6. See the latest comment!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |


### Defect Tracking
> 1. When moving images from gitpod to Heroku there were a few that just didn't want to show. Had to physically load them separately. there was still one that just refused, so it was deleted,
then the problem was solved.
> 2. There was a massive spacing above all the headings on all the pages, I have to adjust the media query 768px and remove the contact form in the css.
> 3. There was an issue with the blog pages and their height and the images not showing on heroku. Had to add a config var DISABLE_COLLECTSTATIC and set it to 1 and tried again. The had to change the /media/ to {{MEDIA_URL}} to get the images to show. Managed to get all 3 images showing finally.
> 4. Then trying to link the blogs to the blog category page. Took out spacings in names_names and then things started working better.
> 5. Added Custom Js to sort out the height issue with the blogs, they all appear correct now.
> 6. Struggled with the contact us image. The image i had chosen was a low quality so when amplified looked terrible. Had to ditch the image and search for a better quality, ended up using the image for the other pages.
> 7. Battled getting the 404 and 500 pages to show. Changed the handler and moved the urls to the main project url. then got it working.

### Outstanding Defects
> 1. On small devices STRIPE CC number overruns into the  date/month field. This field is made by stripe and is very tricky to adjust. The tutors also could not fix it.
    [Number Overflow](https://i.ibb.co/jysvJ9D/number-overflow.png)
> 2. If a user uploads an image with a space in it, Heroku injects an underscore and then the image is not found and writes a 404 console error. I should update the image loading validation to remove spaces for add blog, edit blog, add product, edit product pages/views.

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Gitpod](https://gitpod.io/)

The following **must be installed** on your machine:
- [Python 3](https://www.python.org/downloads/)
- [Git](https://github.com)

- An account at [Heroku](https://dashboard.heroku.com/apps) and 
- An account at [Stripe](https://stripe.com/gb) and 
- An account with [AWS](https://aws.amazon.com/) are needed to complete this project

### Instructions
1. Save a copy of the GitHub repository located at https://github.com/Lee-AnnC/True_Essence by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder.
   If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/Lee-AnnC/True_Essence
```
2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built-in virtual environment.

Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```
6. Install all required modules with the command 
```
pip -r requirements.txt.
```
7. Set up the following environment variables within your IDE. 

        "HOSTNAME="<enter key here>",
        "DEV": "1",
        "SECRET_KEY": "<enter key here>",
        "STRIPE_PUBLISHABLE": "<enter key here>",
        "STRIPE_SECRET": "<enter key here>",
        "EMAILJS_USER_ID": "<enter key here>",
        "STRIPE_SUCCESS_URL": "<enter url here>",
        "STRIPE_CANCEL_URL": "<enter url here>",
        "AWS_ACCESS_KEY_ID": "<enter key here>",
        "AWS_SECRET_ACCESS_KEY": "<enter key here>",
        "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>",

- `DEV` environment variable is set only within the development environment, making it possible to have different settings for the two environments.
For example setting DEBUG = True only when working in development, not on the deployed site.

8. You need to restart your machine to activate your environment variables.

9. Migrate the admin models to create your database template using the command
    ```
    python manage.py migrate
    ```
10. Create your superuser to access the django admin panel with the following command
    ```
    python manage.py createsuperuser
    ```
11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```
12. Once the program is running, go to the local link,  add `/admin` to the end of the url. Here log in with your superuser you just created.

13. Once these items exist in your database your local site will run as expected.

## Heroku Deployment

To deploy True_Essence to Heroku, take the following steps:

1. Create a `requirements.txt` file using the command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps). Give it a name, set the region that is applicable for your location.

4. From the heroku dashboard of your new application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking to the correct GitHub repository.

6. In the heroku dashboard click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
EMAILJS_USER_ID | `<your secret key>`
HOSTNAME | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_CANCEL_URL | `<link to all-products page in your app>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`
STRIPE_SUCCESS_URL | `<link to checkout/confirm page in your app>`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of ShippingDestination and Product within the new database.

12. Once these items exist in your database your heroku site will run as expected.

# Credits

## Content
- The text, images, links and other data in the database was sourced from various websites including but not limited to

- About_Us image[About](https://www.timeout.com/london/things-to-do/lavender-fields-in-and-around-london)
- Steam Distillling[Distilling Video](https://www.youtube.com/watch?v=fBtuUUTbTyw)
- Template code for this site was taken from our Ecommerce Boutique Ado Mini Project Lessons and heavily modified to suit the site needs. There were 3 additional models added.
- Code to help build a blog and its attachments, add, edit, delete and comments were taken from [Codemy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)

## Media

### Images

- The photograph for the hero image was sourced from [womansworld](https://www.womansworld.com/posts/mental-health/essential-oils-for-anxiety)

- Where possible the links to the images for the products and blogs were taken directly from the source image URL. 

- On occasion when this did not work the image was copied to my local machine and then uploaded to my [imgBB](https://leec.imgbb.com/) account, where I took the link from instead.

- Candles
    [Rose](https://www.therosetree.co.uk/blogs/news/aromatherapy-candles-the-ultimate-guide)
    [Lavender](http://fleurfragrances.com/corporate-gifting/)
    [White Lilly](https://wallpapermemory.com/218794)

- Soaps  
    [Lavender](https://br.pinterest.com/marytelma007/sabonete-artesanal/)
    [Rosemary](https://lovelygreens.com/tag/rosemary/)
    [Rose Geranium](https://br.pinterest.com/pin/313422455323721599/)
    [Lemongrass](https://za.pinterest.com/pin/499407046169774646/)
    [Cinnamon](https://www.pinterest.co.uk/pin/292171094574609867/)

- Diffusers
    [Black Fluted](https://browndanielgroup.com/a-beginners-guide-to-essential-oils/)
    [Wooden Fluted](https://bevividyou.com/blogs/vivid-blog/7-reasons-for-home-essential-oil-diffuser)
    [Clear Reed](https://www.ebay.com/c/13036419732)
    [Colored Reed](https://www.indiamart.com/lhasa-aroma/)
    [Two Tone](https://www.contemporist.com/modern-ways-to-introduce-aromatherapy-into-your-home-and-life/)
    [Ceramic](https://www.ecvv.com/product/4064601.html)

- Oils 
    [Citrus](https://www.pinterest.pt/pin/575546027370540982/)
    [Peppermint](https://www.craftovator.co.uk/essential-oils/peppermint-mentha-piperita-essential-oil/)
    [Geranium](http://soiltosoul.asia/product/geranium-oil/)
    [Elemi](https://www.aosproduct.com/ESSENTIAL-OILS/Elemi-Oil)
    [Sandlewood](https://meesho.com/blog/sandalwood-face-pack-benefits)
    [Bergamot](https://www.dreamstime.com/bergamot-essential-oil-bergamot-fruit-isolated-white-background-bergamot-essential-oil-bergamot-fruit-image196691210)
    
- New Arrivals
    [3 pack](https://www.pinterest.fr/pin/501940320966370476/)
    [Remote Control](https://www.amazon.co.uk/household-products-Multi-functional-essential-aromatherapy/dp/B07YQTS9YD)
    [Scented Candles](https://ar.pinterest.com/pin/317503842453953377/)
    [Aromatherapy Gift Basket](https://www.pinkeepromise.com/Essential-Oil-Gift-Basket-Young-Living)
    
- Special Occasions
    [Lavender gift basket](https://www.leisureopportunities.co.uk/news/Body-Bliss-launches-new-aromatherapy-app-for-customisable-spa-treatments/308027
    [Candle Gift Basket](https://kelownacandlefactory.com/product/medium-gift-basket/)
    

- Blog Images
    [Main Blog Image](https://za.pinterest.com/pin/626070785674471920/)

- Blog Category Images
    [Gardening](https://za.pinterest.com/pin/210050770100707234/)
        Growing Lavender[Lavender](https://www.gardendesign.com/plants/lavender.html)
        Growing Peppermint[Peppermint](https://www.masterclass.com/articles/mint-companion-planting-guide)

    [Medical](https://howeessentials.com/)
        [Mint](https://www.indiamart.com/proddetail/green-mint-leaf-23226784197.html)
    
    [Recipes](https://www.dreamstime.com/stock-photo-natural-soaps-spa-setting-flower-aromatherapy-image69369773)
        Recipes Post [Natural Soap](https://lovelygreens.com/eco-friendly-cold-process-soap-recipe-instructions/)

## Code

- Template code for this site was taken from our Ecommerce Boutique Ado Mini Project Lessons and heavily modified to suit the site needs. There were 3 additional models added.

- Template code for cards in the blogs and products were taken from [Bootstrap](https://getbootstrap.com/) and modified to suit the site's needs.

- Code to help build a blog and its attachments, add, edit, delete and comments were taken from [Codemy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)

- Code for buttons taken from [Bootstrap](https://getbootstrap.com/).

- Code for the grid was taken from [Bootstrap](https://getbootstrap.com/)

- Code for adding the correct prefixes to CSS was created using [AutoPrefixer](https://autoprefixer.github.io/).

- To dump and load data help was taken from [Coderwall](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)

- To sort out the blog imagery and heights advice was taken from [CSS-tricks](https://css-tricks.com/snippets/jquery/equalize-heights-of-divs/)

- To make my add post more responsive help was taken from [Nolanbraman](https://www.nolanbraman.com/Resizing%20the%20Django-ckeditor%20To%20Make%20It%20Responsive/)

## Acknowledgements

Special thanks to my mentor **Aaron Sinnot** for his patience and help.

Special thanks to **Malia Havlicek** who's patience and understanding has helped on many a dark day when things haven't gone to plan.
For being my sounding board and an extra pair of eyes when I was just not seeing things.

## Disclaimer
This is a student project and hence the content of this website is for educational purposes only.