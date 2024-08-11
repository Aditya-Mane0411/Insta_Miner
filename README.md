# Insta_Miner
# InstaMiner

InstaMiner is a Python-based tool designed for scraping Instagram profiles. It allows users to extract and download key information, such as profile data, followers, followings, and posts. This project utilizes the Instaloader library to interact with Instagram's data.

## Features

- **Profile Information**: Extract detailed profile information including username, user ID, bio, and external URL.
- **Followers and Followings**: Fetch a list of followers and followings for a given profile.
- **Streamlit Interface**: Simple and interactive GUI for running the scraper without the need for complex command-line inputs.

## Requirements

- Python 3.6+
- Instaloader
- Streamlit

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/insta_miner.git
    cd insta_miner
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:

    ```bash
    streamlit run insta_miner.py
    ```

## Usage

1. **Launch the Streamlit App**: After running the `streamlit run insta_miner.py` command, the Streamlit interface will open in your browser.

2. **Input Profile Name**: Enter the Instagram username you want to scrape.

3. **Extract Data**: Click on the buttons to fetch profile details, followers, followings, or to download posts.

4. **View Results**: All extracted data will be displayed within the Streamlit interface
