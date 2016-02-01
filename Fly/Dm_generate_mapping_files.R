#function to print list to a file, lifted from 
#stack overflow http://stackoverflow.com/questions/8261590/write-list-to-a-text-file-preserving-names-r

require(org.Dm.eg.db)

fn2list <- function(x, fil){ z <- deparse(substitute(x))
                          nams=names(x) 
                    for (i in seq_along(x) ){ cat(nams[i], "\t",  x[[i]], "\n", 
                                             file=fil, append=TRUE) }
                           }

#each of these transformations came from BioConductor
#https://www.bioconductor.org/packages/release/data/annotation/manuals/org.Dm.eg.db/man/org.Dm.eg.db.pdf


# entrez gene id to ensemble gene accession
entrez_ensembl <- org.Dm.egENSEMBL
mapped_entrez_ensembl <- mappedkeys(entrez_ensembl)
entrez2ensembl <- as.list(entrez_ensembl[mapped_entrez_ensembl])

fn2list(entrez2ensembl, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_entrez2ensembl.txt")

#ensemble gene accession id to entrez gene id
ensembl_entrez <- org.Dm.egENSEMBL2EG
mapped_ensembl_entrez <- mappedkeys(ensembl_entrez)
ensembl2entrez <- as.list(ensembl_entrez[mapped_ensembl_entrez])

fn2list(ensembl2entrez, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_ensembl2entrez.txt")

#entrez to ensemble protein accession
entrez_ensemblprotein <- org.Dm.egENSEMBLPROT
mapped_entrez_ep <- mappedkeys(entrez_ensemblprotein)
entrez2ensemblprotein <- as.list(entrez_ensemblprotein[mapped_entrez_ep])


fn2list(entrez2ensemblprotein, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_entrez2ensemblprotein.txt")

#ensemble protein accession to entrez 
ensemblprotein_entrez <- org.Dm.egENSEMBLPROT2EG
mapped_ep_entrez <- mappedkeys(ensemblprotein_entrez)
ensemblprotein2entrez <- as.list(ensemblprotein_entrez[mapped_ep_entrez])

fn2list(ensemblprotein2entrez, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_ensemblprotein2entrez.txt")



#entrez to uniprot
entrez_uniprot <- org.Dm.egUNIPROT
mapped_entrez_uniprot <- mappedkeys(entrez_uniprot)
entrez2uniprot <- as.list(entrez_uniprot[mapped_entrez_uniprot])

fn2list(entrez2uniprot, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_entrez2uniprot.txt")



#entrez to FlyBase accesion number
entrez_flybase <- org.Dm.egFLYBASE
mapped_entrez_flybase <- mappedkeys(entrez_flybase)
entrez2flybase <- as.list(entrez_flybase[mapped_entrez_flybase])

fn2list(entrez2flybase, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_entrez2flybase.txt")


#FlyBase to entrez
flybase_entrez <- org.Dm.egFLYBASE2EG
mapped_flybase_entrez <- mappedkeys(flybase_entrez)
flybase2entrez <- as.list(flybase_entrez[mapped_flybase_entrez])

fn2list(flybase2entrez, "/Users/hescott/Gene-Name-Conversion/Fly/Dm_flybase2entrez.txt")
