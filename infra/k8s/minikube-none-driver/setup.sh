# Requirements: https://minikube.sigs.k8s.io/docs/drivers/none/
sudo apt-get update && apt-get install iptables conntrack

# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube

# install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# install cri-tools
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.31.0/crictl-v1.31.0-linux-amd64.tar.gz
sudo tar zxvf crictl-v1.31.0-linux-amd64.tar.gz -C /usr/local/bin

# install cri-dockerd
wget https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.15/cri-dockerd_0.3.15.3-0.ubuntu-focal_amd64.deb
sudo dpkg -i cri-dockerd_0.3.15.3-0.ubuntu-focal_amd64.deb
sudo systemctl enable --now cri-docker.service
systemctl status cri-docker.service
