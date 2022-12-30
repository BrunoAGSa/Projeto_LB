from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio import AlignIO
from Bio import Phylo

# Recolher sequências e fazer alinhamento

print()
print('''Recolher a sequência proteica dos primeiros três hsp do blast

        Recolher do NCBI base de dados proteína as sequências proteicas
        do PPARa e PPARd para as mesmas espécies

        ir ao https://www.ebi.ac.uk/Tools/msa/mafft/ e proceder com o
        alinhamento de sequências com as opções Default, guardar o alinhamento
        em formato fasta e guardar a arvore filogenética em formato newick''')
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

            # Filogenias

            print()
            print('''Cálculo da Filogenia utilizando este alinhamento no
            https:\\ngphylogeny.fr
            
            Comparação da Arvore calculada pelo EBI Vs Arvore calculada no NGPylogeny
            
            Árvore EBI Neighbor Joining''')
            print()
            
            while(True):

                nomeFicheiroArvoreNJ = input("Digite o nome do ficheiro que dá origem à árvore Filogenética NJ: ")
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
                            
                            nomeFicheiroArvorePhyML = input("Digite o nome do ficheiro que dá origem à árvore Filogenética PhyML: ")
                            
                            try:

                                if nomeFicheiroArvorePhyML == "sair":

                                    break

                                else:
                                    
                                    print()
                                    arvoreEBI = Phylo.read(nomeFicheiroArvorePhyML + ".newick", "newick")
                                    print(Phylo.draw_ascii(arvoreEBI))

                                    # Análise dos resultados

                                    print()
                                    print('''Os dois métodos de cálculo de filogenia deram árvores iguais, as sequências estão agrupadas por tipo e não por
                            espécie. A sequência do tipo gamma e delta são mais próximas do que a sequência do tipo alfa.''')
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

