from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

# Recolher sequências e fazer alinhamento

print()
print('''Recolher do NCBI base de dados proteína as sequências proteicas
        do PPARa e PPARd para as mesmas espécies

        ir ao https://www.ebi.ac.uk/Tools/msa/mafft/ e proceder com o
        alinhamento de sequências com as opções Default, guardar o alinhamento
        em formato fasta e guardar a arvore filogenética em formato newick
        Nome do Ficheiro do Alinhamento: PPARalign
        Nome do Ficheiro da árvore em EBI: arvoreEBINJ
        Nome do Ficheiro da árvore em Phyml: arvorePhyml
        ''')
print()

# Explorar alinhamento
print("Explorar o alinhamento")
print()

while(True):

    print("Digite 'sair' para sair do programa")
    
    print()
    nomeFicheiroAlinhamento = input("Escreva o nome do ficheiro do alinhamento: ")
    print()
    try:
        if nomeFicheiroAlinhamento == "sair":

           break

        else:
            
            alignment = AlignIO.read(nomeFicheiroAlinhamento + ".fasta", "fasta")
            print(alignment)
            print()
            print("Tamanho do Alinhamento: %i " % alignment.get_alignment_length())
            print()
            for record in alignment:
                print("%s - %s" % (record.seq, record.id))

            # Cálculo da matriz de distância e Filogenia
            print()
            print("Cálculo da matriz de distância e Filogenia")
            print()
            calculator = DistanceCalculator("identity")
            MatrizDis = calculator.get_distance(alignment)
            print(MatrizDis)
            print()
            constructor = DistanceTreeConstructor()
            upgmaTree = constructor.upgma(MatrizDis)
            print(Phylo.draw_ascii(upgmaTree))

            # Visualizacao de Filogenias calculadas no EBI e no NJPylogeny

            print()
            print('''Cálculo da Filogenia utilizando este alinhamento no
            https:\\ngphylogeny.fr
            
            Comparação da Arvore calculada pelo EBI Vs Arvore calculada no NGPhylogeny
            
            Árvore EBI Neighbor Joining''')
            print()
            
            while(True):

                nomeFicheiroArvoreNJ = input("Digite o nome do ficheiro da árvore Filogenética EBI: ")
                print()
                try:
                    if nomeFicheiroArvoreNJ == "sair":

                        break

                    else:
                        
                        arvoreEBI = Phylo.read(nomeFicheiroArvoreNJ + ".newick", "newick")
                        print(Phylo.draw_ascii(arvoreEBI))
                        print()
                        print("Árvore NG PhyML")
                        print()
                        
                        while(True):
                            
                            nomeFicheiroArvorePhyML = input("Digite o nome do ficheiro da árvore Filogenética PhyML: ")
                            
                            try:

                                if nomeFicheiroArvorePhyML == "sair":

                                    break

                                else:
                                    
                                    print()
                                    arvoreEBI = Phylo.read(nomeFicheiroArvorePhyML + ".newick", "newick")
                                    print(Phylo.draw_ascii(arvoreEBI))

                                    # Análise dos resultados

                                    print()
                                    print('''Os três métodos de cálculo de filogenia deram árvores semelhantes, onde as sequências estão agrupadas por tipo (alfa, delta e gama) e não por
                            espécie.''')
                                    print()

                            except:

                                print("Nome do ficheiro da árvore filogenética PhyML inválido")
                                print()

                except:
                
                   print("Nome do ficheiro da árvore filogenética NJ inválido")
                   print()

    except:

          print("Nome do ficheiro dos alinhamentos inválido")
          print()

