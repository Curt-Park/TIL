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

Open http://localhost:12345/dolphinscheduler/ui
![image](https://user-images.githubusercontent.com/14961526/214229341-cf3d2b5f-19fa-4f04-8adb-81380adccb8a.png)

- ID: admin
- PW: dolphinscheduler123

## Create a project
<img width="1345" src="https://user-images.githubusercontent.com/14961526/214239800-2bfae09c-11bd-406a-aee6-830b631c921a.png">

Click `Project` -> `Create Project`.

<img width="1352" src="https://user-images.githubusercontent.com/14961526/214240310-28866a08-5d35-4ec6-912b-4b0c9744906b.png">

## Workflow Definition

<img width="1348" src="https://user-images.githubusercontent.com/14961526/214240526-bc7733a7-7a37-4daf-ba7b-4c13217daa28.png">

- Click `Workflow Definition` -> `Create Workflow`.
- Drag `SHELL` from the left.
- Configure the node and click `Confirm`.
- Click `Save`

<img width="1352" src="https://user-images.githubusercontent.com/14961526/214241047-7dad709d-27ea-4590-bdea-f678a8a86b82.png">
<img width="1121" src="https://user-images.githubusercontent.com/14961526/214241096-92c1d3c6-7320-4dc8-bc11-6cc1c2802d53.png">
<img width="1350" src="https://user-images.githubusercontent.com/14961526/214241294-e6f8cc34-8975-434b-acc0-bfb68ec75179.png">

## Run the workflow

- Click `Online`
- Click `Start`

<img width="1117" src="https://user-images.githubusercontent.com/14961526/214241645-4cce65a8-d636-4df4-88e6-ac9de7188d10.png">
<img width="1120" src="https://user-images.githubusercontent.com/14961526/214241701-88b5cf38-e61c-4121-9f56-b871e8043a39.png">
