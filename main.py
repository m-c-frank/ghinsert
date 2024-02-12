import time
from insert import create_github_issue
from watchdir import watch_directory
import os
from watchdog.events import FileSystemEventHandler

TOKEN = os.environ.get('GH_INSERT')
TOKEN_POSTS = os.environ.get('GH_ISSUES_POSTS')


class NewFileHandler(FileSystemEventHandler):
    def post_issue(self, body, timestamp, token=TOKEN_POSTS):
        repo_owner = "m-c-frank"
        repo_name = "posts"
        title = f":page_facing_up:{timestamp}"
        create_github_issue(repo_owner, repo_name, title, body, token)

    def note_issue(self, body, timestamp, token=TOKEN):
        repo_owner = "m-c-frank"
        repo_name = "notes"
        title = f":notes:{timestamp}"
        create_github_issue(repo_owner, repo_name, title, body, token)

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file created: {event.src_path}")
        if str(event.src_path).endswith(".md"):
            timestamp = str(event.src_path).split("/")[-1].split(".")[0]
            text = open(event.src_path, "r", encoding="utf-8").read()
            self.post_issue(text, timestamp)


def main():
    directory_to_watch = "/home/mcfrank/posts"
    event_handler = NewFileHandler()
    watch_directory(directory_to_watch, event_handler)


if __name__ == "__main__":
    main()
