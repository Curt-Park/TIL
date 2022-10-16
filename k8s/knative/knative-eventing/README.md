# Knative Eventing
Knative Eventing provides you with helpful tools that can be used to create event-driven applications,
by easily attaching event sources, triggers, and other options to your Knative Services.

Event-driven applications are designed to detect events as they occur,
and process these events by using user-defined, event-handling procedures.

This tutorial shows how you can use a basic workflow for managing events that uses Event Sources, Brokers, Triggers, and Sinks.

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

## Sources, Brokers, and Triggers
As part of the kn quickstart install, an `InMemoryChannel-backed Broker` is installed on your kind cluster.

```bash
kn broker list
# NAME             URL                                                                               AGE   CONDITIONS   READY   REASON
# example-broker   http://broker-ingress.knative-eventing.svc.cluster.local/default/example-broker   26s   6 OK / 6     True
```

## Using a Knative Service as a source
In this tutorial, you will use the [CloudEvents Player app](https://github.com/ruromero/cloudevents-player) to showcase the core concepts of Knative Eventing.
By the end of this tutorial, you should have an architecture that looks like this:
![image](https://user-images.githubusercontent.com/14961526/196023858-8dcd999f-7abe-4c9b-9872-02e14196fb9b.png)
