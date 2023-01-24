# ETCD
etcd is a strongly consistent, distributed key-value store that provides a reliable way to store data that needs to be accessed by a distributed system or cluster of machines.
It gracefully handles leader elections during network partitions and can tolerate machine failure, even in the leader node.

## Features
- Simple Interface based on json
- Key-value storage
- Watch for changes

## How to Install
```bash
brew install etcd
```

## Quick Start
Let's see how to run and test a single-member cluster of etcd.

1. Launch `etcd`:
```bash
$ etcd
```

2. From another terminal, use `etcdctl` to set a key:
```bash
$ etcdctl put greeting "Hello, etcd"
ok
```

3. From any terminal, retrieve the key:
```bash
$ etcdctl get greeting
greeting
Hello, etcd
```

4. Delete the key:
```bash
$ etcdctl del greeting
1
```

5. Check the key deleted:
```bash
$ etcdctl get greeting
# shows nothing
```

6. Watch keys:
```bash
$ etcdctl watch stock1  # terminal1
$ etcdctl put stock1 1000  # terminal1
OK

# terminal1 shows:
## PUT
## stock1
## 1000

$ etcdctl put stock2 10
OK

# terminal1 shows nothing
```

7. How to create lease:

etcd uses leases to manage temporary keys.
A lease is created with a time-to-live (TTL) and then attached to a key at creation.
One lease can be used for multiple keys.
When the TTL on the lease expires, it deletes all associated keys.
To create a lease, use grant with a number of seconds for TTL.

```bash
$ etcdctl lease grant 300
lease 694d85e25c31920e granted with TTL(300s)

$ etcdctl put sample value --lease=694d85e25c31920e
OK
$ etcdctl get sample
sample
value

$ etcdctl lease keep-alive 694d85e25c31920e
lease 694d85e25c31920e keepalived with TTL(300)

$ etcdctl revoke 694d85e25c31920e
$ etcdctl get sample
# shows nothing
```

8. How to create locks:
```bash
$ etcdctl lock mutex1  # terminal1
mutex1/694d85e25c319214

$ etcdctl lock mutex1  # terminal2
# waiting... shows nothing

# terminate the lock in terminal1
# terminal2 will show: mutex1/694d85e25c319218
```
