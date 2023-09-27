# Keyword-Searcher
A few simple Python scripts to search for keywords in PDF and Text files. 

The scripts create a new text file containing the search results in which, first, is listed the count of all the keywords with the names of the files in which the given keyword(s) appear and then, second, the actual keyword search results within context (a few sentences before and after). 

Here is a rundown of the various scripts:

### Keyword-Searcher-A
This code searches for the specified keywords within all PDF files only in the specified directory.

### Keyword-Searcher-B
This code searches for the specified keywords within all PDF files in the specified directory and all its subdirectories.

### Keyword-Searcher-C
This code searches for the specified keywords within all Text files only in the specified directory.

### Keyword-Searcher-D
This code searches for the specified keywords within all Text files in the specified directory and all its subdirectories.

## How to use

### Keyword-Searcher-A
1. Open the Python script in your code editor.
2. In `pdf_directory = '/path/to/pdf/files'`  replace /path/to/pdf/files with the actual directory path.
3. In `keywords = ['keyword1', 'keyword2', 'keyword3']` replace keyword1 etc. with the keywords you want to search for. You can, of course, add more or less keywords; simply continue editing following the same pattern.
4. In `output_text_file = 'output_search_results.txt'` replace output_search_results.txt with the desired name for text file containing the keyword search results. 
5. In `output_directory = '/path/to/output/directory'`  replace /path/to/output/directory with the desired output directory path.
6. Save the script and you're ready to go. 

### Keyword-Searcher-B
1. Open the Python script in your code editor.
2. In `pdf_directory = '/path/to/pdf/files'`  replace /path/to/pdf/files with the actual directory path.
3. In `keywords = ['keyword1', 'keyword2', 'keyword3']` replace keyword1 etc. with the keywords you want to search for. You can, of course, add more or less keywords than two; simply continue adding more keywords following the same pattern.
4. In `output_text_file = 'output_search_results.txt'` replace output_search_results.txt with the desired name for text file containing the keyword search results. 
5. In `output_directory = '/path/to/output/directory'`  replace /path/to/output/directory with the desired output directory path.
6. Save the script and you're ready to go.

### Keyword-Searcher-C
1. Open the Python script in your code editor.
2. In `text_directory = '/path/to/text/files'`  replace /path/to/text/files with the actual directory path.
3. In `keywords = ['keyword1', 'keyword2', 'keyword3']` replace keyword1 etc. with the keywords you want to search for. You can, of course, add more or less keywords than two; simply continue adding more keywords following the same pattern.
4. In `output_text_file = '/path/to/output/directory/output_search_results.txt'` replace /path/to/output/directory/ with the desired output directory path, and replace output_search_results.txt with the desired name for text file containing the keyword search results.
5. Save the script and you're ready to go.

### Keyword-Searcher-D
1. Open the Python script in your code editor.
2. In `text_directory = '/path/to/text/files'`  replace /path/to/text/files with the actual directory path.
3. In `keywords = ['keyword1', 'keyword2', 'keyword3']` replace keyword1 etc. with the keywords you want to search for. You can, of course, add more or less keywords than two; simply continue adding more keywords following the same pattern.
4. In `output_text_file = '/path/to/output/directory/output_search_results.txt'` replace /path/to/output/directory/ with the desired output directory path, and replace output_search_results.txt with the desired name for text file containing the keyword search results.
5. Save the script and you're ready to go.

## Requirements

To run scripts A and B you need to have the PyMuPDF library in your terminal, you can install it using pip: `pip install PyMuPDF`.

*Scripts written with the help of GPT-3.5.*
