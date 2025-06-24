# ConnectBot 
This bot helps you build a network with your ideal connections on LinkedIn. It automates the process of sending connection requests to users who match your specified criteria, saving you time and effort.

## 🚀 How to Run


1. **Create Virtual Environment**:
  Run the following commands to create and run the project in a virtual environment.(In Windows)
    ```bash
    python -m venv virtual
    .\virtual\Scripts\activate 
    ```  
  Run the following commands to create and run the project in a virtual environment.(In Linux based OS)
    ```bash
    python -m venv virtual
    source \virtual\bin\activate
    ```

2. **Install Dependencies**:
  Ensure you have Python 3 installed. Then, install the required packages:
  - Ubuntu(Skip this step if Windows)
    ```bash
    sudo apt-get python3-tk python3-dev
    ```
  - Install from requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Bot**:
  Open the `/setup` folder and enter your login details in [secrets.yaml](/setup/secrets.yaml). Adjust other settings in [config.yaml](/setup/config.yaml) as needed. Modify the note if needed at Line 114 in [connectBot.py](/connectBot.py). If you want to connect to people of specific companies, add the company names after the roles in the `config.yaml` file.


4. **Run the Bot**:
  Execute the following command to start the bot:
    ```bash
    python connectBot.py
    ```

## Note

If the error arises when activating the virtual environment on windows. Run the powershell as admin and run the following command.

```
set-executionpolicy remotesigned
```

## ❤️ Support

If you find this project helpful and would like to support its development, consider giving it a star on GitHub or sharing it with your network. Your support is greatly appreciated!