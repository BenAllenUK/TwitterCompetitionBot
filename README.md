# TwitterCompetitionBot
Automatically enters you into competitions based on searches of keywords. The program runs every 60 seconds,
this is to avoid the rate limit set by Twitter. The program only retweets tweets. It does not yet follow them.


## Requirements
You **WILL NEED**  a Twitter account that is linked to a mobile device. You are then able [to get](https://apps.twitter.com/) a consumer key, consumer secret key, access token key and access secret token.


## Installation
1) FROM GIT CONSOLE: Run `git clone https://github.com/BenAllenUK/TwitterCompetitionBot.git` in command prompt/terminal.
   FROM ZIP: Press Download ZIP in the top right of the project page. Extract somewhere
   
2) [Install Python](https://www.python.org/downloads/)

3) Continue to Usage


## Usage
1) Navigate to the src directory in this project

2) Run `python3 main.py` in command prompt/terminal. 

3) Follow the instructions given in the console


## TODO
- Change runtime so it removes extra hour
- Defend against/make the most of the rate limit by checking reaming attempts which are in response HTTP header
- Instead of just retweeting, follow the account as well.
- Post randomly generated text so that it looks less like a bot