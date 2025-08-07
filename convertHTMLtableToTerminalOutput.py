import requests
from bs4 import BeautifulSoup

def print_grid(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find first table
    table = soup.find('table')
    data = []
    if table:
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            cols_text = [ele.text.strip() for ele in cols]
            if cols_text: # Ensure the row is not empty
                data.append(cols_text)
    del data[0] # Remove header row
    # Find largest x- and y-coordinates
    longest_y = int(data[0][2])
    longest_x = int(data[0][0])
    for row in data:
        if int(row[2])>longest_y:
            longest_y = int(row[2])
        if int(row[0])>longest_x:
            longest_x = int(row[0])
    # Create sorted 2Dlist with spaces as default
    sorted = [[' ' for _ in range(longest_x + 1)] for _ in range(longest_y + 1)]
    for row in data:
        sorted[int(row[2])][int(row[0])] = row[1]
    condensed = ['']
    for row in sorted:
        condensed.append(''.join(row))
    condensed.reverse()
    for row in condensed:
        print(row)

url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
print_grid(url)