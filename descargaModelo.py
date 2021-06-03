import gdown

url=https://drive.google.com/file/d/1Pt8Q7kT1ytPk9gBrHBpQBOlfKS1NEUmK/view?usp=sharing

gdown.download(url, output='./modelo-0.1.pth', quiet=True)