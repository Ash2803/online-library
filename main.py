import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    with open("books.json", "r") as my_file:
        books_json = my_file.read()

    books = json.loads(books_json)
    print(type(books))

    rendered_page = template.render(
        books=books
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
