from os.path import isfile
from ast import literal_eval

# Check if the addon presets file, addonpresets.txt, is present in the current working directory
if not isfile("addonpresets.txt"):
	print("""Couldn't find the addon presets file!
Place me in GarrysMod/garrysmod/settings, or place addonpresets.txt in the same directory as me.""")
	quit()

# Read presets file into string
with open("addonpresets.txt", "r") as f:
	presets_str = f.read()

# Decode the string into a dictionary of presets with the same structure
try:
	presets = literal_eval(presets_str)
except:
	print("Something went wrong while evaluating your presets file. Make sure it's not empty or corrupted.")
	quit()

# Check if there are any presets at all, if not: stop and notify user
if len(presets) == 0:
	print("There are no presets.")
	quit()

# Ask user which preset they wish to use
print("The following presets have been found:")
preset_names = list(presets.keys())
i = 0
for preset_name in preset_names:
	print(str(i+1) + ": " + preset_name)
	i += 1
preset_number = int(input("Use preset number: "))
while not (1 <= preset_number and preset_number <= i+1):
	preset_number = int(input("Use preset number: "))

# Get list of enabled addons from chosen preset
preset = presets[preset_names[preset_number-1]]
addons = preset["enabled"]

# Check that there are addons in the preset
if len(addons) == 0:
	print("There are no enabled addons in the chosen preset.")
	quit()


# Generate js script
script = 'let addons = ["' + '","'.join(addons) + '"];\n'
script += """for (let addonId of addons) {
	ToggleChildInCollection('choice_MySubscribedItems_' + addonId, addonId);
}"""
with open("into_collection.js", "w") as f:
	f.write(script)
print("The js script for inserting the " + str(len(addons)) + " enabled addons of this preset has been placed into into_collection.js")

