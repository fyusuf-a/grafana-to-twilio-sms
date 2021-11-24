# grafana-to-twilio-sms
A containerized proxy to be placed between Grafana (which supports webhooks but does not allow for the body of a POST to be changed) and Twilio SMS API.

The goal is to have a SMS notification channel working within Grafana.

# Install

Choose the port on which the proxy should listen in the `docker-compose.yml` (default is 3030).
Put in a `.env` file at the root of the directory with your Twilio account details and the phone numbers used (FROM is the number given to you by Twilio and TO is the number you want to be alerted on.

```
docker-compose -d up
```

Then set up a new notification channel in Grafana as such:

![Screeshot from Grafana](https://github.com/fyusuf-a/grafana-to-twilio-sms/grafana.png)
