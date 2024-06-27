# Discord Scanner

A Python script to scan for potential Discord injections and malicious activities.
After reading several texts about injection on discord, and verifying existing patterns in several injection code cases, this is proof of concept only.

## Installation

To run the Discord Scanner, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, follow these steps:

1. Clone this repository: `git clone https://github.com/your-username/discord-scanner.git`
2. Navigate to the project directory: `cd discord-scanner`
3. Create a virtual environment (optional but recommended):
   - Windows: `python -m venv myenv` and then `myenv\Scripts\activate`
   - macOS/Linux: `python -m venv myenv` and then `source myenv/bin/activate`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To run the Discord Scanner, simply execute the following command:

```bash
python main.py
```

## Or make an exe file

```bash
pyinstaller --add-data "myenv\Lib\site-packages\pyfiglet;./pyfiglet" --onefile --icon=assets\app.ico main.py --name=discord_scanner.exe
```

# June 2024
