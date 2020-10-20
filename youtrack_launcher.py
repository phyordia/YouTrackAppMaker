#!/usr/bin/env python
import rumps
import subprocess
import sys
rumps.debug_mode(True)

class App(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("YT")
        self.icon = "../Resources/youtrack/apps/youtrack/web/favicon.ico"
        self.menu = ["Toggle"]
        self.toggle = self.menu['Toggle']
        self.toggle.title = "Start"


    def print_something(self, _):
        rumps.alert(message='something', ok='YES!', cancel='NO!')


    @rumps.clicked("Toggle")
    def prefs(self, sender):
        toggle = self.menu['Toggle']
        if toggle.title == "Start":
            rumps.notification("YouTrack", "Launching YouTrack", "This may take a few seconds...")
            subprocess.run(["../Resources/youtrack/bin/youtrack.sh", "start"],  stdout=sys.stdout, stderr=sys.stderr)
            rumps.notification("YouTrack", "Started", "")
            toggle.title = "Stop"
        
        else:
            rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...")
            subprocess.run(["../Resources/youtrack/bin/youtrack.sh", "stop"],  stdout=sys.stdout, stderr=sys.stderr)
            rumps.notification("YouTrack", "Stopped", "")
            toggle.title = "Start"




    @rumps.clicked('Clean Quit')
    def clean_up_before_quit(_):
        rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...")
        subprocess.run(["../Resources/youtrack/bin/youtrack.sh", "stop"],  stdout=sys.stdout, stderr=sys.stderr)
        rumps.notification("YouTrack", "Stopped", "")
        rumps.quit_application()


app=App().run()
