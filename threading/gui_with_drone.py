import threading
import time

class Drone(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.position = 0

    def run(self):
        while True:
            self.position += 1
            print("{} is droning!".format(self.name))
            time.sleep(0.1)

class Gui(threading.Thread):

    def __init__(self,name,drone):
        threading.Thread.__init__(self)
        self.name = name
        self.drone = drone

    def run(self):
        while True:
            time.sleep(1)
            print("drone is at position {}".format(self.drone.position))


if __name__ == '__main__':

    try:
        drone_thread = Drone('drone_thread')
        gui_thread = Gui('gui_thread',drone_thread)

        drone_thread.start()
        gui_thread.start()

    except KeyboardInterrupt:
        pass

