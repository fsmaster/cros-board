FROM python:3

ADD cros-board.py /

RUN pip install --upgrade pip && \
    pip install numpy pandas colorama progress

CMD [ "python", "./cros-board.py"]
