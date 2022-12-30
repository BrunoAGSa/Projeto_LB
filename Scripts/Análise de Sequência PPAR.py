from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
from Bio.Data import CodonTable
import Blast

# Importar a sequência
record = SeqIO.read("ARL15.gb", "gb")
ppar = record.seq

print("Explorar a informação associada ao ficheiro GeneBank do gene PPAR gamma")
print()
print("Sequência Nucleotídica:")
print()
print(ppar)

# Identificação da sequencia

# Id (Accession number)

print()
print("Accession Number: " + record.id)
print()
print("Descrição: " + record.description)

# Comprimento da sequência

comprimento = len(ppar)
print()
print("Esta sequência tem " + str(comprimento) + " nucleótidos")

# Analise das Features e Annotations

print()
print("Número de Annotations e Features contidas no ficheiro GeneBank")
print()
print("Annotations = " + str(len(record.annotations)))
print()
print("Features = " + str(len(record.features)))
print()
print("Organismo = " + record.annotations["source"])
print()
print("Palavras-chave = " + "".join(record.annotations["keywords"]))
print()
print("Features associadas ao ficheiro = " + str(record.features))
print()
print("Listar as features Type e Location")
print()
for i in record.features:

    print(i.type)
    print(i.location)

# Extração do ficheiro GeneBank da sequência codificante

print()
print("Extração do CDS do ficheiro GeneBank")
print()
listaCDS = []
for i in range (len(record.features)):

    if record.features[i].type == "CDS":

        listaCDS.append(i)

for k in listaCDS:
    cds = record.features[k].extract(record.seq)
    print(cds)

# Antes de traduzir verificar que o CDS é divisível por 3

print()
print("Divisão do CDS por 3 = " + str(len(cds)/3))
print()
print("Tradução da proteína PPAR gamma")
print()
# traducaoPPAR = codon.table.unambiguous_dna_by_name["Standard"]
traducaoPPAR = cds.translate(table = "Standard")
print(traducaoPPAR)
print()
# Escrita do ficheiro fasta com a designação e a sequencia da proteina

with open('NP_056953.fasta', 'w') as save_file:
    
    save_file.write(">NP_056953.2\n" + str(traducaoPPAR))
        
print("Resultados do Blast")
print()

Blast.blast()
        
    
