Velero (formerly Heptio Ark) gives you tools to back up and restore your Kubernetes cluster resources and persistent volumes. You can run Velero with a cloud provider or on-premises. Velero lets you:

- Take backups of your cluster and restore in case of loss.
- Migrate cluster resources to other clusters.
- Replicate your production cluster to development and testing clusters.

Velero consists of:

- A server that runs on your cluster
- A command-line client that runs locally

## Prerequisites
- Install Minikube: `brew install minikube`
- Install velero: `brew install velero`

## Backup workflow
When you run velero backup create test-backup:

1. The Velero client makes a call to the Kubernetes API server to create a Backup object.
2. The BackupController notices the new Backup object and performs validation.
3. The BackupController begins the backup process. It collects the data to back up by querying the API server for resources.
4. The BackupController makes a call to the object storage service – for example, AWS S3 – to upload the backup file.

By default, velero backup create makes disk snapshots of any persistent volumes. You can adjust the snapshots by specifying additional flags. Run velero backup create --help to see available flags. Snapshots can be disabled with the option --snapshot-volumes=false.

![image](https://github.com/user-attachments/assets/a0cdacb6-15b0-407e-a89a-e09e23eee63c)

## Restore workflow
When you run velero restore create:

1. The Velero client makes a call to the Kubernetes API server to create a Restore object.
2. The RestoreController notices the new Restore object and performs validation.
3. The RestoreController fetches the backup information from the object storage service. It then runs some preprocessing on the backed up resources to make sure the resources will work on the new cluster. For example, using the backed-up API versions to verify that the restore resource will work on the target cluster.
4. The RestoreController starts the restore process, restoring each eligible resource one at a time.

## Set a backup to expire
When you create a backup, you can specify a TTL (time to live) by adding the flag --ttl <DURATION>. If Velero sees that an existing backup resource is expired, it removes:

1. The backup resource
2. The backup file from cloud object storage
3. All PersistentVolume snapshots
4. All associated Restores

## References
- https://github.com/vmware-tanzu/velero
- https://velero.io/docs/v1.14/
