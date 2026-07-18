from apscheduler.schedulers.background import BackgroundScheduler

from database import db
from scraper import get_latest_posts

scheduler = BackgroundScheduler()


def check_new_movies(app):
    print("Checking for new uploads...")

    posts = get_latest_posts()

    for post in reversed(posts):

        if db.is_post_exists(post["url"]):
            continue

        db.add_post(post["url"], post["title"])

        text = (
            "🎬 **New Movie Uploaded**\n\n"
            f"📌 {post['title']}\n\n"
            f"🔗 {post['url']}"
        )

        try:
            app.send_message(
                "me",
                text,
                disable_web_page_preview=False
            )

            print(f"New movie: {post['title']}")

        except Exception as e:
            print(e)


def start_scheduler(app, interval):
    scheduler.add_job(
        check_new_movies,
        "interval",
        seconds=interval,
        args=[app],
        id="movie_checker",
        replace_existing=True
    )

    scheduler.start()
