import re
from bs4 import BeautifulSoup

# t = '''
# <a class="card release__card" href="/project/Django/1.1/"> 
# <a class="card release__card" href="/project/Django/1.1/"> 
# <a href="https://files.pythonhosted.org/packages/a2/40/42ddc0f9156e7d9d75ef2e7c78ab6f21619ba409c7934cccc32d6c0597ba/numpy-1.21.4-cp37-cp37m-win32.whl">
# <a href="https://files.pythonhosted.org/packages/5a/29/57691d477283b8683acac34ba8e9548f1f5ec936d041ab7abb6f81577d2a/numpy-1.21.4-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl">
# <a href="https://files.pythonhosted.org/packages/c0/d0/c4bc6c65e2aad2904b78d4fe12772e5d89fa3f26f9d28813c72d2e878720/numpy-1.21.4-cp39-cp39-macosx_10_9_universal2.whl">
# <a href="https://files.pythonhosted.org/packages/fb/48/b0708ebd7718a8933f0d3937513ef8ef2f4f04529f1f66ca86d873043921/numpy-1.21.4.zip">
# '''

def meets_conditions(s):
	p = r'(macosx|manylinux|.zip)'
	result = re.search(p, s)
	if result:
		return False
	return True


with open("s.html", 'r') as f:
	s = f.read()

# html = BeautifulSoup(s, "html.parser")
# tags = str(html('a'))

# pat = r'href="https:\/\/files.pythonhosted.org\/packages\/(?!.*manylinux)(?!.*macosx)(.*?)(?<!\.zip)"'
# pat = r'(?!.*manylinux)(?!.*macosx)href="(https:\/\/files.pythonhosted.org\/packages\/.*?)(?<!\.zip)"'
# pat = r'(?!.*(macosx|manylinux)).*href="(https://files.pythonhosted.org/packages/.*?)"'

pat = r'href="(https://files.pythonhosted.org/packages/.*?)"'
x = re.findall(pat, s, flags=re.MULTILINE)
x = [(i, i.split('/')[-1]) for i in x if meets_conditions(i)]

for a in x:
	print(a)

# t = "https://files.pythonhosted.org/packages/d5/99/7d0271fac620d938ad4fc06a53d9d42245529a1ced5416dd6744b93afe78/numpy-1.21.4-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl"
# p = r'(macosx|manylinux|.zip)'
# r = re.search(p, t)
# print(r)

