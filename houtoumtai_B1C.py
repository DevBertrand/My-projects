import requests
from bs4 import BeautifulSoup


def mon_scrapping(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        all_quotes = []
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            all_quotes.append((text, author, tags))
        return all_quotes
    else:
        print("Erreur lors de la requête:", response.status_code)
        return []


base_url = 'https://quotes.toscrape.com/page/'
page_number = 1


url = f"{base_url}{page_number}/"
first_page_quotes = mon_scrapping(url)


for text, author, tags in first_page_quotes:
    print("+" + "-" * 50 + "+")
    print(f"| Citation : {text}")
    print(f"| Auteur : {author}")
    print("| Tags : " + ", ".join(tags))
    print("+" + "-" * 50 + "+")

user_input = input("Voulez-vous voir les citations des autres pages ? (YES/NO) : ").strip().upper()

if user_input == "YES":
    all_quotes = first_page_quotes
    page_number = 2
    while True:
        url = f"{base_url}{page_number}/"
        quotes = mon_scrapping(url)
        
        if not quotes:   
            break
        
        all_quotes.extend(quotes)
        for text, author, tags in quotes:
            print("+" + "-" * 50 + "+")
            print(f"| Citation : {text}")
            print(f"| Auteur : {author}")
            print("| Tags : " + ", ".join(tags))
            print("+" + "-" * 50 + "+")
        
        page_number += 1
else:
    print("Affichage terminé pour la première page.")


    ## explication de mon travail : Tout d'abord, j'ai scrappé toutes citations de la première page. Ensuite, 
    # on demande à l'utilisateur si il souhaite aussi l'affichage des citaions des autres pages. Si il ecrit YES, 
    # le scrapping continu et affiche toutes les citations des autres pages, si il ecrit NO, le scrapping s'arrête
    # sur les citations de la première page.
    # Editeur utilisé : VS Code