<a href="https://github.com/letelete/Easy-Issues-Documentation" alt="GitHub release"><img src="https://i.imgur.com/OQUy5Ly.png" /></a>
<h2 align="center"><b>Easy Issues Documentation</b></h2>
<h4 align="center">Python script to create a documentation for issues status in repository.</h4>
<h5>Made for specific task in Google Code-In, so Its functionality is strongly focused on this task. It will not be useful for anyone else probably.</h5>

<br><br>

# How to use

#### Initial setup

* Clone this repo on your machine
* Make sure you have [Python](https://www.python.org/downloads) and [PIP](https://pypi.org/project/pip/) installed
* Install required packages with pip
  * open your terminal
  * type `pip install pygsheets oauth2client PyGithub beautifulsoup4 requests`

#### Authorizing pygsheets

To make use of google's spreadsheets, you need to create your own google app which will access to your shared google's sheet

* ([Here's how](https://www.youtube.com/watch?v=vISRn5qFrkM))
* when your google app is ready, and credentials added to project, you should have your OAuth client ID `.json` file saved on your machine.
  * rename your .json file to `client_secret.json`
  * move your client_secret.json to `./user_data` directory
  
#### github access token

To make use of github api, you'll need to configure your github token

* create [github access token](https://github.com/settings/tokens)
* move to the `./user_data` directory
* create `github_secret_key.json`
* paste these lines into your .json file, and change github token to yours
  
```
{
  "access_token" : "REPLACE_THIS_TEXT_WITH_YOURS_TOKEN"
}
```

#### customize sheet, set github repo

* configure your settings in `./user_data/config.json` file

__NOTICE__: 

* Don't add/remove headers since these are kinda hard typed into code. You can only rename them.

* If you really want to colorize issue statuses you can enable it in your config.json file. It works really slowly, so I don't recommend that. It's better to set a conditional formatting in your spreadsheet for status column.

#### Running script

* run script by:
  * double click on run.bat
  * or typing in terminal `py ./src/update_documentation.py`




