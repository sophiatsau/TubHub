# Crittr
A GrubHub-inspired platform for animal enthusiasts to buy and sell their critters! Gotta collect them all!

# Live Link
https://crittr.onrender.com/

## Tech Stack
<!-- List of techs/languages/plugins/APIs used
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=python,flask,javascript,react,redux,css,html,docker,postgres,sqlite,aws" />
</a> -->

<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" /><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white" />
<img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" />
<img src="https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" />

# Index
[Database Schema](https://github.com/sophiatsau/Crittr/wiki/DB-Schema) | [Feature Lists](https://github.com/sophiatsau/Crittr/wiki/Features-List) | [Future Implementations](https://github.com/sophiatsau/Crittr/wiki/Future-Implementations) | [User Stories](https://github.com/sophiatsau/Crittr/wiki/User-Stories)


## Screenshots
### Landing Page
Enter your address to view shops around you!

### Shop Page
Check out the different animals being sold!

### Profile Page
Here, you can add, edit, or remove your addresses.

If you are a shop owner, you can manage your shops and critters.

# Endpoints
### Auth
| Request  | Purpose | Return Value | Status |
| :------- | :------ | :----------- | :------ |
| GET /api/auth/  | On initial load and subsequent refreshes, returns logged in user if there is one | {<br/>&nbsp;&nbsp;&nbsp;"id": INT, <br/>&nbsp;&nbsp;&nbsp;"username": STRING, <br/>&nbsp;&nbsp;&nbsp;"email": STRING, <br/>&nbsp;&nbsp;&nbsp;"firstName": STRING, <br/>&nbsp;&nbsp;&nbsp;"lastName": STRING, <br/>&nbsp;&nbsp;&nbsp;"balance": DECIMAL<br/>, <br/>&nbsp;&nbsp;&nbsp;"shops":[ARRAY of INT], <br/>&nbsp;&nbsp;&nbsp;"addresses":{INT:{ADDRESS OBJ}}, <br/>&nbsp;&nbsp;&nbsp;"critters":[ARRAY of INT]} | 200 |
| POST /api/auth/login | Logs in user. Successful login returns user dictionary |{<br/>&nbsp;&nbsp;&nbsp;"id": INT, <br/>&nbsp;&nbsp;&nbsp;"username": STRING, <br/>&nbsp;&nbsp;&nbsp;"email": STRING, <br/>&nbsp;&nbsp;&nbsp;"firstName": STRING, <br/>&nbsp;&nbsp;&nbsp;"lastName": STRING, <br/>&nbsp;&nbsp;&nbsp;"balance": DECIMAL<br/>}| 200 |
| GET /api/auth/logout | Logs current user out |{"message": "User logged out"}| 200 |
| POST /api/auth/signup | Signs user up with provided info. Creates new user, logs them in, and returns user dictionary |{<br/>&nbsp;&nbsp;&nbsp;"id": INT, <br/>&nbsp;&nbsp;&nbsp;"username": STRING, <br/>&nbsp;&nbsp;&nbsp;"email": STRING, <br/>&nbsp;&nbsp;&nbsp;"firstName": STRING, <br/>&nbsp;&nbsp;&nbsp;"lastName": STRING, <br/>&nbsp;&nbsp;&nbsp;"balance": DECIMAL<br/>}| 200 |
<!-- | GET /api/auth/unauthorized | Returns errors when flask-login authentication fails |{"errors": {"user": "Unauthorized"}}| 403 | -->
<!-- | GET /api/auth/oauth_login | Redirects user to Google Oauth login if user chooses to login or sign up via Google account |redirect(authorization_url)| 302 |
| GET /api/auth/callback | If Google account authorization successful, creates new user if user doesn't exist, logs user in, and redirects user to landing page |redirect(landing page URL)| 302 | -->

### Addresses
| Request  | Purpose | Return Value | Status |
| :------- | :------ | :----------- | :------ |
| GET /api/addresses/current | Query for all of logged in user's addresses and returns them in a list of dictionaries | {"addresses": <br/>&nbsp;&nbsp;&nbsp;[ARRAY:{"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"fullAddress": STRING}]<br/>} | 200 |
| POST /api/addresses/new | Creates a new address for the user and returns new address in a dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"fullAddress": STRING<br/>} | 201 |
| PUT /api/addresses/:addressId/edit | Edits an existing address for the user and returns updated address in a dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"fullAddress": STRING<br/>} | 200 |
| DELETE /api/addresses/:addressId/delete | Deletes an address and returns a message if successfully deleted | {"message": "Address successfully deleted."} | 200 |

### Shops
| Request  | Purpose | Return Value | Status |
| :------- | :------ | :----------- | :------ |
| GET /api/shops/ | Returns all shops available as a list of dictionaries | {"shops": <br/>&nbsp;&nbsp;&nbsp;[ARRAY:{<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"priceRange": INT,<br/>&nbsp;&nbsp;&nbsp;"businessHours": STRING,<br/>&nbsp;&nbsp;&nbsp;"pickup": BOOL,<br/>&nbsp;&nbsp;&nbsp;"delivery": BOOL,<br/>&nbsp;&nbsp;&nbsp;"searchImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"categories": [ARRAY of "category.name"]}]<br/>} | 200 |
| GET /api/shops/current | Returns all current user's shops as a list of dictionaries | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"priceRange": INT,<br/>&nbsp;&nbsp;&nbsp;"businessHours": STRING,<br/>&nbsp;&nbsp;&nbsp;"pickup": BOOL,<br/>&nbsp;&nbsp;&nbsp;"delivery": BOOL,<br/>&nbsp;&nbsp;&nbsp;"searchImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"categories": [ARRAY of "category.name"]<br/>} | 200 |
| GET /api/shops/:shopId | Queries for and returns shop details by id | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"priceRange": INT,<br/>&nbsp;&nbsp;&nbsp;"businessHours": STRING,<br/>&nbsp;&nbsp;&nbsp;"pickup": BOOL,<br/>&nbsp;&nbsp;&nbsp;"delivery": BOOL,<br/>&nbsp;&nbsp;&nbsp;"searchImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"categories": [ARRAY of STRING],<br/>&nbsp;&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;&nbsp;"phoneNumber": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"coverImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"businessImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"formattedAddress": STRING,<br/>&nbsp;&nbsp;&nbsp;"critters": [ARRAY of INT],<br/>&nbsp;&nbsp;&nbsp;"crittersDetails": [ARRAY of DICT]<br/>} | 200 |
| POST /api/shops/new | Creates a new shop and adds it to the database, returns new shop as dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"priceRange": INT,<br/>&nbsp;&nbsp;&nbsp;"businessHours": STRING,<br/>&nbsp;&nbsp;&nbsp;"pickup": BOOL,<br/>&nbsp;&nbsp;&nbsp;"delivery": BOOL,<br/>&nbsp;&nbsp;&nbsp;"searchImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"categories": [ARRAY of STRING],<br/>&nbsp;&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;&nbsp;"phoneNumber": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"coverImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"businessImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"formattedAddress": STRING,<br/>&nbsp;&nbsp;&nbsp;"critters": [ARRAY of INT],<br/>&nbsp;&nbsp;&nbsp;"crittersDetails": [ARRAY of DICT]<br/>} | 201 |
| PUT /api/shops/:shopId/edit | Edits an existing shop, returns edited shop as dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"userId": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"address": STRING,<br/>&nbsp;&nbsp;&nbsp;"city": STRING,<br/>&nbsp;&nbsp;&nbsp;"state": STRING,<br/>&nbsp;&nbsp;&nbsp;"zipCode": STRING,<br/>&nbsp;&nbsp;&nbsp;"priceRange": INT,<br/>&nbsp;&nbsp;&nbsp;"businessHours": STRING,<br/>&nbsp;&nbsp;&nbsp;"pickup": BOOL,<br/>&nbsp;&nbsp;&nbsp;"delivery": BOOL,<br/>&nbsp;&nbsp;&nbsp;"searchImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"categories": [ARRAY of STRING],<br/>&nbsp;&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;&nbsp;"phoneNumber": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"coverImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"businessImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"formattedAddress": STRING,<br/>&nbsp;&nbsp;&nbsp;"critters": [ARRAY of INT],<br/>&nbsp;&nbsp;&nbsp;"crittersDetails": [ARRAY of DICT]<br/>} | 200 |
| DELETE /api/shops/:shopId/delete | Deletes a shop and returns a message if successfully deleted | {"message": "Shop successfully deleted"} | 200 |
| POST /api/shops/:shopId/critters/new | Creates a new critter and adds it to the database, returns new critter as dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"species": STRING,<br/>&nbsp;&nbsp;&nbsp;"shopId": INT,<br/>&nbsp;&nbsp;&nbsp;"price": DECIMAL,<br/>&nbsp;&nbsp;&nbsp;"category": STRING,<br/>&nbsp;&nbsp;&nbsp;"previewImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"stock": INT<br/>} | 201 |

### Critters
| Request  | Purpose | Return Value | Status |
| :------- | :------ | :----------- | :------ |
| GET /api/critters/ | Returns all critters available as a list of dictionaries | {"critters": <br/>&nbsp;&nbsp;&nbsp;[ARRAY:{<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"species": STRING,<br/>&nbsp;&nbsp;&nbsp;"shopId": INT,<br/>&nbsp;&nbsp;&nbsp;"price": DECIMAL,<br/>&nbsp;&nbsp;&nbsp;"category": STRING,<br/>&nbsp;&nbsp;&nbsp;"previewImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"stock": INT}]<br/>} | 200 |
| GET /api/critters/current | Returns all current user's critters as a list of dictionaries | {"critters": <br/>&nbsp;&nbsp;&nbsp;[ARRAY:{<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"species": STRING,<br/>&nbsp;&nbsp;&nbsp;"shopId": INT,<br/>&nbsp;&nbsp;&nbsp;"price": DECIMAL,<br/>&nbsp;&nbsp;&nbsp;"category": STRING,<br/>&nbsp;&nbsp;&nbsp;"previewImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"stock": INT}]<br/>} | 200 |
| PUT /api/critters/:critterId/edit | Edits an existing critter, returns edited critter as dictionary | {<br/>&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;"name": STRING,<br/>&nbsp;&nbsp;&nbsp;"species": STRING,<br/>&nbsp;&nbsp;&nbsp;"shopId": INT,<br/>&nbsp;&nbsp;&nbsp;"price": DECIMAL,<br/>&nbsp;&nbsp;&nbsp;"category": STRING,<br/>&nbsp;&nbsp;&nbsp;"previewImageUrl": STRING,<br/>&nbsp;&nbsp;&nbsp;"description": STRING,<br/>&nbsp;&nbsp;&nbsp;"stock": INT<br/>} | 200 |
| DELETE /api/critters/:critterId/delete | Deletes a critter and returns a message if successfully deleted | {"message": "Critter successfully deleted"} | 200 |

# Connect With Me!
<a href="https://www.linkedin.com/in/sophiatsau/">LinkedIn</a>
