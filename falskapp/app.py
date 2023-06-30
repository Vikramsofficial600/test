from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('E:/Library/books_data/books.csv', encoding='latin-1',delimiter=';',error_bad_lines=False, dtype={'Year-Of-Publication': str})
df.head()
@app.route('/api/books/<year>')
def get_books_by_year(year):
    # Filter books based on the year of publication
    df.head()
    filtered_books = df[df['Year-Of-Publication'] == int(year)]
    filtered_books_subset = filtered_books[['Book-Title', 'Book-Author', 'Image-URL-L']]
    print(filtered_books_subset)
    books_json = filtered_books_subset.to_json(orient='records')

    return jsonify(books_json)

if __name__ == '__main__':
    app.run()
