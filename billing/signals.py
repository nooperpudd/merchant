from django.dispatch import Signal

transaction_started = Signal()

transaction_was_successful = Signal(providing_args=["type"])
transaction_was_unsuccessful = Signal(providing_args=["type"])
