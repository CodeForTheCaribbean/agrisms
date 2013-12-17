from rapidsms.contrib.handlers import KeywordHandler
import urllib2, json


class FindHandler(KeywordHandler):
  keyword = "find"

  def help(self):
    """ Responds with valid commands """
    self.respond("Valid command: VOTE: [FARMER]")

  def handle(self, text):
    text = text.strip().lower()
    data = json.load(urllib2.urlopen('http://localhost:3500/farmers/081117657/.json'))
    name = data['last_name']
    self.respond(name)