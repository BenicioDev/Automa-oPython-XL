from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Firefox()
driver.get("https://www.amazon.com.br/s?k=Iphones&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2LPCNPK06N4NZ&sprefix=iphone%2Caps%2C240&ref=nb_sb_noss_1")

#Extrair titulos produtos
title = driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')

#Extrair preços produtos
price = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')

# Criar Planilhas
workbook = openpyxl.Workbook()
# Criando página produtos
workbook.create_sheet("Produtos")
# Selecionando página produtos___
planilhaProdutos = workbook['Produtos']
# Inserindo informações na planilha
planilhaProdutos['A1'].value = 'TITLE'
planilhaProdutos['B1'].value = 'PRICE'
workbook.save('Produtos.xlsx')

for titulo, preco in zip(title, price):
       planilhaProdutos.append([titulo.text, preco.text])

workbook.save('Produtos.xlsx')