import tweepy
import requests
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAOQBcgEAAAAAt4mjcF4T1l0Z8G%2BSYtmT%2FYqouoQ%3DiIlwUDeSVMThwr6taT1kuJb5odbelhHvcCrn5Yhjclxxwa32ce',      
                       consumer_key='LQOdSKXZN7UQ814kwZXhJrGiN',
                       consumer_secret='DCCWaDUaBbNaSncTatvRyEsvKfaYqbfXgF59fEiSw7LfH4E1xW',
                       access_token='1512539435107241986-kDLeaVSmrhymfciWKFTSUVRF5T8tg9',
                       access_token_secret='XoxyYvQw2J91PzgbdSz3uRGKp5OUv7bKebkG2XJDJwjmk',
                       return_type = requests.Response,
                       wait_on_rate_limit=True)