FROM python:3.10.0-bullseye

COPY main.py /main.py
COPY entorypoint.sh /entorypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
