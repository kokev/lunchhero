ARG RASA_SDK_VERSION
FROM rasa/rasa-sdk:$RASA_SDK_VERSION

USER root

COPY requirements.txt

COPY actions.py /actions

COPY main.py .

RUN pip install -r requriements.txt

CMD ["start", "--actions", "actions"]

CMD ["run", "python", "/app/main.py"]
