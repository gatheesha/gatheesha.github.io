import pathlib
import os
import re

html = ""
cap = ""
alt = ""
s1 = "{{"
s2 = "}}"


for file in pathlib.Path(".").iterdir():
	if file.is_file():
		if str(file).endswith(".jpg"):
			cap = re.sub(r"\B([A-Z])", r" \1", str(file.stem).replace("-", " "))
			cap = re.sub(r'\b\d{1,2}.', r"", str(cap))
			alt = cap.lower().replace(" ", "-")
			html += f'{s1}<figure src="/img/designs/{file}" \n alt="{alt}"\n caption="{cap}">{s2}\n \n'
			print(html)


with open("figs.txt", "w") as outputfile:
	outputfile.write(html)
	

os.startfile("figs.txt")


# {{<figure src="/img/designs/art-nuteshelldiysc3.webp"
#       alt="NushellAnimation DTIYS challenge-unedited"
#       caption="NushellAnimation DTIYS challenge-unedited">}}