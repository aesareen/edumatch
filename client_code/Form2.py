from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
<<<<<<< HEAD
    with open("json")
=======
    f = open("_/theme/json_files/ratings_North%20Carolina%20State%20University.json")
    content = json.load(f)
    print()
>>>>>>> a2e8e1ca8847fcb102118dac07abae021c2eada5

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
