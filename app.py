# app.py
from flask import Flask, render_template, request, redirect, send_file
from functions import merge, create

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/merge_pdf')
def merge_page():
    return render_template('merge_pdf.html')


@app.route('/merge', methods=['POST'])
def merge_pdf():
    if request.method == 'POST':
        pdf_files = request.files.getlist('files')
        output = request.form['output']
        if not output.lower().endswith('.pdf'):
            output += '.pdf'
        merged_pdf = merge(pdfs=pdf_files) 
        return send_file(
            merged_pdf, 
            download_name=output,
            mimetype='application/pdf',
            as_attachment=True,
        )


@app.route('/create_pdf')
def create_page():
    return render_template('create_pdf.html')

@app.route('/create', methods=["POST"])
def create_pdf():
    if request.method == 'POST':
        pdf_files = request.files.getlist('files')
        output = request.form['output']
        if not output.lower().endswith('.pdf'):
            output += '.pdf'
        created_pdf =  create(pdf_files)
        return send_file(
            created_pdf, 
            download_name=output,
            mimetype='application/pdf',
            as_attachment=True,
        )



if __name__ == '__main__':
    app.run(debug=True)