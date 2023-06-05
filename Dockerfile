FROM python:3.10

LABEL authors="francesco"

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --upgrade pip

WORKDIR app

COPY requirements.txt /app
COPY resources  /app/resources
COPY source  /app/source
COPY tests  /app/tests

RUN pip install -r requirements.txt

ENTRYPOINT ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "results", "tests/features/"]