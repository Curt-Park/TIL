# Knative Quick Start

## Prerequisites
- Install [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- Install [Knative CLI](https://knative.dev/docs/getting-started/quickstart-install/)
- Install [Knative quickstart plugin](https://knative.dev/docs/getting-started/quickstart-install/#install-the-knative-quickstart-plugin)

With HomeBrew:
```bash
brew install \
    minikube \
    knative/client/kn \
    knative-sandbox/kn-plugins/quickstart
```

## Cluster Creation
```bash
kn quickstart minikube
minikube tunnel --profile knative  # run this command in a separate terminal window
kubectl get pods -A
#│ NAMESPACE↑              NAME                                           PF       READY              RESTARTS STATUS          IP                   NODE            AGE
#│ knative-eventing        eventing-controller-5c8967885c-6v755           ●        1/1                       0 Running         172.17.0.12          knative         79s
#│ knative-eventing        eventing-webhook-7f9b5f7d9-5cqq6               ●        1/1                       0 Running         172.17.0.13          knative         79s
#│ knative-eventing        imc-controller-7d9b5756cb-wrhqq                ●        1/1                       0 Running         172.17.0.14          knative         65s
#│ knative-eventing        imc-dispatcher-76665c67df-qgghs                ●        1/1                       0 Running         172.17.0.15          knative         65s
#│ knative-eventing        mt-broker-controller-b74d7487c-csb6x           ●        1/1                       0 Running         172.17.0.18          knative         52s
#│ knative-eventing        mt-broker-filter-545d9f864f-ggk4p              ●        1/1                       0 Running         172.17.0.16          knative         52s
#│ knative-eventing        mt-broker-ingress-7655d545f5-j4jrj             ●        1/1                       0 Running         172.17.0.17          knative         52s
#│ knative-serving         activator-c7d578d94-m2rxl                      ●        1/1                       0 Running         172.17.0.3           knative         2m34s
#│ knative-serving         autoscaler-6488988457-7lk5v                    ●        1/1                       0 Running         172.17.0.4           knative         2m34s
#│ knative-serving         controller-6cff4c9d57-dvjh9                    ●        1/1                       0 Running         172.17.0.5           knative         2m34s
#│ knative-serving         default-domain-nq7bj                           ●        1/1                       0 Running         172.17.0.11          knative         85s
#│ knative-serving         domain-mapping-7598c5f659-qx5cs                ●        1/1                       0 Running         172.17.0.6           knative         2m34s
#│ knative-serving         domainmapping-webhook-8c4c9fdc4-8l7rl          ●        1/1                       0 Running         172.17.0.7           knative         2m34s
#│ knative-serving         net-kourier-controller-7997b54d46-lzq6g        ●        1/1                       0 Running         172.17.0.9           knative         118s
#│ knative-serving         webhook-df8844f6-44wgs                         ●        1/1                       0 Running         172.17.0.8           knative         2m34s
#│ kourier-system          3scale-kourier-gateway-54f8c78c75-tdrhx        ●        1/1                       0 Running         172.17.0.10          knative         118s
#│ kube-system             coredns-6d4b75cb6d-dd8hd                       ●        1/1                       0 Running         172.17.0.2           knative         3m50s
#│ kube-system             etcd-knative                                   ●        1/1                       0 Running         192.168.58.2         knative         4m2s
#│ kube-system             kube-apiserver-knative                         ●        1/1                       0 Running         192.168.58.2         knative         4m5s
#│ kube-system             kube-controller-manager-knative                ●        1/1                       0 Running         192.168.58.2         knative         4m2s
#│ kube-system             kube-proxy-s7t64                               ●        1/1                       0 Running         192.168.58.2         knative         3m50s
#│ kube-system             kube-scheduler-knative                         ●        1/1                       0 Running         192.168.58.2         knative         4m4s
#│ kube-system             storage-provisioner                            ●        1/1                       0 Running         192.168.58.2         knative         3m49s
```

## Deploying a Knative Service
```bash
kn service create hello --image gcr.io/knative-samples/helloworld-go --port 8080 --env TARGET=World
# Creating service 'hello' in namespace 'default':
#
#   0.023s The Route is still working to reflect the latest desired specification.
#   0.040s Configuration "hello" is waiting for a Revision to become ready.
#   0.073s ...
#  33.351s ...
#  33.442s Ingress has not yet been reconciled.
#  33.484s Waiting for load balancer to be ready
#  33.668s Ready to serve.
#
# Service 'hello' created to latest revision 'hello-00001' is available at URL:
# http://hello.default.example.com
```

or

```bash
kubectl apply -f hello.yaml
# service.serving.knative.dev/hello created
```

Access the service.
```bash
kn service list
# NAME    URL                                       LATEST        AGE   CONDITIONS   READY   REASON
# hello   http://hello.default.127.0.0.1.sslip.io   hello-00001   10m   3 OK / 3     True

curl "$(kn service describe hello -o url)"
# Hello World!
```

## Autoscaling
Wait for all pod terminated. It may take up to 2 minutes.
```bash
kubectl get pod -l serving.knative.dev/service=hello -w
# NAME                                      READY   STATUS        RESTARTS   AGE
# hello-00001-deployment-85b6c8d697-hjgsq   2/2     Terminating   0          66s
# hello-00001-deployment-85b6c8d697-hjgsq   1/2     Terminating   0          90s
# hello-00001-deployment-85b6c8d697-hjgsq   0/2     Terminating   0          93s
# hello-00001-deployment-85b6c8d697-hjgsq   0/2     Terminating   0          93s
# hello-00001-deployment-85b6c8d697-hjgsq   0/2     Terminating   0          93s
```

Rerun `curl "$(kn service describe hello -o url)"`.
```bash
hello-00001-deployment-85b6c8d697-zrjpn   0/2     ContainerCreating   0          0s
hello-00001-deployment-85b6c8d697-zrjpn   1/2     Running             0          2s
hello-00001-deployment-85b6c8d697-zrjpn   2/2     Running             0          2s
```

## Traffic Splitting
Traffic splitting is useful for blue/green deployments and canary deployments.

A Revision is a snapshot-in-time of application code and configuration.
A new Revision is created every time you make changes to the configuration of a Knative Service.
When splitting traffic, Knative splits traffic between different Revisions of your Knative Service.

Instead of TARGET=World, update the environment variable TARGET on your Knative Service to greet "Knative" instead.

```bash
kn service update hello --env TARGET=Knative
# Updating Service 'hello' in namespace 'default':
#
#   0.021s The Configuration is still working to reflect the latest desired specification.
#   1.185s Traffic is not yet migrated to the latest revision.
#   1.254s Ingress has not yet been reconciled.
#   1.267s Waiting for load balancer to be ready
#   1.433s Ready to serve.
#
# Service 'hello' updated to latest revision 'hello-00002' is available at URL:
# http://hello.default.127.0.0.1.sslip.io
```

or

Edit your existing hello.yaml file to contain the following:
```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    spec:
      containers:
        - image: gcr.io/knative-samples/helloworld-go
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "Knative"
```

Deploy.
```bash
kubectl apply -f hello.yaml
# service.serving.knative.dev/hello configured
```

Access the new revision.
```bash
curl $(kn service describe hello -o url)
# Hello Knative!
```

Split traffic between revisions.
```bash
kn service update hello \
    --traffic hello-00001=50 \
    --traffic @latest=50
```

or

Add the `traffic` section to the bottom of your existing `hello.yaml` file:
```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello
spec:
  template:
    spec:
      containers:
        - image: gcr.io/knative-samples/helloworld-go
          ports:
            - containerPort: 8080
          env:
            - name: TARGET
              value: "Knative"
  traffic:
  - latestRevision: true
    percent: 50
  - latestRevision: false
    percent: 50
    revisionName: hello-00001
```

Run:
```bash
kubectl apply -f hello.yaml
```

Check the traffic split:
```bash
kn revisions list
# NAME          SERVICE   TRAFFIC   TAGS   GENERATION   AGE     CONDITIONS   READY   REASON
# hello-00002   hello     50%              2            7m12s   3 OK / 4     True
# hello-00001   hello     50%              1            92m     3 OK / 4     True

curl "$(kn service describe hello -o url)"
# Hello World!
 204 curl "$(kn service describ)"
curl "$(kn service describe hello -o url)"
# Hello World!
curl "$(kn service describe hello -o url)"
# Hello World!
curl "$(kn service describe hello -o url)"
# Hello Knative!
curl "$(kn service describe hello -o url)"
# Hello Knative!
curl "$(kn service describe hello -o url)"
# Hello Knative!
```

## Shutdown the service
```bash
kn service delete hello
# Service 'hello' successfully deleted in namespace 'default'.

kn service list
# No services found.
```

## Shutdown the cluster
```bash
minikube delete --profile knative
```

## References
- https://knative.dev/docs/getting-started
- https://github.com/knative/docs/blob/main/docs/client/kn-plugins.md
