
# Лабораторная работа №8 — Миграция на Kubernetes


### Инфраструктура Spark в Kubernetes

Установлен Spark Operator и настроена возможность запуска Spark-заданий:

```bash
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm repo update
helm install spark-operator spark-operator/spark-operator \
  --namespace spark-operator --create-namespace \
  --set sparkJobNamespace=bigdata-lab8 \
  --set serviceAccounts.spark.create=true
```



### Запуск сервиса модели (ЛР5) в Kubernetes
```
kubectl apply -f k8s/10-model-deploy.yaml -n bigdata-lab8
kubectl apply -f k8s/11-model-svc.yaml -n bigdata-lab8
kubectl apply -f k8s/12-model-ingress.yaml -n bigdata-lab8


kubectl get pods -n bigdata-lab8 -l app=lab5-model
kubectl logs deploy/lab5-model -n bigdata-lab8


INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     GET /health -> 200 OK
INFO:     POST /predict -> 200 OK
{
  "input": [1.2, 3.4, 5.6],
  "prediction": 0.87
}

```


### Запуск сервиса источника данных (ЛР6)
```
kubectl apply -f k8s/20-source-deploy.yaml -n bigdata-lab8
kubectl apply -f k8s/21-source-svc.yaml -n bigdata-lab8

kubectl get pods -n bigdata-lab8 -l app=lab6-source
kubectl logs deploy/lab6-source -n bigdata-lab8

INFO:     Uvicorn running on http://0.0.0.0:8001
INFO:     GET /health -> 200 OK
INFO:     POST /data -> 200 OK
Data received: {
  "id": 123,
  "features": [0.5, 0.6, 0.7]
}
Pushed to Kafka topic: input-events
```


### Запуск сервиса витрины данных
```
kubectl apply -f k8s/30-showcase-deploy.yaml -n bigdata-lab8
kubectl apply -f k8s/31-showcase-svc.yaml -n bigdata-lab8
kubectl apply -f k8s/32-showcase-ingress.yaml -n bigdata-lab8

kubectl get pods -n bigdata-lab8 -l app=lab7-showcase
kubectl logs deploy/lab7-showcase -n bigdata-lab8

INFO:     Uvicorn running on http://0.0.0.0:9000
INFO:     GET /health -> 200 OK
INFO:     GET /show -> 200 OK
Fetched predictions from Redis:
[
  {"id": 101, "score": 0.92},
  {"id": 102, "score": 0.84}
]
Rendered HTML with 2 records

```

### Запуск Spark-приложения через Spark Operator

```
kubectl apply -f k8s/40-spark-app.yaml -n bigdata-lab8

kubectl get sparkapplications -n bigdata-lab8
kubectl logs -n bigdata-lab8 $(kubectl get pods -n bigdata-lab8 -l spark-role=driver -o name)

```
