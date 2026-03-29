from docx import Document
import pandas as pd
import os

FOLDER_PATH = r"D:\uni - 4th sem\uni 4th\PP\Project\Resumes"

def extract_tools(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

def process_word_files(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")

            try:
                text = extract_tools(file_path)
                data.append({
                    "filename": filename,
                    "text": text
                })
            except Exception as e:
                print(f"  [ERROR] {filename}: {e}")
    return data

    # Create a DataFrame
    df = pd.DataFrame(process_word_files(FOLDER_PATH))
    print(df.head())
    print(f"Total: {len(df)} dokumen")

if __name__ == "__main__":
    process_word_files(FOLDER_PATH)
