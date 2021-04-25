import npyscreen
import _curses
import requests
import time
from npyscreen import FixedText
from npyscreen.wgNMenuDisplay import HasMenus

class App(npyscreen.NPSAppManaged):
    clusterAmount = 0
    loc = ""

    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
 
class FirstForm(npyscreen.ActionFormMinimal, npyscreen.FormWithMenus):
    def drawLine(self,text,relx,rely):
        self.add(npyscreen.TitleText, w_id="sun", name=text,editable = False, relx = relx,rely = rely)

    def create(self):
        self.add(npyscreen.FixedText, w_id="welcometxt",  value = "This is a KMeans plotter GL." )
        self.add(npyscreen.TitleText, w_id="loc", name= "Enter your preferred location: " )
        self.add(npyscreen.TitleText, w_id="clusteramount", name= "Enter your preferred cluster amount: " )

    def on_ok(self):
        if self.get_widget("clusteramount").value == "" or self.get_widget("loc").value == "":
            npyscreen.notify_confirm("You entered some variable wrong.", title="Error Message", wrap=True, wide=True, editw=1)
            return

        App.clusterAmount = self.get_widget("clusteramount").value
        App.loc = self.get_widget("loc").value
        print("Exited terminal with code 0")
        self.parentApp.switchForm(None)
    

