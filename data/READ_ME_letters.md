## Get Vasari letters from Fondazione Memofonte with Beautiful Soup

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

all_letters.csv is containing all the 1151 letters 

### letters folder
contains the .html files

### grouped_letters
contains .txt and .csv files containing all the letters from one author 
list of authors: Vasari, VasariC (= copies by his nephew), Bartoli, Borghini, Giambullari, Sangaletti (Sanga), Minerbetti, 'other' (all other authors)

### formatted folder
contains the data formatted for the methods used

#### formatted_letters folder
contains the letters in the following: author_letternumber.txt

### formatted_vite folder
contains all biographies in the following format: unkown_artist-name.txt
+ the books before the biographies as unkown_Introduction.txt

#### formatted_letters_lives_Ghiberti
contains the formatted letters folder, the formatted vite folder and Ghibertis Commentarii (1447) as a single .txt file
