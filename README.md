# Crypto News Sentiment Analysis

This repository uses Selenium to scrape crypto headlines and then evaluates the general sentiment with three categories: Neutral, Positive, and Negative with TextBlob.

## Project Overview

This project focuses on scraping cryptocurrency news headlines from news websites and analyzing their sentiment (Positive, Neutral, Negative) using TextBlob. The goal is to identify prevailing sentiments in the crypto market as reported by the news. This analysis can help users gauge the general market sentiment towards the crypto market as a whole in a given period of time.

## Features

- Scrapes cryptocurrency news headlines.
- Analyzes sentiment of each headline.
- Saves the headlines and sentiments to a DataFrame.
- Counts the number of Positive, Neutral, and Negative headlines.

## Getting Started

### Prerequisites

Before running this project, you need to have Python installed on your system. Additionally, the following Python libraries are required:

- Selenium
- Pandas
- TextBlob
- Matplotlib
- Seaborn

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sxdisbr/sentiment_analysis_crypto.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd sentiment_analysis_crypto
    ```

3. **Set up a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Unix/macOS
    venv\Scripts\activate  # On Windows
    ```

4. **Install the required packages using pip:**

    ```sh
    pip install selenium pandas seaborn matplotlib textblob
    ```

### Usage

To run the sentiment analysis, execute the script from the command line:

```sh
python sentiment_analysis_crypto.py
```

## Contributing

Contributions to this project are welcome! Here are a few ways you can help:

- **Report bugs and issues**: Open issues in the [GitHub repository](https://github.com/sxdisbr/sentiment_analysis_crypto/issues) to report bugs or issues you've encountered.
- **Suggest new features or improvements**: Have ideas for enhancing the project? Open an issue to share your suggestions.
- **Contribute code**: Fork the repository, make your changes, and submit a pull request. Your contributions are appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Disclaimer

This analysis is for educational purposes only and not financial advice. Always conduct your own research before making any investment decisions.

## Acknowledgments

- **Selenium**: Thanks to the Selenium library for enabling web scraping of dynamic content rendered by JavaScript.
- **Pandas**: Gratitude to Pandas for providing an exceptional toolkit for data analysis.
- **Matplotlib & Seaborn**: Appreciation for Matplotlib and Seaborn for their excellent visualization capabilities.
- **TextBlob**: Love for the TextBlob library for simplifying sentiment analysis.
- **News Outlets**: Acknowledgment to all news outlets and websites that serve as sources for cryptocurrency news.
