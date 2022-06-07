FROM logiqx/python-bs4:latest

ADD scrape_style.py .

CMD [ "python3", "./scrape_style.py" ]