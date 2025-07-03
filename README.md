<h1 align="center">
  <img src="static/xssreplay.jpg" alt="xssreplay" width="150px">
  <br>
</h1>

<h4 align="center">Fast  tool</h4>

<p align="center">
  <a href="#Features">Features</a> •
  <a href="#Requirements">Post Installation</a> •
  <a href="#Install">Install</a> •
  <a href="#Usage">Usage</a> 
  
</p>

---

**xssreplay** is a lightweight automated tool for replaying a list of potential Cross-Site Scripting (XSS) payloads against a target URL. 

It uses Selenium to load each payload in a browser, check for triggered JavaScript alerts, and log successful ones.

This is useful for testing input vectors manually during a penetration test or bug bounty assessment.

---

# Features

- Automatically loads payloads into browser session
- Reads payloads from wordlist
- Detects alert() triggers via Selenium WebDriver
- Logs working XSS payloads to an output file
- Easy to use, zero config beyond Chrome setup

# Requirements

- Python
- Google Chrome
- ChromeDriver
  
ChromeDriver Linux:

```sh
sudo apt update
sudo apt install chromium-chromedriver
```
ChromeDriver Mac

```sh
brew install chromedriver
```
ChromeDriver Windows

https://developer.chrome.com/docs/chromedriver/downloads


- Selenium

```sh
pip install seleniun 
```

# Install

```sh
git clone https://github.com/adminera/xssreplay.git
cd xssreplay
```


# Usage

1. Add your payloads to **payloads.txt** (one per line).
2. Set the **base_url** variable in **main.py** to the target injection point.
3. Run the script:

```sh
python main.py
python3 main.py 
```
4. Successful payloads (those that trigger an alert()) will be written to it_worked.txt.






