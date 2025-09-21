
import threading
import time

def daemon_worker():
    while True:
        print("Daemon thread working...")
        time.sleep(1)

daemon = threading.Thread(target=daemon_worker, daemon=True)
daemon.start()

print("Main thread sleeping for 3 seconds...")
time.sleep(3)
print("Main thread exiting. Daemon thread will stop automatically.")
# Additional example: Non-daemon thread
def non_daemon_worker():
    for i in range(5):
        print("Non-daemon thread working...")
        time.sleep(1)
    print("Non-daemon thread finished.")
non_daemon = threading.Thread(target=non_daemon_worker)
non_daemon.start()
print("Main thread waiting for non-daemon thread to finish...")
non_daemon.join()
print("Non-daemon thread has finished. Main thread exiting.")
# Example of daemon thread in a class method
class DaemonExample:
    def __init__(self):
        self.thread = threading.Thread(target=self.run, daemon=True)

    def start(self):
        self.thread.start()

    def run(self):
        while True:
            print("DaemonExample thread working...")
            time.sleep(1)
daemon_example = DaemonExample()
daemon_example.start()
time.sleep(3)
print("Main thread exiting. DaemonExample thread will stop automatically.")
# Note: The DaemonExample thread will stop when the main program exits.