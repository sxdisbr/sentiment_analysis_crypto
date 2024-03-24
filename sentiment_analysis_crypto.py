import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from textblob import TextBlob
import time



# Specify the path to your WebDriver executable
driver_path = r'C:\Users\reinassance\Desktop\geckodriver.exe'

# Initialize the WebDriver service
service = Service(executable_path=driver_path)

# Initialize the WebDriver (Firefox in this example)
driver = webdriver.Firefox(service=service)

# Navigate to the website
driver.get('https://www.bitcoininsider.org/category/ethereum')

# Wait for the dynamic content to load
time.sleep(5)  # Adjust the sleep time as necessary

# Locate the elements containing the headlines
# Update the selector based on the actual page structure
headlines = driver.find_elements(By.CSS_SELECTOR, 'h2')

# Print the text of each headline
for headline in headlines:
    print(headline.text)

# Clean up by closing the browser window
driver.quit()

headlines_str = """
Optimizing Your Crypto Payment Process: Coinremitter's Gas Fee Reduction Strategy
Fidelity Amends Spot Ethereum ETF to Include Staking
Crypto fear and greed index retreats as Algotech token sale spikes
Solana Meme Coin Mania Breaks Records: DEX Volume Surges, Yet Failed Transactions Hit 72%
North Korean Lazarus group funnels over $100 million in Ethereum through sanctioned mixer Tornado Cash in 8 days
Ethereum Shows Signs of Growth Despite FUD
Ripple leaders forecast SEC defeat in Ethereum security saga
Rising dollar spooked bitcoin, but not the entire crypto market
Ripple CEO Predicts Setback For US SEC In Ethereum Case, Similar To XRP
Google adding Ethereum Name Service data into search results through Etherscan
Estonia’s crypto service providers face new regulations as government approves bill
Why Now? Crypto Lawyer Uncovers Reasons For Ethereum Probe By SEC
Rumors Swirl As North Korea’s ETH Transfer To BlackRock Via Tornado Cash Sparks Speculation
A16z Crypto Lawyer Unleashes Scathing Attack On US SEC, Spot Ethereum ETF In Danger?
Chainlink integrates EigenLayer liquid restaking protocol Renzo
Ethereum, Algorand prices show potential, BlockDAG presale clocks over $6M
Union: The Sovereign Interoperability Layer of the Interchain Future
Ethereum growth slumps before ETF nod, experts bet on Algotech
Crypto finished its pullback thanks to the Fed
Ethereum In Regulatory Hot Seat: SEC Security Classification Looms
"""

# Split the string into a list by newlines
headlines = headlines_str.strip().split('\n')

data = []

for headline in headlines:
    analysis = TextBlob(headline)
    sentiment_score = analysis.sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else 'Negative' if sentiment_score < 0 else 'Neutral'
    print(f"Headline: {headline}")
    print(f"Sentiment: {sentiment}")
    print("")
    data.append({"Headline": headline, "Sentiment": sentiment})

df = pd.DataFrame(data)

print(df)

# Count the occurrences
sentiment_counts = df['Sentiment'].value_counts()
print(sentiment_counts)

# Plot the data
sns.countplot(x='Sentiment', data=df)
plt.title('Distribution of Headline Sentiments')
plt.show()

# Save the data to csv
df.to_csv('headlines_sentiment_analysis.csv', index=False)
