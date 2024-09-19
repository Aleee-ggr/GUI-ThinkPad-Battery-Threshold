import sys
import subprocess


class Modify:
    def __init__(self, v1, v2):
        self.path = "/sys/class/power_supply/BAT0/"
        self.modify_charge_thresholds(0, 100)
        self.modify_charge_thresholds(v1, v2)

    def modify_charge_thresholds(self, v1, v2):
        try:
            subprocess.run(
                [
                    "sudo",
                    "bash",
                    "-c",
                    f"echo {v1} > {self.path}charge_start_threshold",
                ],
                check=True,
            )
            subprocess.run(
                [
                    "sudo",
                    "bash",
                    "-c",
                    f"echo {v2} > {self.path}charge_stop_threshold",
                ],
                check=True,
            )
        except subprocess.CalledProcessError:
            print("Error while modifying thresholds")
            sys.exit(1)
