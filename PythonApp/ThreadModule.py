import threading
import function
class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID, url, path, downloadtype):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.link = url
        self.save_path = path
        self.type = downloadtype
        # helper function to execute the threads
    def run(self):
        #print(str(self.thread_name) +" "+ str(self.thread_ID));
        function.Downloader(self.link, self.save_path, self.type)