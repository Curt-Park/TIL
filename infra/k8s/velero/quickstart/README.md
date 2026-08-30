## Files
This directory contains manifests for two versions of a sample Nginx app under the nginx-example namespace.

- minio.yaml: Object storage for backups.
- nbinx.yaml: This is the most basic version of the Nginx app, which can be used to test Velero's backup and restore functionality.

```bash
# cluster setup
minikube start
# velero installation
kubectl apply -f minio.yaml
velero install \
    --provider aws \
    --plugins velero/velero-plugin-for-aws:v1.2.1 \
    --bucket velero \
    --secret-file ./credentials-velero \
    --use-volume-snapshots=false \
    --backup-location-config region=minio,s3ForcePathStyle="true",s3Url=http://minio.velero.svc:9000

# create namesapce, pvc, deployment, service
kubectl apply -f nginx.yaml

# create a backup
velero backup create nginx-backup --include-namespaces nginx-example

# simulate a disaster. all created things are gone.
kubectl delete namespaces nginx-example

# restore your lost resources
velero restore create --from-backup nginx-backup
```
