FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 requests beautifulsoup4 openpyxl lxml
WORKDIR /app

COPY ingest_data.py ingest_data.py
COPY read_parameters_2.py read_parameters_2.py

ENTRYPOINT [ "python","ingest_data.py" ]

