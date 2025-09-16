FROM python:3.12-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    SPARK_VERSION=3.5.1 \
    HADOOP_VERSION=3 \
    SPARK_HOME=/opt/spark

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless curl ca-certificates procps bash tini && \
    rm -rf /var/lib/apt/lists/*

COPY images/spark-job/requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

RUN curl -fsSL https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    -o /tmp/spark.tgz && \
    mkdir -p ${SPARK_HOME} && \
    tar -xzf /tmp/spark.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} && \
    rm -f /tmp/spark.tgz
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

WORKDIR /app
COPY jobs /app/jobs
ENTRYPOINT ["/opt/spark/bin/spark-class"]
