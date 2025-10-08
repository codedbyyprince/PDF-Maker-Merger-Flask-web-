# app.py
from flask import Flask, render_template, request, redirect, send_file
from functions import merge

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/merge', methods=['POST'])
def merge_pdf():
    if request.method == 'POST':
        pdf_files = request.files.getlist('pdf')
        output = request.form['output']
        
        # 1. This variable holds the BytesIO object (the merged PDF)
        merged_pdf = merge(pdfs=pdf_files) 
        
        return send_file(
            # 2. FIX: Use the variable that holds the merged data (meged_pdf)
            merged_pdf, 
            download_name=output,
            mimetype='application/pdf',
            as_attachment=True,
        )

if __name__ == '__main__':
    app.run(debug=True)