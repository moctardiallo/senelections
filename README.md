**Pre-installation**

```
python3.6
```

```
spark2.3 and pyspark
```

A useful guide to install spark and pyspark can be found
[here](https://medium.com/@GalarnykMichael/install-spark-on-ubuntu-pyspark-231c45677de0)

**Installation**

```
git clone https://github.com/moctardiallo/senelections

cd senelections

pipenv install

```

**Configuration**

Open `~/.bashrc` in an editor. Add the following lines and replace `path/to/your/cloned/repo`

```
export SENELECTIONS_PATH=path/to/your/downloaded/repo
export PYTHONPATH=$PYTHONPATH:SENELECTIONS_PATH;
```

**Run**

Assuming your current directory is the cloned repo run:

```
spark-submit senelections/senelections.py
```
