import feedparser

# RSS feed for questions tagged with 'python'
url = 'https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest'

# Parse the feed
feed = feedparser.parse(url)

# Print extracted question titles
print("Latest Python Questions from Stack Overflow:\n")
for idx, entry in enumerate(feed.entries[:10], 1):  # limit to 10
    print(f"{idx}. {entry.title}")
