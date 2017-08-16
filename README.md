# Goal

This docker container helps streamlining your Latex Document production by (1) cloning a remote git repository and (2) build a pdf from your latex file. As the latex installation is a full texlive + extras from an ubutun distribution, you should be able to build most of your latex documents.

# Manifest file

The manifest file is a simple yaml file that describe how to get your repository, which latex file to use as input.

example:

```
girafe:
  url:
    git@github.com:nherbaut/girafe_poster.git
  file:
    girafe.tex
  counter: 
    true
```

the counter boolean is a little trick that, if set to true, also creates a js file that tells you how many words and pages are in the documets. Here's how to display the data:
```
  <span id="pages_count"></span> pages (<span id="words_count"></span> words )
  <script type="text/javascript" src="thesis_counter.js"></script>

```

# Usage

you should bind a local folder containing the manifest file to receive the result as a pdf file copied in the same folder.

example:

```
sudo docker run -v $PWD:/var/phd_counter/:rw  nherbaut/phd_count
```


