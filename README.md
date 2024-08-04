# File Explorer and Notes Application

This repository contains two Tkinter-based applications: a file explorer and a notes viewer. The file explorer allows users to navigate through their filesystem and view disk information, while the notes viewer displays the content of selected files in a simple text editor.

## Features

### File Explorer
- **Disk Information:** Displays total, used, and free space for each disk volume.
- **Navigation:** Users can navigate through folders, open files, and go back to previous directories.
- **Graphical Interface:** Provides a graphical representation of folders and files using icons.

### Notes Viewer
- **Text Display:** Displays the content of selected files in a text editor interface.
- **Real-time Updates:** Updates the text display when a new file is selected.

## Project Structure

- **`file_explorer.py`:** Contains the code for the file explorer application.
- **`notes.py`:** Contains the code for the notes viewer application.

## How to Run

### Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- psutil (for disk information)

### Running the File Explorer

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/file-explorer-notes.git
   cd file-explorer-notes
Install the required packages:

sh
Copy code
pip install psutil
Run the file explorer application:

Copy code
python file_explorer.py
Running the Notes Viewer
Ensure the file_explorer.py is running to select and send file paths to the notes viewer.

Run the notes viewer application:
Copy code
python notes.py
Instructions:

Use the file explorer to navigate through directories and click on a file to view its content in the notes viewer.
Key Bindings
File Explorer:

Mouse Wheel: Scrolls the view vertically or horizontally.
Backspace: Navigate to the parent directory.
Ctrl + C: Reset to the root view showing all disk volumes.
Notes Viewer:

Mouse Enter: Enable text editing.
Mouse Leave: Disable text editing.
Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
