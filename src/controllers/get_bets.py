import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from collections import Counter
import pdb


def ultimos_6_numeros_max_sorteados(listaDezenas):
    
    frequencia_elementos = Counter(listaDezenas)
    
    # numeros_mais_frequentes = [numero for numero, _ in frequencia_elementos.most_common(6)]
    numeros_mais_frequentes = [numero for numero, _ in frequencia_elementos.most_common(15)]
    return numeros_mais_frequentes, frequencia_elementos



def ultimos_60_numeros(qtdSorteios):

    PATH = '/Users/caioassis/Downloads/programas/chromedriver'


    cService = webdriver.ChromeService(executable_path=PATH)
    
    chrome_options = webdriver.ChromeOptions()
    
    # chrome_options.add_argument('--headless')  # Adiciona a opção --headless
    # driver = webdriver.Chrome(service=cService, options=chrome_options)
    
    driver = webdriver.Chrome(service=cService)
    driver.minimize_window()

    # driver.get("https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx")
    driver.get("https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx")
    
    listaDezenas = []
    
    for _ in range(qtdSorteios):
        
        numero_data_concurso = driver.find_elements(By.CLASS_NAME,'ng-binding')[18].text
        numero_concurso = numero_data_concurso.split()[1]
        numero_concurso_int = int(numero_concurso)
        
        # dezenasSorteadas = driver.find_elements(By.CLASS_NAME,'ng-binding')[20:26]
        dezenasSorteadas = driver.find_elements(By.CLASS_NAME,'ng-binding')[20:35]
        time.sleep(4)

        for dezena in dezenasSorteadas:
            texto_elemento = dezena.text
            listaDezenas.append(texto_elemento)            

        resposta = driver.find_elements(By.CLASS_NAME,'field-d')
        resposta[0].clear()  # Limpa o campo
        time.sleep(3)
        num_concurso = numero_concurso_int - 1 # diminuindo a cada for o numero do concurso
        
        resposta[0].send_keys(str(num_concurso))# adiciona valor ao campo
        resposta[0].send_keys(Keys.RETURN)# clica no enviar do campo, como se fosse o ENTER

        time.sleep(4)
    
    driver.close()
    
    numeros_mais_sorteados,listaFrequenciaElementos = ultimos_6_numeros_max_sorteados(listaDezenas)
    return numeros_mais_sorteados,listaFrequenciaElementos

if __name__ == "__main__":
    
    qtdSorteios = 15
    listaDezenas, listaFrequenciaElementos = ultimos_60_numeros(qtdSorteios)
    print(listaFrequenciaElementos)
    print(listaDezenas)
