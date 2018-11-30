If you want to make changes to the AppleScript, do it in `snatsrl.AppleScript` first then copy the contents inside Alfred's _Run NSAppleScript_ code. 

Alfred does not reference `snatsrl.AppleScript` directly. We just store it as a seprate file for backup since Alfred puts the actual code inside `info.plist`.