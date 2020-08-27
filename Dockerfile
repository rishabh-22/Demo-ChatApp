FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader punkt averaged_perceptron_tagger
EXPOSE 5000
CMD python3 app.py