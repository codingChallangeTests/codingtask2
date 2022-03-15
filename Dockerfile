FROM python:3.10 AS builder
WORKDIR /app/

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt \
    pip install --no-cache-dir -r test-requirements.txt

RUN tox

RUN python3 setup.py sdist

FROM python:3.10-slim
WORKDIR /app/
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash app

COPY --from=builder /app/dist/*.tar.gz /app/codingtask2.tar.gz
COPY example_merge.py /app/

RUN pip install --no-cache-dir /app/codingtask2.tar.gz && \
    rm /app/codingtask2.tar.gz

USER app

ENTRYPOINT ["python", "example_merge.py"]
CMD ["-h"]
