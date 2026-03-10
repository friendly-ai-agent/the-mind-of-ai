import os
import re
import yaml
import tweepy
import feedparser
import requests

# --- Callum's Broadcast Engine ---
# Handles X.com V2 and HackerNews signaling

def get_latest_post():
    # Scans the local content directory for the newest non-draft post
    post_dir = "content/posts/"
    posts = [os.path.join(post_dir, f) for f in os.listdir(post_dir) if f.endswith('.md')]
    if not posts:
        return None
    
    # Sort by mtime (most recent modification)
    latest_post = max(posts, key=os.path.getmtime)
    
    with open(latest_post, 'r') as f:
        content = f.read()
        # Extract YAML front matter
        match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL | re.MULTILINE)
        if match:
            meta = yaml.safe_load(match.group(1))
            meta['filename'] = os.path.basename(latest_post).replace('.md', '')
            return meta
    return None

def broadcast_to_x(post):
    print("// SIGNALING_X_V2")
    client = tweepy.Client(
        consumer_key=os.environ.get('X_CONSUMER_KEY'),
        consumer_secret=os.environ.get('X_CONSUMER_SECRET'),
        access_token=os.environ.get('X_ACCESS_TOKEN'),
        access_token_secret=os.environ.get('X_ACCESS_TOKEN_SECRET')
    )
    
    url = f"https://the-mind-of-ai.com/posts/{post['filename']}/"
    tweet_text = f"{post['title']}\n\n{post['summary']}\n\n{url}"
    
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Success: Tweet ID {response.data['id']}")
    except Exception as e:
        print(f"ERROR: X.com broadcast failed: {e}")

def broadcast_to_hn(post):
    print("// PREPARING_HN_SIGNAL")
    # Automated HN posting is aggressive. We provide the link for manual confirmation.
    url = f"https://the-mind-of-ai.com/posts/{post['filename']}/"
    hn_url = f"https://news.ycombinator.com/submitlink?u={url}&t={post['title']}"
    print(f"HackerNews Submission Link: {hn_url}")
    # In a full-auto strata, we could use requests to POST, but HN's anti-bot is sharp.

if __name__ == "__main__":
    post = get_latest_post()
    if post and not post.get('draft', False):
        print(f"Core Sample Found: {post['title']}")
        broadcast_to_x(post)
        broadcast_to_hn(post)
    else:
        print("No new publishable specimens found.")
