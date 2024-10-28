Longhorn is a lightweight, reliable and easy-to-use distributed block storage system for Kubernetes.

## Prerequisites
- Install Minikube: `brew install minikube`
- Install Helm: `brew install helm`

## Setup
```bash
# Create a cluster
minikube start --nodes 3
# https://github.com/kubernetes/minikube/issues/2846
minikube ssh -n minikube "sudo apt-get update;sudo apt-get install -y open-iscsi"
minikube ssh -n minikube-m02 "sudo apt-get update;sudo apt-get install -y open-iscsi"
minikube ssh -n minikube-m03 "sudo apt-get update;sudo apt-get install -y open-iscsi"

# Install Longhorn
helm repo add longhorn https://charts.longhorn.io
helm repo update
helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace --version 1.7.2
```

You will see:
```bash
$ kubectl get pods -n longhorn-system

NAME                                                READY   STATUS    RESTARTS        AGE
csi-attacher-86dc84c794-5s9c2                       1/1     Running   0               2m58s
csi-attacher-86dc84c794-7c6hb                       1/1     Running   0               2m58s
csi-attacher-86dc84c794-tscrb                       1/1     Running   0               2m58s
csi-provisioner-5f5459959d-bpz4v                    1/1     Running   0               2m58s
csi-provisioner-5f5459959d-dr4n6                    1/1     Running   1 (2m12s ago)   2m58s
csi-provisioner-5f5459959d-qszqg                    1/1     Running   1 (101s ago)    2m58s
csi-resizer-6c57584d66-8fgpn                        1/1     Running   1 (2m5s ago)    2m58s
csi-resizer-6c57584d66-lpfss                        1/1     Running   0               2m58s
csi-resizer-6c57584d66-r8vfj                        1/1     Running   0               2m58s
csi-snapshotter-656cf9b8f5-9r568                    1/1     Running   1 (119s ago)    2m58s
csi-snapshotter-656cf9b8f5-pzqqm                    1/1     Running   0               2m58s
csi-snapshotter-656cf9b8f5-sqj9l                    1/1     Running   0               2m58s
engine-image-ei-51cc7b9c-cfqbj                      1/1     Running   0               3m32s
engine-image-ei-51cc7b9c-knl9z                      1/1     Running   0               3m32s
engine-image-ei-51cc7b9c-lx5rg                      1/1     Running   0               3m32s
instance-manager-08542bc6ea9938cf7be3e7085325038b   1/1     Running   0               3m2s
instance-manager-7c202bd4688f90952f315d9d81d7df9a   1/1     Running   0               97s
instance-manager-9c6692f057f958092a36809d8ebd3421   1/1     Running   0               70s
longhorn-csi-plugin-4bhzh                           3/3     Running   1 (116s ago)    2m58s
longhorn-csi-plugin-8c9b4                           3/3     Running   0               2m58s
longhorn-csi-plugin-qw8bc                           3/3     Running   1 (90s ago)     2m58s
longhorn-driver-deployer-6f6fdf4f75-x95lx           1/1     Running   0               7m31s
longhorn-manager-9f26q                              2/2     Running   0               3m42s
longhorn-manager-9qfrl                              2/2     Running   0               2m12s
longhorn-manager-s8t8x                              2/2     Running   0               104s
longhorn-ui-b97bd599c-sm2jz                         1/1     Running   0               7m31s
longhorn-ui-b97bd599c-xn2s9                         1/1     Running   0               7m31s
```

## Access
- Change `svc/longhorn-frontend` ClusterIP into LoadBalancer
- `minikube tunnel`
- Open http://localhost/

You will see:
<img width="1456" src="https://github.com/user-attachments/assets/8d1b231f-d9b1-47a8-ad33-2f177b5e76c9">
