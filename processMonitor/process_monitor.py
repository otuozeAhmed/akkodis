import os
import subprocess
import time
import json
import re
from dataclasses import dataclass, field


@dataclass
class IData:
    pid: int = field(default=0)
    cpu_percent: int = field(default=0.0)
    mem_bytes: int = field(default=0)
    fd_count: int = field(default=0)
    executable_name: str = field(default="init")
    interval: int = field(default=5)
    count: int = field(default=0)
    start: int = field(default=0)


class ProcessMonitor(IData):
    """
    this class diplays the cpu, mem usage and fd count of an executable
    """

    @property
    def get_executable(self) -> str:
        exec_error = "The executable name you entered is invalid!"

        while True:
            try:
                self.executable_name = input(
                    "Enter The Name of The Executable You'd Like To Monitor (e.g. firefox): "
                )
                if not self.executable_name.isalpha():
                    print(exec_error)
                    print("Please try again...")
                    self.get_executable
                self.pid = (
                    subprocess.check_output(["pgrep", self.executable_name])
                    .decode()
                    .strip()
                )
            except subprocess.CalledProcessError:
                print(exec_error)
                print("Please try again...")
                self.get_executable
            break
        return self.executable_name

    @property
    def get_interval(self) -> int:
        while True:
            try:
                self.interval = int(
                    input(
                        "Enter The Interval of Time (secs: 5) You'd Want To Save The Data: "
                    )
                )
            except ValueError:
                print("The interval you entered is invalid!")
                print("Please try again...")
                self.get_interval
            break

        return self.interval

    def _process_monitor(self) -> list[str, str, str, int]:
        self.pid = (
            subprocess.check_output(["pgrep", self.executable_name]).decode().strip()
        )
        self.cpu_percent = (
            subprocess.check_output(["ps", "-p", self.pid, "-o", "%cpu"])
            .decode()
            .split("\n")[1]
            .strip()
        )
        self.mem_bytes = (
            subprocess.check_output(["ps", "-p", self.pid, "-o", "rss"])
            .decode()
            .split("\n")[1]
            .strip()
        )
        self.fd_count = len(os.listdir("/proc/{}/fd".format(self.pid)))

        return self.pid, self.cpu_percent, self.mem_bytes, self.fd_count

    def _collect_data(self) -> dict[str, str]:
        self.count += 1
        self.start += self.interval
        data = {
            "cpu_percent": self.cpu_percent,
            "mem_bytes": self.mem_bytes,
            "fd_count": self.fd_count,
        }
        self.json_data = json.dumps(data)
        print(f"written {self.count} times in {self.start} seconds to file")

        return self.json_data

    def _save_to_json(self) -> None:
        try:
            with open("data.json") as f:
                data = json.load(f)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            data = []
        data.append(json.loads(self.json_data))
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
        time.sleep(self.interval)


def main():
    ps = ProcessMonitor()
    ps.get_executable
    ps.get_interval
    while True:
        ps._process_monitor()
        ps._collect_data()
        ps._save_to_json()


if __name__ == "__main__":
    main()
