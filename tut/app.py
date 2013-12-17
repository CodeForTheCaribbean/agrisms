from rapidsms.apps.base import AppBase

class PingPong(AppBase):

    def handle(self, msg):
        if msg.text == 'tess':
            msg.respond('Her name is Tessanne')
            return True
        return False
