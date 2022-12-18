# Ver: https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import webbrowser

def blast():

    sequence_data = open("NP_056953.fasta").read()

    result_handle = NCBIWWW.qblast("blastp", "nr", sequence_data)
    print(result_handle)

    with open('results.xml', 'w') as save_file:

        blast_results = result_handle.read()
        save_file.write(blast_results)

    E_VALUE_THRESH = 1e-20
    for record in NCBIXML.parse(open("results.xml")):
        if record.alignments:
            print("\n")
            print("query: %s" % record.query[:100])
            for i in range(0, 29):
                for align in record.alignments:
                    for hsp in align.hsps:
                        if hsp.expect < E_VALUE_THRESH:
                            print("match: %s " % align.title[:100])
    bin = webbrowser.open('results.xml', 'rb')
