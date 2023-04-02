FROM prefecthq/prefect:2.7.7-python3.11

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

WORKDIR  /de-zoomcap

COPY ingest_data_6.py ingest_data_6.py
COPY read_parameters.py read_parameters.py 