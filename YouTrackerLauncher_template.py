#!/usr/bin/env python
import rumps
import subprocess
import sys
import os
import re
import webbrowser

rumps.debug_mode(True)

class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("YT")
        self.basedir = "{{BASEDIR}}"
        self.icon = os.path.join(self.basedir, "src/apps/youtrack/web/favicon.ico")
        self.menu = ["Open", "Toggle"]
        self.toggle = self.menu['Toggle']
        self.toggle.title = "Start"
        self.quit_button=None
        self.menu['Open'].set_callback(None)


    def open_window(self, _):
        rumps.notification("YouTrack", "Opening", "", sound=False)
        webbrowser.open_new_tab(self.url)

    @rumps.clicked("Toggle")
    def prefs(self, sender):
        toggle = self.menu['Toggle']
        if toggle.title == "Start":
            rumps.notification("YouTrack", "Launching YouTrack", "This may take a few seconds...", sound=False)
            proc_output = subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "start"], capture_output=True)
            re_res = re.search(".*available on .*\[(http.*)\].*",proc_output.stdout.decode('utf-8'))
            if re_res:
                self.url = re_res.group(1)
            
            toggle.title = "Stop"
            self.menu['Open'].set_callback(self.open_window)
            rumps.notification("YouTrack", "Started", "", sound=False)
            
        
        else:
            rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...", sound=False)
            subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "stop"],  stdout=sys.stdout, stderr=sys.stderr)
            toggle.title = "Start"
            self.menu['Open'].set_callback(None)
            rumps.notification("YouTrack", "Stopped", "", sound=False)
            


    @rumps.clicked('Quit')
    def clean_up_before_quit(self, _):
        rumps.notification("YouTrack", "Stopping YouTrack", "This may take a few seconds...", sound=False)
        subprocess.run([ os.path.join(self.basedir, "src/bin/youtrack.sh"), "stop"],  stdout=sys.stdout, stderr=sys.stderr)
        rumps.notification("YouTrack", "Stopped", "", sound=False)
        rumps.quit_application()


app=App().run()
