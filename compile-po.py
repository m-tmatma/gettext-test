import os

for top, dirs, files in os.walk('.'):
	if '.git' in top:
		continue

	for file in files:
		filePath = os.path.join(top, file)
		if filePath.endswith('.po'):
			cmd = "msgfmt.py " + filePath
			print(cmd)
			os.system(cmd)
