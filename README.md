# YouTrackAppMaker
Make a .App for JetBrains YouTracker


To build an app run: 

```bash
./make_app.sh
```

The output will be in `./dist/`. You can move the bundle to your `Applications` folder.

If you need/want to re-create the icon set, uncomment the respective lines in the `make_app.sh` script.

After launching (it may take a few seconds), you need to run "start" (and then "stop") from the top-bar icon.
Starting and Stopping the service may take a few seconds.


If you rebuild the app after creating some content, you need to click "Upgrade" after the app is launched and start; Then unser `source`, select `$HOME/.youtrack/src`, click "Next" in the next dialogs. All of the data should be present.

It is also goo didea to make a DB backup before updating the app... just in case ;)