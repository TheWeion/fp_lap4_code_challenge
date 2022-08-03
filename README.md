# Urlly

> Let’s face it, most developers are a bit lazy. One thing that can be really laborious is typing in very long URL’s, Urlly solves that problem!


## Requirements
- Users should be able to enter a url into an input box on your website's front page
- Your backend will then generate a shortened path at which a User can access their url
- You must implement Python in some capacity in this application
- Store this shortened path and it's longer counterpart in a database
- No login should be required to create a shortened URL
- If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to 
- If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL 

## Usage

* Access our Urlly Tool: [HERE](https://urllify.herokuapp.com/)
* User enter an URL to the provided input and a custom short ID (optional).
* User receives a new, short URL eg. `https://urllify.herokuapp.com/u5o83` 
* User can now access the website via the new, Urllified link.

## Changelog

### url_shortener/routes/main.py

- [x] Added Exception handling.

- [x] Added `/<short_id>` route to redirect to long URL

- [x] Added Routes for URL shortening

### url_shortener/models/url.py

- [x] Added URL model for the database

### url_shortener/static/styles/styles.css

- [x] Added CSS for static pages

### url_shortener/templates/index.html

- [x] Added template for the homepage.

### url_shortener/templates/base.html

- [x] Added template for the base structure of the website

### url_shortener/__init__.py

- [x] Implemented first iteration of DB structure.

### Pipfile

- [x] Added dependencies.

### .gitignore

- [x] Improved .gitignore boilerplate.

- [x] Added .gitignore file.

## TODO

- [ ] 

## Bugs

- [ ] 