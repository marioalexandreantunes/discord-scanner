import os
import glob
import time
import pyfiglet
from termcolor import colored

# pyinstaller --add-data "myenv\Lib\site-packages\pyfiglet;./pyfiglet" --onefile --icon=assets\app.ico main.py --name=discord_scanner.exe


def main() -> None:
    """Main function to run the Discord Scanner."""
    ascii_banner = pyfiglet.figlet_format("Discord Scanner")
    print(colored(ascii_banner, 'green'))
    print("=========================================================================")
    ascii_banner = pyfiglet.figlet_format("Mario Antunes")
    print(colored(ascii_banner, 'light_blue'))

    start_time = time.time()

    # Get the user's home directory
    home_directory = os.environ['USERPROFILE'] if os.name == 'nt' else os.environ['HOME']
    print(colored(f"Home directory: {home_directory}", 'green'))

    # Construct the Discord directory path
    discord_directory = os.path.join(
        home_directory, 'AppData', 'Local', 'Discord')

    # maybe check if discord directory exists
    if not os.path.exists(discord_directory):
        print(
            colored(f"Discord directory not found at {discord_directory}", 'red'))
        # maybe check if exist discord canary folder
        discord_canary_directory = os.path.join(
            home_directory, 'AppData', 'Local', 'discordcanary')
        if os.path.exists(discord_canary_directory):
            discord_directory = discord_canary_directory
        else:
            print(colored(
                f"Discord canary directory not found at {discord_canary_directory}", 'red'))
            input("Press enter to exit...")
            return

    js_files = glob.glob(os.path.join(
        discord_directory, '**/*.js'), recursive=True)

    print(colored(
        f"Searching for last changed JavaScript files in {discord_directory}", 'green'))
    print(colored(
        f"Searching for 'injection code words' in .js and .asar files in {discord_directory}", 'green'))
    print("=========================================================================")

    for file in js_files:
        modification_time = os.path.getmtime(file)
        # Discord Injection Warnings:
            # https://github.com/can-kat/cstealer
            # https://www.trendmicro.com/en_us/research/23/e/info-stealer-abusing-codespaces-puts-discord-users--data-at-risk.html
            # https://github.com/k4itrun/discord-injection/blob/main/injection.js
            # https://github.com/waltuhium23/waltuhium/blob/main/Waltuhium.py
            # https://www.pcrisk.com/removal-guides/17509-anarchygrabber-stealer

        # check if the file is a JavaScript/electron file (ends with.js or .asar)
        # check if the file contains any possible injection code words (like 'discord injection', 'WEBHOOK', or 'discord API URLs')
        if file.endswith(".js") or file.endswith(".asar"):
            # read all file content and check if exist possible 'injection code words'
            with open(file, 'r') as f:
                content = f.read()
                if 'process.env' in content and 'discord_desktop_core' in file:
                    print(
                        colored(f"'process.env' is being used, code found in {file}", 'yellow'))
                if 'email' in content:
                    print(
                        colored(f"'email' is being used, code found in {file}", 'yellow'))
                if '/cdn' in content:
                    print(
                        colored(f"'cdn' is being used, code found in {file}", 'yellow'))
                if 'discord injection' in content:
                    print(colored(f"Injection code found in {file}", 'yellow'))
                if 'WEBHOOK' in content:
                    print(colored(f"WEBHOOK found in {file}", 'yellow'))
                if 'https:' in content and 'discord.com/api' in content:
                    print(colored(f"urls found in {file}", 'yellow'))
                if 'discord_desktop_core' in file:
                    # check if exist more than one line
                    # For the %AppData%\Discord\[version]\modules\discord_desktop_core\index.js file,
                    # it should only contain the "module.exports = require('./core.asar');"
                    lines = content.split('\n')
                    if len(lines) > 1:
                        print(
                            colored(f"More than one line found in {file}", 'yellow'))

        # last 24
        # last 24 hours = 86400 seconds (60 seconds * 60 minutes * 24 hours)
        # Subtract 86400 seconds from current time to get time of last 24 hours
        # Compare with modification time to check if the file was modified within the last 24 hours
        if (file.endswith(".js") or file.endswith(".asar")) and modification_time > start_time - 86400:
            print(
                colored(f"{file}: Last modified on {time.ctime(modification_time)}", 'green'))

    input("Press enter to exit...")


if __name__ == "__main__":
    main()
