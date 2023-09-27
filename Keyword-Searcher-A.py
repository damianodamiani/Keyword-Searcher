import fitz  # PyMuPDF
import os
from collections import defaultdict

# Directory where the PDF files are located
pdf_directory = '/path/to/pdf/files'  # Replace with the actual directory path

# Keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']  # Replace with your keywords

# Output text file path
output_text_file = 'output_search_results.txt'  # Replace with the desired output text file path

# Output directory for search results file
output_directory = '/path/to/output/directory'  # Replace with your desired output directory path

# Ensure the output directory exists or create it
os.makedirs(output_directory, exist_ok=True)

# Full path for the output text file
output_text_file = os.path.join(output_directory, output_text_file)

# Dictionary to store keyword counts and file names
keyword_counts = defaultdict(int)
keyword_files = defaultdict(list)

# Create or open the output text file in write mode
with open(output_text_file, 'w', encoding='utf-8') as text_file:
    # Write keyword counts and file names
    text_file.write("Keyword Counts:\n")
    for keyword in keywords:
        total_count = 0
        for pdf_file_name in sorted(os.listdir(pdf_directory)):
            if pdf_file_name.endswith('.pdf'):
                pdf_file_path = os.path.join(pdf_directory, pdf_file_name)
                pdf_document = fitz.open(pdf_file_path)
                keyword_count = 0
                
                for page_num in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_num)
                    page_text = page.get_text()
                    keyword_count += page_text.lower().count(keyword.lower())
                
                if keyword_count > 0:
                    keyword_counts[keyword] += keyword_count
                    keyword_files[keyword].append(pdf_file_name)
                    total_count += keyword_count
        
        text_file.write(f"{keyword}: {total_count} times\n")
        text_file.write(f"Files: {', '.join(keyword_files[keyword])}\n")
    
    # Write search results
    text_file.write("\nSearch Results:\n")
    for keyword in keywords:
        text_file.write(f"Keyword: {keyword}\n")
        
        for pdf_file_name in keyword_files[keyword]:
            pdf_file_path = os.path.join(pdf_directory, pdf_file_name)
            pdf_document = fitz.open(pdf_file_path)
            
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                page_text = page.get_text()
                sentences = page_text.split('\n')
                
                for sentence_num, sentence in enumerate(sentences, start=1):
                    if keyword.lower() in sentence.lower():
                        start_sentence = max(0, sentence_num - 3)
                        end_sentence = min(sentence_num + 4, len(sentences))
                        context = '\n'.join(sentences[start_sentence:end_sentence])
                        page_number = page_num + 1
                        
                        text_file.write(f"File: {pdf_file_name}, Page {page_number}:\n")
                        text_file.write(f"Context:\n{context}\n")
                        text_file.write("-" * 30 + "\n")

print(f"Search results saved to {output_text_file}")
