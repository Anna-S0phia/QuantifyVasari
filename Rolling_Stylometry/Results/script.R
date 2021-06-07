# This script is the final script we have used to both evaluate and run the Rolling Stylo method. Only the dataset vary. 

# Install and upload the package 
install.packages("stylo")
library(stylo)

# First method in the package: SVM
rolling.classify(write.png.file = TRUE, classification.method = "svm", mfw=100, training.set.sampling = "normal.sampling", slice.size = 5000, slice.overlap = 4500)

# Second method in the package: SNC
rolling.classify(write.png.file = TRUE, classification.method = "nsc", mfw=100, training.set.sampling = "normal.sampling", slice.size = 5000, slice.overlap = 4500)

# Third method in the package: Delta
rolling.classify(write.png.file = TRUE, classification.method = "delta", mfw=100, training.set.sampling = "normal.sampling", slice.size = 5000, slice.overlap = 4500)
