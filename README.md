<h1 align="center">SECOND CHOICE WEB</h1>

[View the live webpage here](https://second-chance-web.herokuapp.com/)
--

Our generation is facing a major global concern: adapting our current lifestyle to achieve a better environment sustainability.


The scope of the website is to give good products a “second chance” (as the title suggests) so that they can fulfill their technical lifetime
before being discarded.

The website I created is a second-hand products web-shop where users can sale different things they don’t need but still in proper functionality. 


The purpose of the **buyer visitors** is to find good products at affordable prices which otherwise would be too expensive or temporary necessary.
Like people relocating for a short-term and they need some furniture or people who wouldn’t spend a lot of money on new bikes for the children
and they rather buy second hand until kids grow old enough to use the same size for longer time.


The purpose of the **seller visitors** is to be able to get some money out of the products which don’t serve their needs anymore.


My personal purpose as a developer in creating Second Chance website is learning how to design, develop and implement a back-end for a web
application using Python, Flask micro-framework and MongoDB database.


The creation of this website is subject solely to educational purposes.



# User Experience
## User Stories
### Buyer Users
1. As a buyer user I want to easily find the products I'm looking for buying.
1. As a buyer user I want to find clear information about the products like title, description, images, quality, price, location.
1. As a buyer user I want to be able to find contact information about the person who sells the product I'm looking for.
1. As a buyer user I want to be able to contact somebody if I'm not satisfied with my purchase.
### Seller Users
1. As a seller user I want to be able to register.
1. As a seller user I want to be able to login.
1. As a seller user I want to be able to view, update and delete my account.
1. As a seller user I want to be able to post different products for advertising with the selling scope.
1. As a seller user I want to be able to update and delete my posts.
## Design
### Color Scheme

### Typography

### Imagery



## Wireframes
-   Wireframes [View]()

<h2 align="center"><img src=""></h2>



# Features
-   It's responsive on different device sizes
-   Defensive programming
-   Secured connection
-   Side Filter with index options for area, condition, category
    
## Features left to implement

# Technologies Used
### Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://nl.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
### Frameworks, Libraries & Programs Used
1. [Bootstrap 4.5.0:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the game.
1. [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used to add the social-media icons in the footer of the page.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Share Tech Mono' font into the style.css file which is used on all text throughout the game.
1. [jQuery:](https://jquery.com/)
    - jQuery was used for the interactive features.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Figma:](https://www.figma.com/)
    - Figma was used to create the [wireframes](https://www.figma.com/file/sxreNPL15miV7jLFIaidk5/memory-game?node-id=0%3A1) during the design process.
1. [PicResize:](https://picresize.com/)
    - PicResize was used to resize the pictures used in the game.
1. [Easycaptures](https://easycaptures.com/)
    - EasyCaptures was used to host the mockup, the sample card images, the html, css and javascript validation results in the README file.
# Testing
## Testing User Stories from User Experience (UX) Section
### Testing Buyer User Stories
1. As a buyer user I want to be able to easily find the products I'm looking for buying.

    1. The ads are displayed in a very obvious manner on the first page of the site.
    2. The users can find the products they're looking for by typing in the search bar on top of the page.
    3. The search key word is looking for results in the title, description and category of the advertising.

    
2. As a buyer user I want to find clear information about the products like title, description, images, quality, price, location.

    1. The ads display on the card content key information about the product the image, the title, the price, the quality and location.
    2. The reveal card is displayed by clicking the photo or the title of the ad and closed back by clicking the close symbol "x".
    3. The reveal card displays detailed information in the product description.
3. 1. As a buyer user I want to be able to find contact information about the person who sells the product I'm looking for.

    1. The reveal card displays information about the seller's contact details (name, email, telephone)
4. As a buyer user I want to be able to contact somebody if I'm not satisfied with my purchase.

    1. There is a contact page where users are able to get in contact with the owners of the website where they can submit a
        message or or via the contact details in the footer section.
### Testing Buyer User Stories
1. As a seller user I want to be able to register. 

    1. The user can register by filling in the required fields: "username", "password" and "confirm password". 
    2. If the username is already in use, the message "Username already exists" is being flashed and the user is redirected to the login page.
1. As a seller user I want to be able to login into "My Account".

    1. The user can login with the registered username and password by filling in the respective fields.
    2. If the username and password match the messages "Welcome 'user'" and the "'username' Account" are being flashed.
    3. If the username is not registered yet, the message "Username doesn't exist" is being flashed and the user is redirected to the register page.
    4. If the username and password don't match the message "Incorrect User or/and Password" is being flashed and the user is redirected to the login page.
1. As a seller user I want to be able to post different products for advertising with the scope of selling.

    1. The seller user can post his ad after having registered by filling in the required fields: 
        -   Category
        -   Photo
        -   Title
        -   Description
        -   Price
        -   Condition
        -   Location
        -   Telephone
        -   Email
1. As a seller user I want to be the only user able to update and delete my posts.

    1. The posted ad displays the edit and delete buttons are available only for the user who posted them.
    2. When clicked, the edit button sends the user to a similar form used for posting the ad.
    3. The displayed ad editing form has the original options and data filled in.
    4. The user can change the desired fields and after clicking the edit button, the changes are saved.

## Validation
-   [W3C Markup Validator](https://validator.w3.org/) View [results](https://easycaptures.com/fs/uploaded/1498/4114442852.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) View [results](https://easycaptures.com/fs/uploaded/1498/2110581351.png)
-   [JavaScript validator](https://jshint.com/) View [results](https://easycaptures.com/fs/uploaded/1498/1830005688.png)
## Further Testing
-   The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   Friends and family members were asked to review the game to point out any bugs and/or user experience issues.
## Bugs
-   When trying to register an already registered user, the user gets the notification that user already exists but still creates another account
# Deployment

## GitHub Pages


## Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
    to retrieve pictures for some of the buttons and more detailed explanations of the above process.

# Credits
For 404.html implementation, the code was copied from the [Flask Documentation site](https://flask.palletsprojects.com/en/master/errorhandling/)
## Images

## Tutorials
## Tutor Support
Special thanks to Johann for his patience and for helping me out with figuring out why the delete button from the profile
template returned the 404 error message that the requested url was not found.
Special thanks to Igor Basuga for his kind support and valuable explanations helping me out when I got stuck with my workspace not being able to preview.
## Other 
