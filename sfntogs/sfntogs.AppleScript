tell application "System Preferences"
	activate
	reveal pane "Keyboard"
end tell

delay 0.5

tell application "System Events"
	tell application process "System Preferences"
		tell tab group 1 of window "Keyboard"
			click radio button "Keyboard"
			click checkbox 0
		end tell
	end tell
end tell

delay 0.5

tell application "System Preferences"
	quit
end tell