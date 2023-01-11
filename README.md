# Library:
Creating a website based on parsed books from [book scraper](https://github.com/Ash2803/book-parser).

### How to execute:

- Download or clone [repo]( https://github.com/Ash2803/online-library.git)
- You must have Python 3.9 or higher already installed;
- Create the virtual environment using command:
```
python3 -m venv venv
```
- Install the requirements using command:
```
pip install -r requirements.txt
``` 

Then you need to have data like images, books in txt format etc. To get previously mentioned data
you need to scrap it following steps in [book scraper's](https://github.com/Ash2803/book-parser) readme.
After that you need to copy `images`, `books` and `books.json` to this project.
The project already include pre-downloaded data, and you can run it in **online** mode just by script execution.

Script execution:
```
python main.py
```
[Here](https://ash2803.github.io/online-library/pages/index1.html) you can see how the already
built website looks.

### Launch library offline:
If you want to open the library in **offline** mode just open `index1.html` in `pages` folder without script execution.

### Project Goals

The code is written for educational purposes at online-course for web-developers [dvmn.org](https://dvmn.org/)
