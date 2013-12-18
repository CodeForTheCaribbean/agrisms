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

    first_name = data['first_name']
    last_name = data['last_name']

    name = "Farmer Name: %s %s" % (first_name,last_name)

    self.respond(name)


class FindCropHandler(KeywordHandler):
  keyword = "rec"

  def help(self):
    self.respond("Valid comment: Rec: [Receipt Number]")

  def handle(self, text):
    text = text.strip().lower()

    try:
      data_type = 'http://localhost:3500/receipts/' + text
      data = json.load(urllib2.urlopen(data_type))
      farmer_info = data['farmer']
      self.respond(farmer_info)
    except IOError:
      self.respond("Invalid Receipt - Command <Receipt ID>")
    #else:
      #self.respond("Invalid receipt")










