Get Vasari letters from Fondazione Memofonte with Beautiful Soup (Python)

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

Letters.csv and letters_2.csv are containing all the 1151 letters (letter_2 improved html tag removal)

Bartoli.csv, Borghini.csv, Giambullari.csv and Vasari-no_copies.csv are containing the letters of these authors only. 

Vasari_all.csv 	contains the letters written by Vasari and the copies by his nephew. 
Vcopies.csv 	contains the copies by the nephew only. 

The author information was retrieved by the column "Intestazione".


-----------------------------------------------------------------------------

Description of folders:

-------------------- Vasari_letters
Containing all 1151 letters
Named: author_letternumber.txt



-------------------- Vasari_letters_csv
Containing several csv files, either with all letters, or a subcorpus, named accordingly



-------------------- Vasari_letters_vite
Containing all the letters plus all artist biographies as single .txt files



-------------------- Vasari_letters8
Containing all the letters grouped by the 8 author 
Bartoli, Borghini, Giambullari, Minerbetti, Sanga, Vasari, Vcopy, other



-------------------- Vasari_letters8_vite
Containing all the letters grouped by the 8 author 
Bartoli, Borghini, Giambullari, Minerbetti, Sanga, Vasari, Vcopy, other
Plus all artist biographies as single .txt files



--------------------- Vasari_nephew_letters
Containing the letters from nephew only
