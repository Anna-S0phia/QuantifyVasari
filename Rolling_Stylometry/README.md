---
title: "README"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## Rolling Stylometry
### Presentation of the function 
The Rolling stylometry is a function from the stylo package which has been designed by researchers from the Computational Stylistics Group. The function studies the authorship of a text by comparing the text which the authorship is studies with other texts from potential author candidates. 

### Use of the function 
As explained in the tutorial (see sources), we have used two subfolders: 

* **reference_set**: containing the text we want to analyze, that-is-to-say the Lives of Vasari. For the evaluation of the method, we have only used Vasari's letters. 

* **test_set**: containing the texts from potential candidates

NB. As the two subfolders are different between the evaluation and the results, you can find one folder containing the reference_set and test_set for both the evaluation and the results. 

---------------------------------------------------------

### Sources: 

* **the Computational Stylistic Group**: https://computationalstylistics.github.io/

* **the description of the function**: https://github.com/computationalstylistics/preprints/blob/master/Eder_Rolling_stylometry_draft.pdf

* **a tutorial** to use the function: https://computationalstylistics.github.io/blog/rolling_stylometry/



