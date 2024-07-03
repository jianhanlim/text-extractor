from flask import Flask, request, jsonify
import fitz  # PyMuPDF
import docx
import os
import tempfile

app = Flask(__name__)

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def chunk_text(text, chunk_size):
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

@app.route('/extract', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    chunk_size = int(request.form.get('chunk_size', 100))
    file_extension = os.path.splitext(file.filename)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file.save(temp_file.name)
        temp_file_path = temp_file.name

    try:
        if file_extension == '.pdf':
            text = extract_text_from_pdf(temp_file_path)
        elif file_extension == '.docx':
            text = extract_text_from_docx(temp_file_path)
        elif file_extension == '.txt':
            text = extract_text_from_txt(temp_file_path)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        chunks = chunk_text(text, chunk_size)
        return jsonify({"chunks": chunks})
    finally:
        os.remove(temp_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
