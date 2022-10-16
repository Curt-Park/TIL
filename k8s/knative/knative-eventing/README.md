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

### Creating your first source
Run the command:
```bash
kn service create cloudevents-player \
    --image ruromero/cloudevents-player:latest \
    --env BROKER_URL=http://broker-ingress.knative-eventing.svc.cluster.local/default/example-broker

# Creating service 'cloudevents-player' in namespace 'default':
#
#   0.025s The Route is still working to reflect the latest desired specification.
#   0.039s Configuration "cloudevents-player" is waiting for a Revision to become ready.
#   0.047s ...
#  18.186s ...
#  18.275s Ingress has not yet been reconciled.
#  18.365s Waiting for load balancer to be ready
#  18.487s Ready to serve.
#
# Service 'cloudevents-player' created to latest revision 'cloudevents-player-00001' is available at URL:
# http://cloudevents-player.default.127.0.0.1.sslip.io
```

or

```bash
kubectl apply -f cloudevents-player.yaml
# service.serving.knative.dev/cloudevents-player created
```

### Examining the CloudEvents Player

Open `http://cloudevents-player.default.127.0.0.1.sslip.io` in your web-browser.

Post an event.
```bash
curl -i http://cloudevents-player.default.127.0.0.1.sslip.io \
    -H "Content-Type: application/json" \
    -H "Ce-Id: 123456789" \
    -H "Ce-Specversion: 1.0" \
    -H "Ce-Type: some-type" \
    -H "Ce-Source: command-line" \
    -d '{"msg":"Hello CloudEvents!"}'
```

See the posted event:
<img width="1278" src="https://user-images.githubusercontent.com/14961526/196024155-fccebc93-0c5c-43b7-b7e8-a04b58006f3b.png">

or

```bash
curl http://cloudevents-player.default.127.0.0.1.sslip.io/messages
# [{"event":{"attributes":{"datacontenttype":"application/json","id":"123456789","mediaType":"application/json","source":"command-line","specversion":"1.0","type":"some-type"},"data":{"msg":"Hello CloudEvents!"},"extensions":{}},"id":"123456789","receivedAt":"2022-10-16T09:40:43.243206+02:00[Europe/Madrid]","type":"RECEIVED"}]%
```

## Using Triggers and Sinks
In the last topic we used the CloudEvents Player as an event source to send events to the Broker.
We now want the event to go from the Broker to an event sink.

In this topic, we will use the CloudEvents Player as the sink as well as a source.
This means we will be using the CloudEvents Player to both send and receive events.
We will use a Trigger to listen for events in the Broker to send to the sink.

### Creating you first Trigger
Create a Trigger that listens for CloudEvents from the event source and places them into the sink, which is also the CloudEvents Player app.

```bash
kn trigger create cloudevents-trigger --sink cloudevents-player  --broker example-broker
# Trigger 'cloudevents-trigger' successfully created in namespace 'default'.
```

or

```bash
kubectl apply -f ce-trigger.yaml
# trigger.eventing.knative.dev/cloudevents-trigger created
```

> Because we didn't specify a --filter in our kn command, the Trigger is listening for any CloudEvents coming into the Broker.
> You can specify a filter with --filter option:
>
> `kn trigger create cloudevents-player-filter --sink cloudevents-player  --broker example-broker --filter type=some-type`

Now, when we go back to the CloudEvents Player and send an event, we see that CloudEvents are both sent and received by the CloudEvents Player:
<img width="1270" src="https://user-images.githubusercontent.com/14961526/196024630-c230a38a-d217-492b-b34e-97689f8a1ee0.png">

## References
- https://knative.dev/docs/getting-started/getting-started-eventing/
