'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_starting_url():
    # Return 3 random lower case chars with dns format
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    print(url)
    return url

def handle_local_links(url, link):
    # Join local links to url if needed
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

def get_links(url):
    # Scrape 3 letter site with beautifulsoup
    try:
        resp = requests.get(url)                    # Request data from url
        soup = bs.BeautifulSoup(resp.text, 'lxml')  # Parse text from site
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]  # Get all links from body
        links = [handle_local_links(url, link) for link in links]
        links = [string(link.encode('ascii')) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links')
        return []
    except Exception as e:
        print(str(e))
        return []

def main():
    # Multiprocess scraping and storage
    how_many = 50
    p = Pool(processes = how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()
    
    with open('urls.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    main()