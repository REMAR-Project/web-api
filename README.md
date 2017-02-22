REMAR/Crabbler-Web
==================

This is the server side web component for the REMAR citizen science Mangrove crab study.

Running REMAR/Crabbler-web (Development)
========================================

Crabbler-web should be deployed using uWSGI as the app server but it should run perfectly happily using the Flask development server. Assuming that you already have Pip and VirtualEnv installed, cd into the crabbler-web directory then create a new virtualenv:

    $ cd crabbler-web/
    $ virtualenv env

Start your virtualenv then install the external libraries using the supplied requirements.txt

    $ source env/bin/activate
    $ pip install -r requirements.txt

Now create a logs/ directory to store log files from the running app and create an empty log file ready for data:

    $ mdkir var
    $ touch var/crabblerweb.log

Now create the data/ directories where uploaded json files can be stored:

    $ mkdir data
    $ mkdir data/auth
    $ mkdir data/sightings
    $ mkdir data/users


Finally, we want Crabbler-web to run with the src directory as a sub-directory of our application root (mainly so that the etc/ and var/ directories are located correctly relative to the running app) so cd to the crabbler-web folder then start the app as follows:

    $ python src/crabbler_web.py

Now open a browser and navigate to 

    http://localhost:5000/

There isn't much to see at this point because this server app is, for the moment, mostly aimed at consuming data from the crabbler Android app. However, you can test the routes using the JSON API and the cURL command line tool as describer in the section "Using the API".

Run the tests
=============

From the crabbler-web folder you can run the unittests by executing the following:

    $ python test/crabblerwebtest/crabblerwebtest.py


Using the API
=============

You can call the users route to register as follows:
    
    $ curl -H "Content-type: application/json" localhost:5000/api/0.2/users -X POST -d @testdata/user.json

    
which should yield output similar to the following:

    {
      "phone_id": "phoneid-1234abcd", 
      "status": "ok", 
      "statuscode": 200
    }

You can call the auth route to get an access token as follows:

    $ curl -H "Content-type: application/json" localhost:5000/api/0.1/auth -X POST -d @testdata/user.json

which should yield output similar to the following:

    {
      "access_token": "accesstoken-abcd1234", 
      "status": "ok", 
      "statuscode": 200
    }

Finally you can call the upload route, using a suitable JSON document as a payload as follows:

    $ curl -H "Content-type: application/json" http://localhost:5000/up -X POST  -d @testdata/sighting.json 

The sighting route is mapped to the /up/ route:

    $ curl -H "Content-type: application/json" localhost:5000/api/0.2/sightings -X POST -d @testdata/sighting.json

Which should get you a response similar to the following:

    {
      "message": "File Uploaded to data/2017-01-17T18:54:33.683936_e44aeafe-64bc-4099-a38d-124ba1147287.json", 
      "status": "ok", 
      "statuscode": 200
    }

Running REMAR/Crabbler-web (Production)
=======================================

This section is a work-in-progress....

Install uWSGI
Create necessary folder
Create a uWSGI config file

Data
====

All data is stored in the data folder. There are three subfolders for auth, users, and sightings. Internally, the sightings folder will create a sub-folder hierarchy based upon the date in ISO format, e.g. 

    data/sightings/2017/02/22/some-sighting.json

