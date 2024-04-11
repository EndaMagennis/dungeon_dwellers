# Features

[Return to README](README.md)

## Minimum Viable Product Features (Implemented)

### Nav Bar

The navigation bar allows the user to navigate to the home page, login, register. The navbardynamically updates to show logout functionality to authenticated users. On smaller screens, the navbar collapses into a dropdown menu.

  - #### Navbar
  ![navigation bar](documentation/features/navbar.png)

  - #### Navbar dropdown
  ![navbar dropdown](documentation/features/navbar-dropdown.png)


### Home Page

The home page contains a feed of posts created by users.

  - #### Home page
  ![home page](documentation/features/home.png)

### Authentication
Site users can use authentication features such as register, login and logout.

  - #### Registration
  ![register](documentation/features/register.png)

  - #### Login
  ![login](documentation/features/login.png)

  - #### Logout
  ![logout](documentation/features/logout.png)


## Nice To have/ Future Features

### Implemented

  #### Pagination

  When the home page has above 8 posts, a new page is created, and a navigation button is created to navigate to the new page. The new page, then, has navigation to return to the previous page.
   
   - Next
  ![pagination navigation next](documentation/features/pagination-next.png)

  - Previous
  ![pagination navigation previous](documentation/features/pagination-prev.png)



### Future Implementations
  
  #### Likes
  Likes were the top nice to have fearture, however implementation proved difficult and caused many errors. Given time contraints it has been deprecated. This feature will be iplemented in future

  #### Comments
  Another common fearture that will be added in the future is comments. Comments create more interactivity and generates engagement. 
  
  ### User profiles
  User profiles would give the user more control over their feed and also add to UX through customization.

  #### Search for posts
  Earlier iterations of the site nav bar contained a search bar. Again implementation proved tricky and time consuming, so MVP was prioritised. The site is still quite small and so navigation is not a massive hinderance. This feature will be added in future.

  #### Multiple images per post
  Given boardgames often have a lot of components and set up, this would be nice to show how large the game actually is and what play might look like. The card of each post could have a carosel to swipe through images

  #### Account verification/ retreival
  Allauth is substantial in the options available for authentication functionality. Implementing account validation through email would make the site less vulnerable to spam and trolling, though the reach of the site currently makes it a low priority. Additonaly, there is no sensitive information, such as payment credentials or other user account info available, making this implementation a lower priority.

  As I become more familiar and proficient with Django I hope that implementation of features becomes easier and more efficient.