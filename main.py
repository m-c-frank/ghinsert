import time
from insert import create_github_issue
from watchdir import watch_directory
import os
from watchdog.events import FileSystemEventHandler

TOKEN = os.environ.get('GH_INSERT')


class NewFileHandler(FileSystemEventHandler):
    def note_issue(self, body, token=TOKEN):
        repo_owner = "m-c-frank"
        repo_name = "ghinsert"
        title = f"note:{int(1000*time.time())}"
        create_github_issue(repo_owner, repo_name, title, body, token)

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file created: {event.src_path}")
        text = open(event.src_path, "r", encoding="utf-8").read()
        self.note_issue(text)


def main():
    directory_to_watch = "/home/mcfrank/notes"
    event_handler = NewFileHandler()
    watch_directory(directory_to_watch, event_handler)


if __name__ == "__main__":
    main()
