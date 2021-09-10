FROM python:3.8.6
COPY . /myproject
WORKDIR /myproject
RUN pip install python-dotenv
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD  ["app.py"]