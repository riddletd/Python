#!/usr/bin/env python3

import os
from twilio.rest import Client

client = Client("AC6c638ea40825c4259cacd4ff0e175fd", "7dd68c4bb30d18fafb7a8a70577afea2")

client.messages.create(from_="(828) 403-3667", to="(828) 403-3667", body="Hello!")
