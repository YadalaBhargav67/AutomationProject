from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import shutil


folders = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Text"
}


def organize_file(file_path):

    print("Organizing:", file_path)

    if not os.path.isfile(file_path):
        return

    extension = os.path.splitext(file_path)[1].lower()

    if extension in folders:

        folder = folders[extension]

        os.makedirs(folder, exist_ok=True)

        filename = os.path.basename(file_path)

        destination = os.path.join(folder, filename)

        if os.path.exists(destination):
            print(filename, "already exists in", folder)
            return

        shutil.move(file_path, destination)

        print(filename, "moved to", folder)


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:
            organize_file(event.src_path)


observer = Observer()

handler = MyHandler()

observer.schedule(
    handler,
    ".",
    recursive=False
)

observer.start()

print("Watching folder...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()