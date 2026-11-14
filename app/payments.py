def charge(amount):
    from .gateway import Gateway
    return Gateway().send(amount)
