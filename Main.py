import.os
import.datetime
  class assistant:
    """ a small extendable assistant
        -'uses a sample rule based response
    """
def respond (self,text:str)->str
    """ return short response for given text
    """
  text (text or ""). strip()
  if not text:
    return " please say something so that I can help!"
