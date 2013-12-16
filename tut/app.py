from rapidsms.apps.base import AppBase

class PingPong(AppBase):

    def handle(self, msg):
        if msg.text == 'Life':
            msg.respond('Death')
            return True
        return False
