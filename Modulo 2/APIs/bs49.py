import requests
from bs4 import BeautifulSoup

url = "https://panini.com.br/desconto-exclusivo-comics"
response = requests.get(url)
quantidade = []



print("status", response.status_code)

if response.status_code == 200:
    print("pagina carregada com sucesso!")
    soup = BeautifulSoup(response.text,"html.parser")


    links = soup.find_all("a", class_= "product-item-link") 

    count = 0
    for link in links:
        href = link.get ("href")
        texto = link.get_text(strip=True)
        if href:
            quantidade.append(href)
           

else:
    print("erro ao carregar a pagina")

print(quantidade) 

bolas = len(quantidade)
bolas2 = 0


while bolas2 < bolas:
    print(f"{quantidade[bolas2]}\n")
    bolas2 +=1

print(f"Quantidade de quandrinhos disponiveis para compra: {bolas}")

