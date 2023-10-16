import threading
import time


class CPUPainter:

    wall_number = 0

    def paint_wall(self):
        time.sleep(2)
        self.__class__.wall_number += 1
        print(f"Wall {self.__class__.wall_number} painted")

    def __init__(self):
        t = threading.Thread(target=self.paint_wall)
        t.start()


CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
