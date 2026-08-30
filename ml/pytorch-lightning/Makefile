PYTHON=3.8
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge pytorch defaults

env:
    conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))
