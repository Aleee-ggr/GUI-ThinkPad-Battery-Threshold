import sys
import fileinput


class Modify:
    def __init__(self, v1, v2):
        self.path = "/sys/class/power_supply/BAT0/"
        self.v1 = v1
        self.v2 = v2
        open(self.path + "charge_start_threshold", "w+").write(v1)
        open(self.path + "charge_stop_threshold", "w+").write(v2)
