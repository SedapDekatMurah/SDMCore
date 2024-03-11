# This is a terrible readme that i'm using to store notes. Do not look for documentation here

# Product overview
- A superset analysis tool for Google maps' restaurant recommendations.

# User story
- When i want to eat something, I WANT to find the best restaurants in my area that serve that dish
- When viewing restaurant profiles, I WANT to know what people are saying about it

# Developer story
- I WANT a resilient database backup system that can makes regular copies of my restaurant data, and can easily restore from backup in the event of emergencies
- I WANT a containerized hosting ecosystem that robustly manages deployment of the latest version of my application, and isolates server traffic from my hosting system 
- I WANT an access system that is easy to document and scale
- I WANT a development pipeline that is easy to pick up   

# Frontend: SDM app 
- iOS/Android
- No user login
- Pages/Views
  - Ape Makan?: Home page. User inputs a name of a dish he/she wants. There's also an option for "surprise me!"
  - Results: Shows a list of top 10 restaurants. Results must be able to be sorted by Sedap, Dekat and Murah scores
  - Detailed view: Each restaurant listing shows a recent photo, name, google maps link. There are 3 generated elements: Sedap shows a heatmap of the most mentioned words from reviews. Dekat shows travel time (drive/walk). Murah shows an estimation of the menu and its prices.

# Backend: Core/Api?
- REST API (Django most likely)
- Two Apps:
  - Access point: Interacts with the app
    - Reads from Google API and SDM database 
  - Trainer: Regularly scans Google Places for restaurants to add to training data
    - Write access to database 

# Use Cases: Thoroughly planned = >>>
## Frontend
- User opens app
  - get handshake/ping server. 30 secs timeout async
  - receive packet, reply
  - Show logo
  - Show input field
- User inputs dish
  - send packet to server
  - Show loading 30 secs timeout
  - receive packet
    - name
    - recent photo url
    - alt: google review
      - distance?
      - rating
      - price tag
    - sdm preview:
      - sedap score
      - average price
      - distance(reuse google)
- User clicks restaurant 
  - reuse prev packet
    - name
    - recent photo
  - Request new packet(id)
    - new data from db
      - keyword tags (sedap)
      - menu intellisense (murah)
    - google api call
      - enhanced travel estimate: drive n walk


    

- Software update(Dev)

## Backend
- Server Initialization (Dev)
  - Scheduled reboots every 24 hours
  - Needs to be a detached process
  - Pulls newest image from repository
  - Initializes
  - Runs test
- Training
  - Scheduled every 24 hours
  - Gets latest batch of restaurants from Google 
  -  
