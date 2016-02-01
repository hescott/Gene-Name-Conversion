#function to print list to a file, lifted from 
#stack overflow http://stackoverflow.com/questions/8261590/write-list-to-a-text-file-preserving-names-r


require(org.Mm.eg.db)


fn2list <- function(x, fil){ z <- deparse(substitute(x))
                          nams=names(x) 
                    for (i in seq_along(x) ){ cat(nams[i], "\t",  x[[i]], "\n", 
                                             file=fil, append=TRUE) }
                           }

#each of these transformations came from BioConductor
#http://bioconductor.org/packages/release/data/annotation/manuals/org.Mm.eg.db/man/org.Mm.eg.db.pdf

# entrez gene id to ensemble gene accession
entrez_ensembl <- org.Mm.egENSEMBL
mapped_entrez_ensembl <- mappedkeys(entrez_ensembl)
entrez2ensembl <- as.list(entrez_ensembl[mapped_entrez_ensembl])


fn2list(entrez2ensembl, "/Users/hescott/Gene-Name-Conversion/Mouse/Mm_entrez2ensembl.txt")

#ensemble gene accession id to entrez gene id
ensembl_entrez <- org.Mm.egENSEMBL2EG
mapped_ensembl_entrez <- mappedkeys(ensembl_entrez)
ensembl2entrez <- as.list(ensembl_entrez[mapped_ensembl_entrez])

fn2list(ensembl2entrez, "/Users/hescott/Gene-Name-Conversion/Mouse/Mm_ensembl2entrez.txt")

#entrez to ensemble protein accession
entrez_ensemblprotein <- org.Mm.egENSEMBLPROT
mapped_entrez_ep <- mappedkeys(entrez_ensemblprotein)
entrez2ensemblprotein <- as.list(entrez_ensemblprotein[mapped_entrez_ep])


fn2list(entrez2ensemblprotein, "/Users/hescott/Gene-Name-Conversion/Mouse/Mm_entrez2ensemblprotein.txt")

#ensemble protein accession to entrez 
ensemblprotein_entrez <- org.Mm.egENSEMBLPROT2EG
mapped_ep_entrez <- mappedkeys(ensemblprotein_entrez)
ensemblprotein2entrez <- as.list(ensemblprotein_entrez[mapped_ep_entrez])

fn2list(ensemblprotein2entrez, "/Users/hescott/Gene-Name-Conversion/Mouse/Mm_ensemblprotein2entrez.txt")


#entrez to uniprot
entrez_uniprot <- org.Mm.egUNIPROT
mapped_entrez_uniprot <- mappedkeys(entrez_uniprot)
entrez2uniprot <- as.list(entrez_uniprot[mapped_entrez_uniprot])

fn2list(entrez2uniprot, "/Users/hescott/Gene-Name-Conversion/Mouse/Mm_entrez2uniprot.txt")

