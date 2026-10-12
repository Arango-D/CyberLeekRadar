# CyberleekRadar 

A Python-based webpage monitoring tool that detects newly appearing titles and sends Telegram notifications with their associated links.

## Features

- Extracts titles and links from a public webpage using Playwright.
- Compares the current titles with the previous saved state.
- Sends Telegram notifications for newly detected titles.
- Stores the latest state in a JSON file.

## Requirements

- Python 3.10 or newer
- Playwright
- Requests
- A Telegram bot and chat ID

## Installation

Clone or download this repository, then install the dependencies:

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Configuration

Set these environment variables before running the program:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Never publish your bot token or other credentials.

## Usage

Make sure `estado.json` exists and contains a valid JSON object, then run:

```bash
python Monitor.py
```

The program checks the page once, compares the current titles with the saved state, sends notifications for newly detected titles, and updates the saved state.

## Disclaimer

This project monitors publicly accessible webpage content. Detected titles and links are not independently verified, and their appearance does not establish that any claim is authentic.

## Status

Personal learning project built with Python.
