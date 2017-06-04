#!/usr/bin/env python3
import argparse
import subprocess

import os
import yaml
import tempfile
from git import Repo
from jsmin import jsmin
from jinja2 import Environment, PackageLoader, select_autoescape
from PyPDF2 import PdfFileReader


parser = argparse.ArgumentParser(description='Generate js counter of a pdf document')

parser.add_argument('--config', default="config.yaml",)
parser.add_argument('--file_out', default="thesis_counter.js",)
parser.add_argument('--delay', default=5, type=int)

args = parser.parse_args()

env = Environment(
    loader=PackageLoader('phd_counter', 'templates'),autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('thesis_counter.js.tpl')

#get the config file
with open(args.config) as f:
    config=yaml.load(f.read())


#clone the repo
directory=tempfile.TemporaryDirectory()
Repo.clone_from(config["phd"]["url"], directory.name)
output=subprocess.call(["latexmk","-pdf",config["phd"]["file"]],cwd=directory.name)
if output != 0:
    exit(-1)

thesis_file_name=os.path.join(directory.name,config["phd"]["file"]).replace("tex","pdf")


with open(thesis_file_name, "rb") as f:
    thesis_file = PdfFileReader(f)
    pages_count=thesis_file.getNumPages()


words_count=int(subprocess.check_output('pdftotext %s  -|wc -w'%thesis_file_name,
                        shell=True))


with open("contrib/countUp.js", "r") as f:
    countUp=f.read()

with open(args.file_out,"w") as f:
    f.write("%s"% jsmin(countUp+"\n"+template.render(pages_count=pages_count, words_count=words_count,delay=args.delay)))
