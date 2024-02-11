import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, callback_function):
        super().__init__()

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file created: {event.src_path}")

def watch_directory(path, event_handler):
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_watch = "/home/mcfrank/notes"
    event_handler = NewFileHandler()
    watch_directory(directory_to_watch, event_handler)

