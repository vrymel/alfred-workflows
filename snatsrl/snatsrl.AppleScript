on alfred_script(q)
    tell application "System Preferences"
        activate
        reveal pane "Trackpad"
    end tell

    delay 0.5

    tell application "System Events" 
        tell application process "System Preferences"
            tell tab group 1 of window "Trackpad"
                click radio button "Scroll & Zoom"
                click checkbox 1
            end tell
        end tell
    end tell

    delay 0.5

    tell application "System Preferences"
        quit
    end tell
end alfred_script