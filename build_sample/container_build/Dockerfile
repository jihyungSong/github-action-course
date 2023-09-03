FROM python:3.8-slim

ENV PORT 8000
ENV SRC_DIR /opt/app

RUN pip install --upgrade pip && \
    pip install -r pip_requirements.txt

RUN mkdir -p ${SRC_DIR}
COPY . ./${SRC_DIR}
WORKDIR ${SRC_DIR}

EXPOSE ${PORT}

ENTRYPOINT ["uvicorn"]
CMD ["main:app"]