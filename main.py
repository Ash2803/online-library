import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload(template):
    with open("books.json", "r") as my_file:
        books_json = my_file.read()
    books = json.loads(books_json)
    chunked_books = list(chunked(books, 12))

    pages = list(chunked(chunked_books, 1))
    pages_path = Path('pages')
    pages_path.mkdir(parents=True, exist_ok=True)
    for page_num, books in enumerate(pages, 1):
        rendered_page = template.render(
            chunked_books=books
        )
        with open(pages_path / f'index{page_num}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    on_reload(template)

    server = Server()
    server.watch('index.html', on_reload(template))
    server.serve(root='.')


if __name__ == '__main__':
    main()