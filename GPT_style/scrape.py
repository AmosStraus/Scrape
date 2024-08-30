import requests
from bs4 import BeautifulSoup

def get_address(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try different common sections where addresses are usually found
        possible_sections = ['footer', 'section', 'div']
        for section in possible_sections:
            # Look for common tags and classes
            elements = soup.find_all(section)
            for element in elements:
                # Check if the element contains address-like text
                text = element.get_text(strip=True)
                if 'address' in text.lower() or 'location' in text.lower():
                    return text
        
        return 'Address not found'
    except Exception as e:
        return f'Error: {e}'

# List of farm websites
farms = [
    ("Wolki Farm", "https://wolkifarm.com.au/","Australia"),
    ("Ethical Farmers", "https://www.ethicalfarmers.com.au/","Australia"),
    ("Hunter Natural", "https://hunternatural.com.au/","Australia"),
    ("The Gathered Green", "http://www.thegatheredgreen.com.au","Australia"),
    ("Coogah Harvest", "https://www.coogahharvest.com.au/","Australia"),
    ("Charlton Harvest", "https://www.charltonharvest.com.au/our-farm","Australia"),
    ("The food farm", "https://thefoodfarm.com.au/","Australia"),
    ("Bello Beef", "https://bellobeef.com.au","Australia"),
    ("Living Acres", "http://Livingacres.com.au","Australia"),
    ("Box Gum Grazing", "http://Boxgumgrazing.com.au","Australia"),
    ("Morelands lamb", "http://Moorlandslamb.com.au","Australia"),
    ("Green Hill Organic meat", "http://greenhillorganicmeat.com.au","Australia"),
    ("Canowindra Farms", "http://canowindrafarms.com.au","Australia"),
    ("Branch and Burrow", "http://branchandburrow.com.au","Australia"),
    ("Maleny Black Angus", "https://malenyblackangusbeef.com.au/","Australia"),
    ("Bannock Brae Meats", "https://www.bannockbrae.com.au/","Australia"),
    ("Eastwell Farms", "http://www.eastwellfarms.com.au","Australia"),
    ("Gleneden Farm", "http://www.glenedenfarm.com.au","Australia"),
    ("Echo Valley Farm", "https://www.echovalley.com.au","Australia"),
    ("Lakey Farm", "https://lakeyfarm.com/","Australia"),
    ("Shipwreck Farm", "https://www.shipwreckcoastfarm.com/","Australia"),
    ("Wattle View Farm", "https://wattleviewfarm.com.au","Australia"),
    ("Tom's Paddock", "https://www.otwayprime.com.au/","Australia"),
    ("Otway Prime", "http://www.otwayprime.com.au","Australia"),
    ("Cherry Tree Organics", "http://www.cherrytreeorganics.com.au","Australia"),
]

# Collect addresses
addresses = []
for name, url, _ in farms:
    address = get_address(url)
    print(name, url, address)
    addresses.append((name, url, address))

# Print or save results
import pandas as pd
df = pd.DataFrame(addresses, columns=['Name', 'Website', 'Address'])
df.to_csv('farm_addresses.csv', index=False)
print(df)
