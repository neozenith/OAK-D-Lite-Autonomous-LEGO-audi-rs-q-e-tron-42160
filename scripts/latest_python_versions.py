import subprocess
import dataclasses
from itertools import groupby

result = subprocess.run("pyenv install --list", capture_output=True, shell=True, text=True)
tidy_versions = {
    pyversion.strip(): tuple([int(d) for d in pyversion.strip().split(".")])  
    for pyversion in result.stdout.strip().split("\n") 
    if pyversion.strip().startswith("3.") and "dev" not in pyversion and all([d.isdigit() for d in pyversion.strip().split(".")])
}
print(tidy_versions)

grouped_versions = groupby(tidy_versions.items(), lambda k, v: v[1] )
max_versions = [max(g, key=lambda x: x) for k, g in grouped_versions]
print(max_versions)