# Form Typing Automation

Form Typing Automation is a Python application takes in a text file and types in the first line and hits enter to submit. Then incase the form doesn't clear itself, it does CTRL+A to select everything, deletes it, and types the next line.

## Features

- Browse and select a text file.
- Set a cooldown between submits (in seconds).
- Pause and resume typing process.
- Select typing position on the screen.

## Prerequisites

- Python 3.x
- Tkinter
- PyAutoGUI

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/ImPot8o/form-typing-automation.git
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```
    python form_typing_automation.py
    ```

2. Browse and select a text file.
3. Set the cooldown between submits.
4. Click on "Launch" to start the typing process.
5. Click on "Pause" to pause the typing process. Click again to resume.
6. Click on "Select Typing Position" to set the typing position on the screen.

## Screenshots

![Application](https://cdn.nest.rip/uploads/bbbf41ab-46a8-4f53-b8ea-8120a18b9b5a.png)

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).
