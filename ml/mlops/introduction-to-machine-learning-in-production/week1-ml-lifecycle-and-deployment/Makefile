env:
	conda create -n mlops-week1 python=3.8

setup:
	pip install -r requirements.txt
	pip install tensorflow-macos tensorflow-metal
	conda install -y -c apple tensorflow-deps
	conda install -y -c conda-forge opencv===4.5.3
	python -m ipykernel install --user --name mlops-week1 --display-name "mlops-week1"
