import config

from twilio.rest import Client


def handler(event=None, context=None):
    """
    Function to text a funny photo to Lauren Goemaat
    """
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body='Hi!',
        from_=config.TWILIO_SENDER_NUMBER,
        to=config.TWILIO_RECIPIENT_NUMBER,
        media_url=config.TWILIO_MEDIA_URL,
    )


if __name__ == '__main__':
    handler()
