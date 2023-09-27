import os
from collections import defaultdict

# Directory where the text files are located
text_directory = '/path/to/text/files'  # Replace with the actual directory path

# Keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']  # Replace with your keywords

# Output text file path
output_text_file = '/path/to/output/directory/output_search_results.txt'  # Replace with the desired output text file path

# Dictionary to store keyword counts and file names
keyword_counts = defaultdict(int)
keyword_files = defaultdict(list)

try:
    # Create or open the output text file in write mode
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        # Write keyword counts and file names
        text_file.write("Keyword Counts:\n")
        for keyword in keywords:
            total_count = 0
            for root, _, files in os.walk(text_directory):
                for txt_file_name in files:
                    if txt_file_name.endswith('.txt'):
                        txt_file_path = os.path.join(root, txt_file_name)
                        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                            txt_content = txt_file.read()
                            keyword_count = txt_content.lower().count(keyword.lower())
                            if keyword_count > 0:
                                keyword_counts[keyword] += keyword_count
                                keyword_files[keyword].append(txt_file_name)
                                total_count += keyword_count
            
            text_file.write(f"{keyword}: {total_count} times\n")
            text_file.write(f"Files: {', '.join(keyword_files[keyword])}\n")
        
        # Write search results
        text_file.write("\nSearch Results:\n")
        for keyword in keywords:
            text_file.write(f"Keyword: {keyword}\n")
            
            for txt_file_name in keyword_files[keyword]:
                txt_file_path = os.path.join(text_directory, txt_file_name)
                with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                    txt_content = txt_file.read()
                    sentences = txt_content.split('\n')
                    
                    for sentence_num, sentence in enumerate(sentences, start=1):
                        if keyword.lower() in sentence.lower():
                            start_sentence = max(0, sentence_num - 3)
                            end_sentence = min(sentence_num + 4, len(sentences))
                            context = '\n'.join(sentences[start_sentence:end_sentence])
                            
                            text_file.write(f"File: {txt_file_name}\n")
                            text_file.write(f"Context:\n{context}\n")
                            text_file.write("-" * 30 + "\n")

    print(f"Search results saved to {output_text_file}")

except Exception as e:
    print(f"An error occurred: {e}")
