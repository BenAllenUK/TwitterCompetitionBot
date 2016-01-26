import datetime
import sys
import time

from TwitterAPI import TwitterAPI

# ------------- PROPERTIES START -------------

# Twitter API constants
FILE_NAME = 'twitterconstants.txt'

# Key words looking
KEYWORDS = ["follow", "to", "win", "competition", "prize", "contest", "retweet", "enter", "RT", "tickets", "gift",
            "free", "giveaway"]

# Minimum percent of words required
THRESHOLD = 0.3


# ------------- CODE START -------------
def contains_link(text):
    if "https" in text:
        return True
    else:
        return False


# Anaylze tweet for common key words
def should_retweet(text):
    text = text.lower()
    # is_existing_retweet(text) or
    if contains_link(text):
        return False

    word_count = 0
    for word in KEYWORDS:
        word = word.lower()
        if word in text:
            word_count += 1

    percent_of_common_words = word_count / len(KEYWORDS)
    if percent_of_common_words > THRESHOLD:
        return True
    else:
        return False


def is_existing_retweet(text):
    if text[0] == "r" and text[1] == "t":
        return True
    else:
        return False


def retweet_and_follow(item):
    global retweet_count
    if retweet_count == 0:
        print("Retweeting and following - " + item['text'])
        # r = api.request('statuses/retweet/:%d' % item['id'])

        # TODO: Make the account follow
        id = item['user']['id']
        name = item['user']['screen_name']
        # r = api.request('friendships/update', {'id', id})


        # if r.status_code != 200:
        #     print('Error Retweeting')

        retweet_count += 1


def find_matches_given_tweets(r):
    for item in r.get_iterator():
        if 'text' in item:
            tweet_content = item['text']
            analysis_response = should_retweet(tweet_content)
            if analysis_response:
                retweet_and_follow(item)
                # print(str(analysis_response) + tweet_content)


def init():
    global api, consumer_key, consumer_secret, access_token_key, access_token_secret, twitter_details, retweet_count, start_time
    retweet_count = 0
    start_time = time.time()


    # Try read file
    try:
        twitter_details = open(FILE_NAME, "r")
    except:
        print('ERROR')
        print("You need to make a file called " + FILE_NAME)
        sys.exit()

    # Try get api info
    try:
        consumer_key = twitter_details.readline().rstrip()
        consumer_secret = twitter_details.readline().rstrip()
        access_token_key = twitter_details.readline().rstrip()
        access_token_secret = twitter_details.readline().rstrip()
    except:
        print('ERROR')
        print(
            'You need to add the consumer key, consumer secret, access token key and access token secret in that \n'
            'order on newlines in ' + FILE_NAME)
        sys.exit()

    # Check api info is not wront
    check_api_info(access_token_key, access_token_secret, consumer_secret)

    # Output api info
    print(" Connecting with details: \n" + consumer_key + "\n" + consumer_secret + "\n" + access_token_key + "\n" +
          access_token_secret)

    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    check_api_response(api)

    while True:
        run_search(api)
        sys.stdout.flush()
        time.sleep(60.0)



def run_search(api):
    print()
    time_diff = time.time() - start_time
    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    difference_time = datetime.datetime.fromtimestamp(time_diff).strftime('%H:%M:%S')
    print('[ ' + current_time + ' Running Search, total run time of '+ difference_time +']')
    for key_word in KEYWORDS:
        r = api.request('search/tweets', {'q': key_word})
        find_matches_given_tweets(r)


def check_api_response(api):
    r = api.request('account/verify_credentials')
    if r.status_code != 200:
        print('ERROR')
        print('API details incorrect')
    print()
    print('Connection ok Response: ')
    print(r.text)


def check_api_info(access_token_key, access_token_secret, consumer_secret):
    if consumer_secret == '' or consumer_secret == '' or access_token_key == '' or access_token_secret == '':
        print('ERROR')
        print(
            'You need to add the consumer key, consumer secret, access token key and access token secret in that \n'
            'order on newlines in ' + FILE_NAME)
        sys.exit()


# Begin
init()




# r = api.request('statuses/home_timeline', {'count':50})
# for item in r.get_iterator():
#     if 'text' in item:
#         print(item['text'])


# thetext = input("Enter some text ")
# print("This is what you entered:")
# print(thetext)

# result = urllib.request.urlopen("http://benallen.info").read()
# # print(result)
# from twitter import Twitter
# # ...
# twitter = Twitter()
# api = twitter.Api(consumer_key='P71XDYK8SKcGdHrBf08ewPiia', consumer_secret='LWpSyz54IkFLRB7yL9os9BCd4KIxIern7W8Xn7i7nQLgzRQBNz', access_token_key='183585359-bR7pyeAeb5l9u7OnriVobrBAY8RR2IiSrsZASzNU', access_token_secret='afg64LOmW7QEipCCogvGidPg9wXT6igDOw5PusOokU2vd')
# statuses = api.GetPublicTimeline()
# print [s.user.name for s in statuses]
