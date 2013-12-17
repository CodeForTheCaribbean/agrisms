from rapidsms.contrib.handlers import KeywordHandler
import urllib2, json


class FindHandler(KeywordHandler):
  keyword = "find"

  def help(self):
    """ Responds with valid commands """
    self.respond("Valid command: Find: [FARMER_ID]")

  def handle(self, text):
    text = text.strip().lower()
    data_type = 'http://localhost:3500/farmers/' + text
    data = json.load(urllib2.urlopen(data_type))
    name = data['first_name']
    self.respond(name)