#!/usr/bin/env python3
import argparse
import subprocess

from jsmin import jsmin
from jinja2 import Environment, PackageLoader, select_autoescape
from PyPDF2 import PdfFileReader


parser = argparse.ArgumentParser(description='Generate js counter of a pdf document')

parser.add_argument('--file_in', default="thesis.pdf",)
parser.add_argument('--file_out', default="thesis_counter.js",)
parser.add_argument('--delay', default=5, type=int)

args = parser.parse_args()

env = Environment(
    loader=PackageLoader('phd_counter', 'templates'),autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('thesis_counter.js.tpl')
with open(args.file_in, "rb") as f:
    thesis_file = PdfFileReader(f)
    pages_count=thesis_file.getNumPages()


words_count=int(subprocess.check_output('pdftotext %s  -|wc -w'%args.file_in,
                        shell=True))


with open("contrib/countUp.js", "r") as f:
    countUp=f.read()

with open(args.file_out,"w") as f:
    f.write("%s"% jsmin(countUp+"\n"+template.render(pages_count=pages_count, words_count=words_count,delay=args.delay)))
