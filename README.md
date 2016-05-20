Tensorflow via Docker
=====================

> https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/udacity

```shell
# build image
cd tensorflow-udacity
docker build --pull -t $USER/assignments .

# run jupyter notebooks
docker run -p 8888:8888 -v $(pwd):/udacity -v $(pwd)/notebooks:/notebooks -it --rm $USER/assignments /run_jupyter.sh

# start a console
docker run -v $(pwd):/udacity -v $(pwd)/notebooks:/notebooks -it --rm $USER/assignments /bin/bash
```


[DEPRECATED] Docker (my custom docker image)
============================================

```shell
# build image
docker build -t deeplearning .

# start a console
docker run -v $(pwd):/udacity -i -t deeplearning /bin/bash
```
