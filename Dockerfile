FROM python:3-alpine

EXPOSE 80

COPY ./requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt ; \
	rm /requirements.txt

CMD python3 /sms_proxy.py
