# Project Overview

## Project Links

- [Backend github repo link](https://github.com/bcantello/kidtivity-backend)
- [Frontend github repo link](https://github.com/bcantello/kidtivity)
- [Deployment link]()

## Project Description

Kidtivity allows users to find age appropriate activities with step by step instructions for their children.

## API

Most of the data will be stored and accessed from a rest api that I will build. There is the possibility that I may add additional API's for locating parks or museums in the users area, weather, ip address lookup.


## Wireframes


- [Wireframes]()
- [React architecture]()


### MVP/PostMVP



#### MVP - Front end
- User login in form connected to postgres database via Django
- Form to create an account as a new user
- Display currated activites (most favorited, newly added, etc) on home page
- Page for logged in users to add a new activity to the database
- Activity management (update or delete created activities)
- Search for activities (age range, type, etc)
- Responsive design built mobile first

#### MVP - Back end
- Create User app in Django: Create, update, and delete user profile
- Create Authentication app in Django: Only authenticated, logged in users ca create, delete, or update activities
- Create Activity app in Django: Create, update, and delete activities
- Heroku Deployment

#### PostMVP - Front and Back end

- Add user ability to favorite an activity/view favorites
- Add API to find museums and parks in the area
-- Add page to display local museums and parks
-- Add ability to favorite museums or parks
- Add ip address API so that local museums and parks are automatically displayed for the user's location
- Add weather API which returns weather data based on ip address location
- Add a page for activity planning for the week (Calendar?)

## Components

### Front end

| Component | Description | 
| --- | :---: |  
| App | This will make the initial data pull and include React Router| 
| Main | Hold routes |
| Home | Includes images and links for activities |
| Login | Login form |
| Create Account | Create new user account |
| Activity | Displays complete post details for individual activity |
| Header | This will render the header include the nav. Nave will include links for login and signup | 
| Menu | Drop down menu/hamburger |
| Footer | copyright and home nav |

### Back end

| Component | Description | 
| --- | :---: |  
| Users | Model, serializer, views, urls, etc for user | 
| Activity | Model, serializer, views, urls, etc for Activity | 
| Authentication | Model, serializer, views, urls, etc for Authentication | 

### Front end

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| App | H | 5hrs |  |  |
| Main | H | 1hrs |  |  |
| Home | H | 5hrs |  |  |
| Create Account | M | 4hrs |  |  |
| Login | H | 4hrs |  |  |
| Activity | H | 5hrs |  |  |
| Header | M | 1hrs |  |  |
| Menu | M | 3hrs |  |  |
| Footer | L | 1hr |  |  |
| CSS | H | 8hrs |  |  |
| Testing | H | 2hrs |  |  |
| Deployment | H | 1hrs |  |  |
| Total | - | 40hrs |  |  |

### Back end

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create User app | H | 2hr |  |  |
| Create Authentication app | H | 2hr |  |  |
| Create Activities app | H | 3hr |  |  |
| Testing | H | 4hrs |  |  |
| Deployment | H | 2hrs |  |  |
| Total | H | 13hrs |  |  |

## Additional Libraries
 Axios, Google Fonts, react-burger-menu

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description.  Code snippet should not be greater than 10 lines of code. 

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```
