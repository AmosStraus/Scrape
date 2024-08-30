import requests
from bs4 import BeautifulSoup

def get_address(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the footer or contact section directly
        footer = soup.find('footer')
        if footer:
            # Extract text and look for address
            address_text = footer.get_text(strip=True)
            # Simple extraction; adjust regex if needed
            return address_text.split('Location:')[-1].strip() if 'Location:' in address_text else 'Address not found'
        
        return 'Address not found'
    except Exception as e:
        return f'Error: {e}'

# URL of the website to scrape
url = 'https://wolkifarm.com.au/'

# Collect address
# List of farm websites
farms = [
    ("Wolki Farm", "https://wolkifarm.com.au/"),
    ("Ethical Farmers", "https://www.ethicalfarmers.com.au/"),
    # Add other farms...
]

# Collect addresses
addresses = []
for name, url in farms:
    address = get_address(url)
    addresses.append((name, url, address))

# Print or save results
import pandas as pd
df = pd.DataFrame(addresses, columns=['Name', 'Website', 'Address'])
df.to_csv('farm_addresses.csv', index=False)
print(df)