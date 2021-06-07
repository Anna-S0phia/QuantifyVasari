# Get Vasari letters from Fondazione Memofonte with Beautiful Soup (Python)

The letters are extracted from Fondazione Memofonte at Url https://www.memofonte.it/ricerche/giorgio-vasari/


The collection contains 1151 letters in total. 
They are available under the following URL by augmenting "id=X":
https://www.memofonte.it/home/ricerca/singolo_17.php?id=1& 


The csv_files contain the following columns: 
"Numero d'ordine", "Data", "Intestazione", "Segnatura", "Fonte", "Bibliografia"

Numero d'ordine: unique letter-id, ordered chronologically
Data: 		Date of the letter
Intestazione: 	Who has written to whom and from where to where
Segnatura: 	Signature form the archive providing the letter
Fonte: 		text of the letter
Bibliographie: 	further reading, letter mentioned/printed in these books

all_etters.csv is containing all the 1151 letters 

