# antstacart
Antstack api for store assignment

This repository contain python (flask) based solution to antstack api for store assignment.




## How to run locally?

1) clone git repository on local machine
2) Install dependencies in local environment using 
   
   `pip install -r antstacart-flask/requirements.txt`
3) `python anstacart-flask/src/app.py` to run local server
4) Few test sample json are given in test_json folder for test purpose.
5) Install [httpie](https://httpie.io/) (`snap install httpie` if you snap!)
6) `http POST <localhost>/api/invoice < test_json/sample.json`
## API Endpoints
  ### /api/invoice , Method Allowed = [POST]

### This solution is also hosted on heroku, DONT ABUSE 😈
https://antstacart.herokuapp.com/api/invoice

