from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import time

change_counter = 0
ALERT_THRESHOLD = 5

class RansomwareDetector(FileSystemEventHandler):
    def on_modified(self, event):
        global change_counter

        if not event.is_directory:
            change_counter += 1
            self.log_alert(event.src_path)

            if change_counter >= ALERT_THRESHOLD:
                self.high_alert()

    def log_alert(self, file_path):
        with open("alert_log.txt", "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"Suspicious file change detected: {file_path} at {timestamp}\n")

        print(f"Alert: Suspicious change detected -> {file_path}")

    def high_alert(self):
        with open("alert_log.txt", "a") as log:
            log.write("HIGH ALERT: Possible ransomware attack detected!\n")

            print("\n HIGH ALERT: Possible ransomware activity!\n")
            
if __name__ == "__main__":
    folder_to_watch = "protected_folder"

    observer = Observer()
    event_handler = RansomwareDetector()
    observer.schedule(event_handler, folder_to_watch, recursive=True)

    observer.start()

    print("Monitoring started....")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring stopped.")

    observer.join()