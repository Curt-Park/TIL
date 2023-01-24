# Dolphinscheduler
https://dolphinscheduler.apache.org/

Apache DolphinScheduler provides a distributed and easy to expand visual workflow task scheduling open-source platform. It is suitable for enterprise-level scenarios. It provides a solution to visualize operation tasks, workflows, and the entire data processing procedures.

Apache DolphinScheduler aims to solve complex big data task dependencies and to trigger relationships in data OPS orchestration for various big data applications. Solves the intricate dependencies of data R&D ETL and the inability to monitor the health status of tasks. DolphinScheduler assembles tasks in the Directed Acyclic Graph (DAG) streaming mode, which can monitor the execution status of tasks in time, and supports operations like retry, recovery failure from specified nodes, pause,
resume, and kill tasks, etc.

## Start-up
```bash
# Initialize the database, use profile schema
$ docker-compose --profile schema up -d

# start all dolphinscheduler server, use profile all
$ docker-compose --profile all up -d

$ docker ps
CONTAINER ID   IMAGE                                                                  COMMAND                  CREATED          STATUS                             PORTS                                                NAMES
0913011cd466   ghcr.io/apache/dolphinscheduler/dolphinscheduler-worker:latest         "/bin/bash ./bin/sta…"   29 seconds ago   Up 29 seconds (health: starting)   1235/tcp                                             dolphinscheduler_dolphinscheduler-worker_1
561b9073628d   ghcr.io/apache/dolphinscheduler/dolphinscheduler-api:latest            "/bin/bash ./bin/sta…"   29 seconds ago   Up 29 seconds (health: starting)   0.0.0.0:12345->12345/tcp, 0.0.0.0:25333->25333/tcp   dolphinscheduler_dolphinscheduler-api_1
c849fe43915a   ghcr.io/apache/dolphinscheduler/dolphinscheduler-master:latest         "/bin/bash ./bin/sta…"   29 seconds ago   Up 29 seconds (health: starting)   12345/tcp                                            dolphinscheduler_dolphinscheduler-master_1
9dda05e7a7df   bitnami/zookeeper:3.6.2                                                "/opt/bitnami/script…"   40 seconds ago   Up 39 seconds (healthy)            2181/tcp, 2888/tcp, 3888/tcp, 8080/tcp               dolphinscheduler_dolphinscheduler-zookeeper_1
413cd8a75792   ghcr.io/apache/dolphinscheduler/dolphinscheduler-alert-server:latest   "/bin/bash ./bin/sta…"   40 seconds ago   Up 39 seconds (healthy)            50052-50053/tcp                                      dolphinscheduler_dolphinscheduler-alert_1
e3dbffbf42e4   bitnami/postgresql:11.11.0                                             "/opt/bitnami/script…"   2 minutes ago    Up 2 minutes (healthy)             0.0.0.0:5432->5432/tcp                               dolphinscheduler_dolphinscheduler-postgresql_1

```

## Login
