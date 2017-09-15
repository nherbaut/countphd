from ubuntu
run apt-get update && apt-get install texlive python3 python3-pip latexmk git texlive-latex-extra texlive-full poppler-utils --yes --no-install-recommends && rm -rf /var/lib/apt/lists/*
run pip3 install gitdb2==2.0.2 GitPython==2.1.3 Jinja2==2.9.6 jsmin==2.2.2 MarkupSafe==1.0 PyPDF2==1.26.0 PyYAML==3.12 smmap2==2.0.2
run mkdir -p /opt/phd_counter
copy ./src/ /opt/phd_counter/
copy .latexmkrc ~
CMD /opt/phd_counter/counter_gen.py --config /var/phd_counter/config.yaml
