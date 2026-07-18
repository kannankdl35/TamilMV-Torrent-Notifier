import requests
from bs4 import BeautifulSoup

from config import SITE_URL

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
    )
}


def get_latest_posts():
    """
    Returns:
        [
            {
                "title": "...",
                "url": "..."
            }
        ]
    """

    try:
        response = requests.get(
            SITE_URL,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

    except Exception as e:
        print(f"Scraper Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    posts = []

    seen = set()

    for link in soup.find_all("a", href=True):

        title = link.get_text(" ", strip=True)

        href = link["href"]

        if len(title) < 15:
            continue

        if "(20" not in title:
            continue

        if href.startswith("/"):
            href = SITE_URL.rstrip("/") + href

        if href in seen:
            continue

        seen.add(href)

        posts.append({
            "title": title,
            "url": href
        })

    return posts
