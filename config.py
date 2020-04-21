# This file contains destinations and upstream sources. It's Python so clever trickery
# can be performed based on context (such as a different destination on Linux, or
# something). All variables in the global scope become paths to evaluate, and they use
# underscores in a funny way. See magic() for more. Any variable in the global scope
# starting with '_' is ignored, so make use of that if you must import or some such.

vscode_settings_json = "~/Library/Application Support/Code/User/settings.json"
