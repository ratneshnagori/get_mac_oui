FROM python:3

RUN pip3 install requests

COPY get_mac_oui.py .

CMD ["python", "./get_mac_oui.py"]
