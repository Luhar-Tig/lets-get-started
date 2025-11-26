import random
from pathlib import Path
from twitter_client import get_twitter_client

TIPS_FILE = Path("content/tips.txt")


def get_daily_tip():
    tips = TIPS_FILE.read_text().splitlines()
    tips = [t.strip() for t in tips if t.strip()]
    return random.choice(tips)


def post_tip():
    client = get_twitter_client()
    tip = get_daily_tip()
    client.create_tweet(text=tip)
    print("Tweeted:", tip)


if __name__ == "__main__":
    post_tip()
