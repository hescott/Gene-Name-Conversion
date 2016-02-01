#function to print list to a file, lifted from 
#stack overflow http://stackoverflow.com/questions/8261590/write-list-to-a-text-file-preserving-names-r

require(org.Sc.sgd.db)

fn2list <- function(x, fil){ z <- deparse(substitute(x))
                          nams=names(x) 
                    for (i in seq_along(x) ){ cat(nams[i], "\t",  x[[i]], "\n", 
                                             file=fil, append=TRUE) }
                           }

#each of these transformations came from BioConductor
#https://www.bioconductor.org/packages/release/data/annotation/manuals/org.Sc.sgd.db/man/org.Sc.sgd.db.pdf


# SGD ORF name to ensemble gene accession
sgd_ensembl <- org.Sc.sgdENSEMBL
mapped_sgd_ensembl <- mappedkeys(sgd_ensembl)
sgd2ensembl <- as.list(sgd_ensembl[mapped_sgd_ensembl])

fn2list(sgd2ensembl, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_sgd2ensembl.txt")

#ensemble gene accession id to SGD ORF
ensembl_sgd <- org.Sc.sgdENSEMBL2ORF
mapped_ensembl_sgd <- mappedkeys(ensembl_sgd)
ensembl2sgd <- as.list(ensembl_sgd[mapped_ensembl_sgd])

fn2list(ensembl2sgd, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_ensembl2sgd.txt")



#SGD ORF to ensemble protein accession
sgd_ensemblprotein <- org.Sc.sgdENSEMBLPROT
mapped_sgd_ep <- mappedkeys(sgd_ensemblprotein)
sgd2ensemblprotein <- as.list(sgd_ensemblprotein[mapped_sgd_ep])


fn2list(sgd2ensemblprotein, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_sgd2ensemblprotein.txt")

#ensemble protein accession to SGD ORF
ensemblprotein_sgd <- org.Sc.sgdENSEMBLPROT2ORF
mapped_ep_sgd <- mappedkeys(ensemblprotein_sgd)
ensemblprotein2sgd <- as.list(ensemblprotein_sgd[mapped_ep_sgd])

fn2list(ensemblprotein2sgd, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_ensemblprotein2sgd.txt")



#SGD ORF to uniprot
sgd_uniprot <- org.Sc.sgdUNIPROT
mapped_sgd_uniprot <- mappedkeys(sgd_uniprot)
sgd2uniprot <- as.list(sgd_uniprot[mapped_sgd_uniprot])

fn2list(sgd2uniprot, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_sgd2uniprot.txt")


#sgd to entrez
sgd_entrez <- org.Sc.sgdENTREZID
mapped_sgd_entrez <- mappedkeys(sgd_entrez)
sgd2entrez <- as.list(sgd_entrez[mapped_sgd_entrez])

fn2list(sgd2entrez, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_sgd2entrez.txt")


#sgd to gene name
sgd_genename <- org.Sc.sgdGENENAME
mapped_sgd_genename <- mappedkeys(sgd_genename)
sgd2genename <- as.list(sgd_genename[mapped_sgd_genename])

fn2list(sgd2genename, "/Users/hescott/Gene-Name-Conversion/Yeast/Sc_sgd2genename.txt")
