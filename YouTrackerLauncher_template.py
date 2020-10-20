#!/usr/bin/env python
import rumps
import subprocess
import sys
import os

rumps.debug_mode(True)

class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("YT")
        self.basedir = "{{BASEDIR}}"
        self.icon = os.path.join(self.basedir, "src/apps/youtrack/web/favicon.ico")
        self.menu = ["Toggle"]
        self.toggle = self.menu['Toggle']
        self.toggle.title = "Start"
        self.quit_button=None


    @rumps.clicked("Toggle")
    def prefs(self, sender):
        toggle = self.menu['Toggle']
        if toggle.title == "Start":
            rumps.notification("YouTrack", "Launching YouTrack", "This may take a few seconds...")
            subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "start"],  stdout=sys.stdout, stderr=sys.stderr)
            rumps.notification("YouTrack", "Started", "")
            toggle.title = "Stop"
        
        else:
            rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...")
            subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "stop"],  stdout=sys.stdout, stderr=sys.stderr)
            rumps.notification("YouTrack", "Stopped", "")
            toggle.title = "Start"


    @rumps.clicked('Quit')
    def clean_up_before_quit(self, _):
        rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...")
        subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "stop"],  stdout=sys.stdout, stderr=sys.stderr)
        rumps.notification("YouTrack", "Stopped", "")
        rumps.quit_application()


app=App().run()
