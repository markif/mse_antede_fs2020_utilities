This library provides some basic utilities for the AnTeDe class of the MSE.

# Install 

This package builds on Python 3.

```bash
sudo pip3 install mse_antede_fs2020_utilities
```

# Build

Increase the version number in [setup.py](setup.py).


In order to extract the python script and upload it to pypi run

```bash
docker run -e TZ=Europe/Zurich --name datascience-notebook --net=host -p 8888:8888 -v "$(pwd)":/home/jovyan/work -it --rm i4ds/datascience-notebook start-notebook.sh --NotebookApp.token=''
docker exec -it datascience-notebook /bin/bash
cd work
rm -rf dist/*
python3 setup.py bdist_wheel
python3 -m twine upload dist/*
```

Upload everything to the git repository.
