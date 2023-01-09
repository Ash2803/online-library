import json
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload(template):
    with open("books.json", "r") as my_file:
        books_json = my_file.read()
    books = json.loads(books_json)
    rendered_page = template.render(
        books=books
    )
    with open('index.html', 'w', encoding="utf8") as file:
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
