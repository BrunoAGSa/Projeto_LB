from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
from Bio.Data import CodonTable
import Blast

# Introduzir o nome do ficheiro GeneBank de cada gene:

while(True):

    print()
    print('''Digite 'sair' em letras minusculas para sair do programa

    Para o gene PPAR o nome do ficheiro é: PPAR''')
    print()
    nomeFicheiro = input("Introduza o nome do Ficheiro GeneBank: ")

    try:

        if nomeFicheiro == "sair":
            
            break
        
        else:

            # Importar a sequência
            record = SeqIO.read(nomeFicheiro + ".gb", "gb")
            sequencia = record.seq

            print("Explorar a informação associada ao ficheiro GeneBank do gene " + str(nomeFicheiro))
            print()
            print("Sequência Nucleotídica:")
            print()
            print(sequencia)

            # Identificação da sequencia

            # Id (Accession number)

            print()
            print("Accession Number: " + record.id)
            print()
            print("Descrição: " + record.description)

            # Comprimento da sequência

            comprimento = len(sequencia)
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
            print("Tradução da proteína " + str(nomeFicheiro))
            print()
            # traducao = codon.table.unambiguous_dna_by_name["Standard"]
            traducao = cds.translate(table = "Standard")
            print(traducao)
            print()

            # Obtenção do id da proteina

            qualificadores = record.features[4].qualifiers
            for key, value in qualificadores.items():
    
                if key == "protein_id":
                    idProteina = "".join(value)

            
            # Escrita do ficheiro fasta com a designação e a sequencia da proteina

            with open(idProteina + '.fasta', 'w') as save_file:
                
                save_file.write(">" + idProteina + "\n" + str(traducao))
                    
            print("Resultados do Blast")
            print()

            Blast.blast(idProteina)
   
    except:

        print("O nome introduzido não é válido")
                    
                

