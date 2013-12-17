from rapidsms.contrib.handlers import KeywordHandler
from django.db.models import F

from .models import Choice

class ResultsHandler(KeywordHandler):
  keyword = "results"

  def help(self):
    """ help() get invoked when we get the 'results' message with no arguments"""
    parts = []

    for choice in Choice.objects.all():
      part = "%s: %d" % (choice.name, choice.votes)
      parts.append(part)

    #combine the parts into the response, with a semicolon after each
    msg = "; ".join(parts)

     #Respond
    self.respond(msg)

    def handle(self, text):
      """ This gets called if any arguments are given along with RESULTS, but we don't care. just call help as if they passed no arguments)"""
      self.help()

class VoteHandler(KeywordHandler):
  keyword = "vote"

  def help(self):
    """ Respond with the valid commands. eg.) VOTE <Moe|Larry|Curly>"""
    choices = "|".join(Choice.objects.values_list('name', flat=True))
    self.respond("Valid commands: VOTE <%s>" % choices)

  def handle(self, text):
    text = text.strip()
    #look for a choice that matches the attempted vote
    try:
      choice = Choice.objects.get(name__iexact=text)
    except Choice.DoesNotExist:
      #send help
      self.help()
    else:
      #count the vote, use update to do it in a single query
      Choice.objects.filter(name__iexact=text).update(votes=F('votes')+1)
      self.respond("Your vote for %s has been counted " % text)

