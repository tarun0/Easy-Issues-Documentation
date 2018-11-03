<a href="https://github.com/letelete/Easy-Issues-Documentation" alt="GitHub release"><img src="https://i.imgur.com/OQUy5Ly.png" /></a>
<h2 align="center"><b>Easy Issues Documentation</b></h2>
<h4 align="center">Python script to create a documentation for issues status in repository. Made for Google Code-In 2018</h4>

### How does it works

Script creates a repository documentation by checking if issues have any pull-request references.
* if has, script checks if pr is already merged
  * if merged - status: closed 
  * else if pr is closed - status: open (because issue isn't resolved yet)
  * else - status: in_progress
* else if there are many unique references - status: multiple_prs
* else - status: open

<br><br>

### How to use

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




