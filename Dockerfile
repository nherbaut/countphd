from ubuntu
run apt-get update
run apt-get install texlive --yes
run apt-get install python3 python3-pip --yes
run pip3 install jinja2
run apt-get update
run apt-get install git --yes
run apt-get install latexmk --yes
run mkdir -p /opt/phd_counter
run apt-get install texlive-latex-extra --yes
copy ./src/* /opt/phd_counter/
copy ./config.yaml /var/phd_counter/
