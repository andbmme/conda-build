import os
import subprocess
import sys
import pkg1
pkg1.main()
bindir = 'Scripts' if sys.platform == 'win32' else 'bin'
print("attempting to call ", os.path.join(os.getenv('PREFIX'), bindir, 'pkg1'))
subprocess.check_call([os.path.join(os.getenv('PREFIX'), bindir, 'pkg1')])
