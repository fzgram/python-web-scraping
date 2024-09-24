# Web Scraping with Python and Selenium

## Installing Python

1. **Download Python Installer**:
   - Visit the official Python website: [python.org/downloads](https://www.python.org/downloads/).
   - Download the latest version of Python for your operating system.

2. **Run the Installer**:
   - Double-click the downloaded `.exe` file to launch the installer.
   - **Important**: Check the box labeled "Add Python to PATH" before clicking **Install**.

3. **Verify Installation**:
   - Open **Command Prompt**.
   - Type the following command and press **Enter**:
     ```sh
     python --version
     ```
   - If Python is installed correctly, the installed version will be displayed.

## Installing Selenium

1. **Navigate to the 'src' Folder**:
   - Ensure you're in the directory containing your Python script.

2. **Create a Virtual Environment**:
   - Run the following command to create a virtual environment:
     ```sh
     python -m venv .env
     ```

3. **Install Selenium**:
   - Use `pip` to install Selenium:
     ```sh
     pip install selenium
     ```

## Running the Python Script

1. **Navigate to the 'src' Folder**:
   - Ensure you're in the directory containing your Python script.

2. **Set the Last Page Number**:
   - Open the `requirements.txt` file and update the last page number as needed.

3. **Open Command Prompt in the 'src' Folder**:
   - Open **Command Prompt** and navigate to the `src` folder.

4. **Run the Python Script**:
   - Execute the script using the following command:
     ```sh
     python main.py
     ```
