#Creating First PDF...
New-PDF {
    New-PDFText -Text 'Hello ', 'World' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
    New-PDFText -Text 'Testing adding text. ' -Font HELVETICA -FontColor RED
    New-PDFText -Text 'This text is going by defaults.', ' This will continue...', '... and here as well.'
    New-PDFList -Indent 3 {
        New-PDFListItem -Text 'Test'
        New-PDFListItem -Text 'Test 2nd'
    }

    New-PDFText -Text 'Hello ', 'World' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
    New-PDFText -Text 'Testing adding text. '-Font HELVETICA -FontColor RED
    New-PDFText -Text 'This text is going by defaults.', ' This will continue...', '...and here as well.'
    New-PDFList -Indent 3 {
        New-PDFListItem -Text 'Test'
        New-PDFListItem -Text 'Test 2nd'
    }
} -FilePath "$PSScriptRoot\Example01_Simple.pdf" -Show

#Creating Second PDF...
New-PDF {
    New-PDFText -Text 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    New-PDFText -Text ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    New-PDFText -Text 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea'
    New-PDFText -Text 'commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'
    New-PDFText -Text 'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,'
    New-PDFText -Text 'sunt in culpa qui officia deserunt mollit anim id est laborum.'
} -FilePath "$PSScriptRoot\Example02_Simple.pdf" -Show