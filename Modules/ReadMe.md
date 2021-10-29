# Lab07-ReadMe

For this Lab I choose a Powershell module called "PSWritePDF" which helps convert your text to a PDF format, let's you split, merge, and convert the PDF to a Text format.

### First Use- CreadingPDFs

My first file is Creating PDF's. To create a new PDF use the `New-PDF` and to add text use `New-PDFText -Text`. You can also customize font type and color. A sample from the code is shown below:

`New-PDF { New-PDFText -Text 'Hello ', 'World' }`

After executing the file we get two PDFs in out Module folder. The first is Example01_Simple.pdf and second is Example02_Simple.pdf, these files will then be use to merge the two PDFs together.

### Second Use- mergePDF

For second file we will merge the two PDFs which we got from our first file- CreatingPDFs. To merge two files first you will have to disclose their paths and then their output location with file name. **_Remember outputting will re-write the file if already present. If not the program will create the file for you._**
Then finally by calling `Merge-PDF` function we can get both our files merged. Code for second file is shown below:

```
$FilePath1 = "$PSScriptRoot\Example01_Simple.pdf"
$FilePath2 = "$PSScriptRoot\Example02_Simple.pdf"
$OutputFile = "$PSScriptRoot\Output\OutputDocument.pdf"
Merge-PDF -InputFile $FilePath1, $FilePath2 -OutputFile $OutputFile
```

### Third Use- splitPDF

The third use of this module is to split the pdf. This is achieved by `Split-PDF` function. In this lab I will split the recently merged PDF from second file to two different output documents. The newly split documents can be found inside Modules folder. The code for Splitting the document is shown below:

`Split-PDF -FilePath "$PSScriptRoot\Output\OutputDocument.pdf" -OutputFolder 'C:\it3038c-scripts\Modules'`

### Fourth Use- SaveToText

The fourth usage of this module is to convert the text from the PDF to a text string that you use in Powershell. This is achieved by `Convert-PDFToText` function and by specifying the file path. Full code is shown below:
`Convert-PDFToText -FilePath "$PSScriptRoot\Output\OutputDocument.pdf"`
