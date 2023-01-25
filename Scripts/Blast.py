def blast(idProteina):

    sequence_data = open(idProteina + ".fasta").read()
    print("A consultar o NCBI, por favor Aguarde...")
    result_handle = NCBIWWW.qblast("blastp", "nr", sequence_data)
    print(result_handle)
    nomeFicheiro = 'results_' + str(idProteina) + '.xml'
    with open(nomeFicheiro, 'w') as save_file:
        blast_results = result_handle.read()
        save_file.write(blast_results)

    E_VALUE_THRESH = 1e-20
    for record in NCBIXML.parse(open(nomeFicheiro)):
        if record.alignments:
            print("\n")
            print("query: %s" % record.query[:100])
            #for i in range(0, 9):
            for align in record.alignments:
                for hsp in align.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        print("match: %s " % align.title[:100])
                            
    bin = webbrowser.open(nomeFicheiro, 'rb')
