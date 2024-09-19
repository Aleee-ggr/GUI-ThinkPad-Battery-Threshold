import sys
import subprocess


class Modify:
    def __init__(self, v1, v2):
        self.path = "/sys/class/power_supply/BAT0/"
        self.v1 = v1
        self.v2 = v2
        self.modify_charge_thresholds()

    def modify_charge_thresholds(self):
        try:
            subprocess.run(
                [
                    "sudo",
                    "bash",
                    "-c",
                    f"echo {self.v1} > {self.path}charge_start_threshold",
                ],
                check=True,
            )
            subprocess.run(
                [
                    "sudo",
                    "bash",
                    "-c",
                    f"echo {self.v2} > {self.path}charge_stop_threshold",
                ],
                check=True,
            )
        except subprocess.CalledProcessError:
            print("Error while modifying thresholds")
            sys.exit(1)
