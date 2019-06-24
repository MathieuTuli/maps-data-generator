# Maps Data Generator #

This repository will provide functionality to generator the following given a building address:
- Arial shot of the building at XXX zoom, centered
- 10 3D shots, taken at 36 degree increments centered around the building
- Building height
- Building footprint (array of lat/lon points)

## How to use ##
First we need to generate API keys for Google Maps and Open street maps.

***For Google Maps***
Each Google Maps Web Service request requires an API key or client ID. API keys
are freely available with a Google Account at
https://developers.google.com/console. The type of API key you need is a
**Server key**.

To get an API key:

 1. Visit https://developers.google.com/console and log in with
    a Google Account.
 1. Select one of your existing projects, or create a new project.
 1. Enable the API(s) you want to use. The Python Client for Google Maps Services
    accesses the following APIs:
    * Directions API
    * Distance Matrix API
    * Elevation API
    * Geocoding API
    * Geolocation API
    * Places API
    * Roads API
    * Time Zone API
 1. Create a new **Server key**.
 1. If you'd like to restrict requests to a specific IP address, do so now.

For guided help, follow the instructions for the [Directions API][directions-key].
You only need one API key, but remember to enable all the APIs you need.
For even more information, see the guide to [API keys][apikey].

**Important:** This key should be kept secret on your server.
