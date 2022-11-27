from Bio import Entrez
from Bio import Medline

termos_pesquisa = input(" Termos a Pesquisar ")  # input do que queremos pesquisar na Pubmed


Entrez.email = "sa.bruno.2001@gmail.com"     # kinda que obrigatorio
handle = Entrez.esearch(db = "pubmed", term = termos_pesquisa , retmax = 200 )    # pesquisar  db -> Base de dads    term -> O que pesquisar input de cima  retmaax - resultados
record = Entrez.read(handle)    # ler os resultaados 

lista_ids = record["IdList"]   # obter os ids


handle = Entrez.efetch(db = "pubmed", id = lista_ids, rettype = "medline", retmode = "text")   #handle vai devolver varios resultados
records = Medline.parse(handle)                                                             # dai usar o parse aqui 

print()   # linha branca 

for record in records:
    print("Titulo:", record.get("TI", "Vazio"))     # Print segue esta estrutura (abaixo)                                       
    print()                                         #Isto é um dicionario (.get) em que as Keys estão aqui https://biopython.org/docs/1.75/api/Bio.Medline.html
    print("Abstract:", record.get("AB", "Vazio"))   #                      Existem muitas mas achei estas as mais relevantes 
    print("Autores:", record.get("AU", "Vazio"))
    print("Fonte:", record.get("SO", "Vazio"))
    print()
    print()