# Goal

This docker container helps streamlining your Latex Document production by (1) cloning a remote git repository and (2) build a pdf from your latex file. As the latex installation is a full texlive + extras from an ubutun distribution, you should be able to build most of your latex documents.

# Manifest file

The manifest file is a simple yaml file that describes how to get your repository and which latex file to use as input. There can be more than one repository in the manifest

example:

```yaml
girafe:
  url:
    https://github.com/nherbaut/girafe_poster.git
  file:
    girafe.tex
  counter:
    true
jdev:
  url:
    https://github.com/nherbaut/containers_microservices_factory_poster.git
  file:
    microservice_containers.tex
```

the counter boolean is a little trick that, if set to true, also creates a js file that tells you how many words and pages are in the documet. Here's how to display the data:
```html
  <span id="pages_count"></span> pages (<span id="words_count"></span> words )
  <script type="text/javascript" src="thesis_counter.js"></script>

```

# How to build

I used docker to package everything. To build the project, just call this at the root of the repo

```bash
docker build . -t nherbaut/phd_count
```



# Usage

you should bind a local folder containing the manifest file to receive the result as a pdf file copied in the same folder.

example:

```bash
sudo docker run -v $PWD:/var/phd_counter/:rw  nherbaut/phd_count
```


