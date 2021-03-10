<div align="center">
<h1>True Essence </h1>
<img src="https://i.ibb.co/3Mvxtp2/about-us1.jpg"  href="https://.herokuapp.com/" target="_blank" rel="noopener" alt="True Essence"
    aria-label="True Essence" /><br>
</div> 
<br>

[True Essence](https://.herokuapp.com) was created by Lee-Ann Clark.
A beautiful site that takes one back to nature and its True Essence.

In today's fast paced world filled with man-made medications, there has been a shift, where people are coming back to nature and what she can provide for us.
In the way of medications for all sorts of ailments from headaches to more deeper seated problems. It is nice to be able to find a place that caters 
for all the natural ingredients from oils to soaps to ways of easings ones mind.

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

- To have a place where naturlaly made products can be purchased, knowing that they are 100% natural.
- To be able to find the latest tips in essential gardening and natural recipes easily.
- To be able to contact the company should you have feedback or a concern.
- To be able to shop online safely
- To be able to have itms delivered at a nominal fee or free dependant on the sum spent.

Some extra goals users might have:

- Be inspired to learn to make your own soaps, oils and candles.
- Something the whole family can learn and get involved in.
- Spend more time outdoors as a family or with the kids learning to grow essential plants.
- Learning about the health properties of plants.

True Essence meets these user needs in that:

- The recipes here and all of our products are 100 % naturally made.
- Our new blog is filled with tips and help and recipies on all things "Essential".
- This is wonderful in that there are always new and improved ideas to try and recipes to inspire all.
- Our online store is safe and uses a progrm that protects your data, so you can shop with confidence.
- With every new order the delivery amount is adjusted depending on the sale amount. Meaning delivery could be free. 

### Business Goals

- To give the user the ease and convinience of shopping in our online store.
- To give the user the option to increase their shopping to obtain "Free Delivery".
- To give the user the peace of mind that their payment details are safe.
- To give the user a place to learn/read about new ideas on essential gardening.


Business Owner goals are:
- To give be able to grow our(the company) brand and customer base
- To grow the business in areas such as getting customers to come and see the farm
- To grow the business so that we are able to offer lessons and classes in all things "Essential".

True Essence meets these user needs in that:

- The user has access to the online store and can make purchases from the store. 
- If the user has logged in, they have access to see their previous purchases under "My Profile page"
- When the user is purchasing items from the online store, they can see what their total spent is and how much they need to spend to get "Free Delivery".
- If the user has the correct validated login they can add products to the store.
- The Add-Product page clearly structured and laid out in an easy to understand way.The user has the option to Add their Product, if they are satisfied they can then save their product or delete it.
- The user interface for the input of products has been controlled to validate input. For example the correct url format is required for the image input.
- Setting input field types to `minlength`, `maxlength`,`number`, `url` etc makes sure the user is prompted when the data they have added is incorrect.
- To make navigation easy for the user, buttons have been provided on the pages to help direct should they get stuck. For example, cancel, edit, add-recipe etc.

### True Essence Goals

- To provide an easy to navigate site, where people can purchase their favorite oils and keep track of what they have ordered previously in the profile section.
- To provide a site that is knowledgable in the growing and nurturing of essential oil plants.
- To provide a site that is knowledgable in the making of scented soaps and candles.
- To grow the brand of True Essence by way of the online shop.
- To create a regular customer base with the online shop

## User Stories

### Visitor Stories

As a visitor to True Essence I would expect/want/need:
1. To easily find what I am looking for, I want the site layout to make sense, as varying ages have varying understanding so I dont want to be confused or put off using it. 

2. The information to be laid out in a way that is easy for me to navigate and understand, so I may find what I need quickly and efficiently.

3. The ability to search through the products to find what I need. Then to be able to click and get more detailed information.

4. The ability to search through the blog posts to find what I need. Then to be able to click and get more detailed information.

5. To be able to filter the products and blog posts by name, description or category and find the item that are best suited for my needs.

6. As a someone keen on learning new things, I want to be able to find a recipe that is easy and quick and fun to make.

7. As a user I want my details to be safely kept and not reused or sold.

8. As a user accessing this site from smaller devices such as a mobile phone or tablet, I want the site to be responsive so that it is still easy to navigate. 

9. As a user I want to be able to see a record of my previous purchases.

## Design Choices
True Essence is an informative and interesting site with products from oils to candles and diffusers. 
Everything you and your home need.

The following design choices were made with this in mind:

### Colours
<div align="center">
    <img src="https://i.ibb.co/R289T81/True-Essence-Colors.png" alt=True Essence Palette aria-label=True Essence Colors </div>
<br>
- The home page is crisp in white header and with yellow lemons and green leaves.
- The navbar background is kept white all the way through, with a soft lavender as the page overlay for all other pages
- The product cards have clear white background with black writing on them which show up nicely on the lavender overlay.
- The blog posts are on a white card with an image of the category.
- The post links are done in blue so they show up nicely and can be seen straight away in the blog snippit.
- In the footer two colors were used. A soft pink and a darker purple. This makes the footer stand out more and adds contrast to the page.

### Styling
- All **buttons** on the site fit the bootstrap button styling in size and shape, I kept the colors of blue and red for the edit and delete buttons and black for the rest of the buttons. 
- Bootstrap **cards** were utilized on the products page to display the product selection.
- Bootstrap **cards** were utilized on the blog page to display the category selection, with a link to each category selection page on it. 
- hover effects
    - Some subtle **shadows** have been added to the nav bar dropdown menu's. Links have been underlined. All this gives a positive user experience.

## Wireframes
- [Home Page](https://share.balsamiq.com/c/xiVDhooqR3LYUWTqw3Dzm2.png)
- [About Page](https://share.balsamiq.com/c/pygzqN9TQbkoyQgJpBLFtv.png)
- [Product Dropdown Page](https://share.balsamiq.com/c/gdSMSR97bJzp9NYYQNhU55.png)
- [Blog Page](https://share.balsamiq.com/c/janNSJ7VVkZbnJESHL611T.png)
- [Blog Page mobile](https://share.balsamiq.com/c/pMDSn8U2hom6Vk86kLWqpP.png)
- [Login Page](https://share.balsamiq.com/c/6rbmvPZYXBjk2fz13CBoCQ.png)
- [Register Page](https://share.balsamiq.com/c/7XeodstNwnijxVnMkpVkvj.png)

# Features
 
## Existing Features

### Elements on every page
- Navbar
    - The navigation bar features the True Essence logo in the top left corner.

    - For visitors to the site who are not logged in, list items links are available for them to use.
    1. Home (The logo itself)
    2. Products (drop down menu of products)
    3. Blog Posts(Read Only)
    4. Log In
    5. Register 
    6. Shopping Bag

    - For users who are logged in, the list items are as follows: 
    1. Home (The logo itself)
    2. Products (drop down menu of products)
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
- True Essence home page features a cheerful and colorful hero image that has bright colors. Bright yellow lemons and green leaves surround a essential oils bottle.
- This image is coded as a background-image in css and set to `background-size: cover;` so that it is responsive and doesnt distort or stretch. 

**Search Bar**
- On the top of each page is a Search Bar that was coded in using `Text Index Searching`. The search bar has a search button on the left side of the search bar.
- The user can search through a set of parameters such as `Product Name` or  `item description` to find the products they are looking for.

### Products Page
<div align="center">
<img src="https://i.ibb.co/wgy7T1P/Products-Page.png" alt="True Essence Product Page on all major screen sizes" >
</div>
<br>

**Dropdown Product List**
- This dropdown list is found in the navbar. It is a dropdown list of all products under the online shop nav.At the top is `Candles`, then `Soaps`, `Diffusers`, `Oils`, `New Arrivals` and then `Special Occassions'. 
- Each selection takes you to the product page of all products added in that category.

### Blog Post Page
<div align="center">
<img src="https://i.ibb.co/S3kM37h/Blog-Posts.png" alt="True Essence Product Page on all major screen sizes" >
</div>
<br>

**Dropdown Blog List**
- This dropdown list is found in the navbar. It is a dropdown list of all Blog Posts under the Our Blog nav.At the top is `All`, then `Gardening`, `Medical`, `Recipes`, and `Add Post`. 
- Each selection takes you to the blog post page of all posts added in that category.

### Log In Page
<div align="center">
<img src="https://i.ibb.co/V9HVTKv/Sign-in.png" alt="True Essence Login Page page on all major screen sizes" >
</div>
<br>

- The log in page features a simple **form** where the user enters their username and their password. If the user enters an incorrect password or username a flash message will inform the user of this.
  The user once logged in will receive a welcome message and be directed to their profile page. 
- The profile page a page for that specific user. All the previous purchases that this user has ever purchased will be on this page. This page is unique to the user.
- The user then has the option to add, edit or delete blog posts. These buttons will appear only on the session users profile page on the blog post. The user will not be able to edit or delete blog posts that were not added by the user themselves.
- If the user does not have a username or password the user is directed to the register page.

### Register Page
- The Register page is also a simple **form** where by the user has to choose a username and password.
 - Once the user name and password have been entered and are not duplicates of what is already there, the site will direct you to your blank profile page. Now you are ready to start adding blogs and purchasing products.

 ### Add Post Page
- This can only be accessed if you are logged in as a user.
- The Add Post page is a **form** that gives the user the selection of which category they want the post to show in. 
- The user then can select an image and add it to the body box where the post will appear. The Post can be edited and made to appear as any normal post.
- Validation of the `<input>` fields is handled in different ways.The input `type` attributes are set to `text`, and `url`.
- Limits are placed on both min and max lengths of input accepted.

### Editing Post Page
- Once a new post has been added and the user wants to edit his /her post, they can log in to their profile page and on their post will be 2 buttons.  One for `Edit` and the other for `Delete`. 
- The edit button allows the user to edit the post and then at the bottom of the post will be an update button. The user can then update once the editing is complete.
- Upon successful completion a message will state that the post has been successfully updated. 

### Delete Post
- Should the user decide that they want to **DELETE** the post and they click on delete button, a page will appear with a message asking if the user is sure that want to delete this? if the user clicks on the "Delete" button below the post will be deleted. 
- This page is a safety net to ensure the user doesn't remove all the information they entered.
- Users have to be logged in to be able to a delete posts.

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
The Features Left To Implement is a section that will grow in time as the site itself grows.
 
 # Information Architecture
 - The blog model, the comments model and the contact model were created to add to the basic structure of the project.
 - The blog model allows the user to use the full CRUD operations. Once logged in they can create their own blog, edit and delete the blog and read their own and other blogs as well.
 - Having a blog section then needs to have a comments section as well. Poeple like to let you know what they are thinking.
 - The comments section appears under each blog and the user can then leave a comment on the blog they have read.
 - The contact model is a smaller model that allows the user to get in contact with True Essence via email and recieve a responce in turn.

### Database Choice

As this website is a student project and where I am in the course i had the opportunity to use db.sqlite3 in conjunction with gitpod.
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
- The  categories are used to organize blogs by common types. They are hard wired to be Medical, Gardening and Recipes.
    - **Create** Blog Posts are added when accessing the /Add-Post only if the user is logged in.
    - **Read** The Blog Post categories are shown as a drop down when adding a blog.
    - **Update**  Categories cannot be updated at this point in time
    - **Delete** Categories cannot be deleted at this point in time

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
    - **Update**  Blog Posts can only be updated if the user is the session user and has added that perticular blog.
    - **Delete**  Blog Posts can only be deleted if the user is the session user and has added that perticular blog themselves.

## ERD 
- This is a Entity Relationship Diagram of how the database collections interact.
[ERD](https://i.ibb.co/4pL5CY4/ERD.png)
<br>

# Technologies Used

### Tools
- [Gitpod](https://www.gitpod.io//) is the IDE used for developing this project. 
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [Git](https://git-scm.com/) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- [Techsini](http://techsini.com/) to create the images in this readme file of each page displayed on different screen sizes.

### Libraries
- [CSS3](https://www.w3schools.com/w3css/default.asp) - used to style DOM appearance. 
- [HTML5](https://www.w3schools.com/html/default.asp) -  used to define DOM elements. 
- [JQuery](https://jquery.com) - used to initialize handlers for user interactive elements such as Bootstrap framework pieces like: check boxes, date pickers, menu toggles.
- [JavaScript](https://www.javascript.com/)  -  used to help handle challenge member entry.
- [Python](https://www.python.org/) the project back-end functions are written using Python. Django and Python is used to build route functions.
- [Django](https://docs.djangoproject.com/en/3.0/) Object Relational Mapper, HTML templating, URL routing, Form validation, Authentication, Admin and Security, does a lot of the heavy lifting for a website without much developer input 
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown
[Back To Table of Contents](#table-of-contents)

# Defensive Programming
- To prevent everyone from adding posts and being able to delet at will this code was added.
  @method_decorator(login_required, name='dispatch')
- By using this it means that the user has to be logged in to be able to post or edit or delete a post that they have created.

## Testing

### Validation Testing
- [CSS Validator](https://jigsaw.w3.org/css-validator/) 
- [HTML Validator](https://validator.w3.org/)

### Automated Testing
- [Lighthouse Report](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Ftrue-essence.herokuapp.com)

### Manual Testing
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

- Landed on the home page, clicked the Nav bar buttons to see that they all worked
- Registered and logged in
- Clicked on the products page to view the different products
- Clicked on the blog page and navigated around it, clicked on the posts and the comment section
- Clicked on the ptoducts, added a candle to the bag, purchased the candle.