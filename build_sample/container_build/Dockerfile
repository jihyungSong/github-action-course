FROM python:3.8-slim

ENV PORT 8000
ENV SRC_DIR /opt/app
ENV PKG_TMP_DIR /tmp
COPY pip_requirements.txt ${PKG_TMP_DIR}/

RUN pip install --upgrade pip && \
    pip install -r ${PKG_TMP_DIR}/pip_requirements.txt

RUN mkdir -p ${SRC_DIR}
COPY . ./${SRC_DIR}
WORKDIR ${SRC_DIR}

EXPOSE ${PORT}

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]