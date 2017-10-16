"""
>>> subprocess.check_output("python3 wc.py w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py c testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py c testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: c: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py l testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py l testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: l: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py -w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t22\\ttestinputs/os-release\\n\\t85\\ttestinputs/rc.local\\n\\t61033\\ttestinputs/services\\n\\t1\\ttestinputs/small.txt\\n\\t1\\ttestinputs/small2.txt\\n\\t172\\ttestinputs/zshrc\\n\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -w testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t22\\ttestinputs/os-release\\n\\t85\\ttestinputs/rc.local\\n\\t61033\\ttestinputs/services\\n\\t1\\ttestinputs/small.txt\\n\\t1\\ttestinputs/small2.txt\\n\\t172\\ttestinputs/zshrc\\n\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -w testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -c testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t484\\ttestinputs/os-release\\n\\t531\\ttestinputs/rc.local\\n\\t670293\\ttestinputs/services\\n\\t2\\ttestinputs/small.txt\\n\\t3\\ttestinputs/small2.txt\\n\\t1135\\ttestinputs/zshrc\\n\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -c testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -l testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t15\\ttestinputs/os-release\\n\\t16\\ttestinputs/rc.local\\n\\t11176\\ttestinputs/services\\n\\t1\\ttestinputs/small.txt\\n\\t2\\ttestinputs/small2.txt\\n\\t50\\ttestinputs/zshrc\\n\\t11260\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -l testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py w- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py ww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py ww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: ww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py ww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py ww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: ww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py c- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py c- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: c-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py l- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py l- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: l-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py -ww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t22\\ttestinputs/os-release\\n\\t85\\ttestinputs/rc.local\\n\\t61033\\ttestinputs/services\\n\\t1\\ttestinputs/small.txt\\n\\t1\\ttestinputs/small2.txt\\n\\t172\\ttestinputs/zshrc\\n\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -ww testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -wc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t22\\t484\\ttestinputs/os-release\\n\\t85\\t531\\ttestinputs/rc.local\\n\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t1\\t3\\ttestinputs/small2.txt\\n\\t172\\t1135\\ttestinputs/zshrc\\n\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -wc testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -wl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\ttestinputs/os-release\\n\\t16\\t85\\ttestinputs/rc.local\\n\\t11176\\t61033\\ttestinputs/services\\n\\t1\\t1\\ttestinputs/small.txt\\n\\t2\\t1\\ttestinputs/small2.txt\\n\\t50\\t172\\ttestinputs/zshrc\\n\\t11260\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -wl testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -ww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\ttestinputs/empty.txt\\n\\t22\\ttestinputs/os-release\\n\\t85\\ttestinputs/rc.local\\n\\t61033\\ttestinputs/services\\n\\t1\\ttestinputs/small.txt\\n\\t1\\ttestinputs/small2.txt\\n\\t172\\ttestinputs/zshrc\\n\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -ww testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -wc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t22\\t484\\ttestinputs/os-release\\n\\t85\\t531\\ttestinputs/rc.local\\n\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t1\\t3\\ttestinputs/small2.txt\\n\\t172\\t1135\\ttestinputs/zshrc\\n\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -wc testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -wl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\ttestinputs/os-release\\n\\t16\\t85\\ttestinputs/rc.local\\n\\t11176\\t61033\\ttestinputs/services\\n\\t1\\t1\\ttestinputs/small.txt\\n\\t2\\t1\\ttestinputs/small2.txt\\n\\t50\\t172\\ttestinputs/zshrc\\n\\t11260\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -wl testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -cw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t22\\t484\\ttestinputs/os-release\\n\\t85\\t531\\ttestinputs/rc.local\\n\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t1\\t3\\ttestinputs/small2.txt\\n\\t172\\t1135\\ttestinputs/zshrc\\n\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -cw testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -cw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t22\\t484\\ttestinputs/os-release\\n\\t85\\t531\\ttestinputs/rc.local\\n\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t1\\t3\\ttestinputs/small2.txt\\n\\t172\\t1135\\ttestinputs/zshrc\\n\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -cw testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -cl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t484\\ttestinputs/os-release\\n\\t16\\t531\\ttestinputs/rc.local\\n\\t11176\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t3\\ttestinputs/small2.txt\\n\\t50\\t1135\\ttestinputs/zshrc\\n\\t11260\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -cl testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -lw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\ttestinputs/os-release\\n\\t16\\t85\\ttestinputs/rc.local\\n\\t11176\\t61033\\ttestinputs/services\\n\\t1\\t1\\ttestinputs/small.txt\\n\\t2\\t1\\ttestinputs/small2.txt\\n\\t50\\t172\\ttestinputs/zshrc\\n\\t11260\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -lw testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -lw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\ttestinputs/os-release\\n\\t16\\t85\\ttestinputs/rc.local\\n\\t11176\\t61033\\ttestinputs/services\\n\\t1\\t1\\ttestinputs/small.txt\\n\\t2\\t1\\ttestinputs/small2.txt\\n\\t50\\t172\\ttestinputs/zshrc\\n\\t11260\\t61314\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -lw testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py -lc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t484\\ttestinputs/os-release\\n\\t16\\t531\\ttestinputs/rc.local\\n\\t11176\\t670293\\ttestinputs/services\\n\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t3\\ttestinputs/small2.txt\\n\\t50\\t1135\\ttestinputs/zshrc\\n\\t11260\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -lc testinputs/* 2>&1 >/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py w-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w-c testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-c testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-c: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w-l testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-l testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-l: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py ww- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py ww- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: ww-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wwc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wwc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wwc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wwl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wwl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wwl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wc- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wc- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wc-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wcw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wcw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wcw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wcl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wcl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wcl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wl- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wl- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wl-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wlw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wlw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wlw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wlc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wlc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wlc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w-c testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-c testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-c: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py w-l testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py w-l testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: w-l: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py ww- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py ww- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: ww-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wwc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wwc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wwc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wwl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wwl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wwl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wc- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wc- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wc-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wcw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wcw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wcw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wcl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wcl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wcl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wl- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wl- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wl-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wlw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wlw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wlw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py wlc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py wlc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: wlc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py c-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py c-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: c-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py c-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py c-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: c-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py c-l testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py c-l testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: c-l: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cw- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cw- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cw-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cwl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cwl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cwl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cw- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cw- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cw-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cwl testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cwl testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cwl: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py cl- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py cl- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: cl-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py clw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py clw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: clw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py clw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py clw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: clw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py l-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py l-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: l-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py l-w testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py l-w testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: l-w: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py l-c testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py l-c testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: l-c: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lw- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lw- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lw-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lwc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lwc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lwc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lw- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lw- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lw-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lww testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lww testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lww: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lwc testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lwc testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lwc: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lc- testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lc- testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lc-: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lcw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lcw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lcw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py lcw testinputs/* 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs/empty.txt\\n\\t15\\t22\\t484\\ttestinputs/os-release\\n\\t16\\t85\\t531\\ttestinputs/rc.local\\n\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t1\\t1\\t2\\ttestinputs/small.txt\\n\\t2\\t1\\t3\\ttestinputs/small2.txt\\n\\t50\\t172\\t1135\\ttestinputs/zshrc\\n\\t11260\\t61314\\t672448\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py lcw testinputs/* 2>&1 >/dev/null", shell=True)
b'wc: lcw: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py testinputs 2>/dev/null", shell=True)
b'\\t0\\t0\\t0\\ttestinputs\\n'
>>> subprocess.check_output("python3 wc.py testinputs 2>&1 >/dev/null", shell=True)
b'wc: testinputs: Is a directory\\n'
>>> subprocess.check_output("python3 wc.py -c -- -l testinputs/services 2>/dev/null", shell=True)
b'\\t670293\\ttestinputs/services\\n\\t670293\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py -c -- -l testinputs/services 2>&1 >/dev/null", shell=True)
b'wc: -l: No such file or directory\\n'
>>> subprocess.check_output("python3 wc.py '$' 2>/dev/null", shell=True)
b''
>>> subprocess.check_output("python3 wc.py '$' 2>&1 >/dev/null", shell=True)
b"wc: '$': No such file or directory\\n"
>>> try:
...   subprocess.check_output("python3 wc.py - testinputs/services 2>/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b'\\t11176\\t61033\\t670293\\ttestinputs/services\\n\\t11176\\t61033\\t670293\\ttotal\\n'
>>> subprocess.check_output("python3 wc.py - testinputs/services 2>&1 >/dev/null", shell=True)
b'wc: -: No such file or directory\\n'
>>> try:
...   subprocess.check_output("python3 wc.py -z testinputs/services 2>/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b''
>>> try:
...   subprocess.check_output("python3 wc.py -z testinputs/services 2>&1 >/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b"wc: invalid option -- 'z'\\nTry 'wc --help' for more information.\\n"
>>> try:
...   subprocess.check_output("python3 wc.py --z testinputs/services 2>/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b''
>>> try:
...   subprocess.check_output("python3 wc.py --z testinputs/services 2>&1 >/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b"wc: unrecognised option '--z'\\nTry 'wc --help' for more information.\\n"
>>> try:
...   subprocess.check_output("python3 wc.py testinputs/services -l testinputs/os-release 2>/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b'\\t11176\\ttestinputs/services\\n\\t15\\ttestinputs/os-release\\n\\t11191\\ttotal\\n'
>>> try:
...   subprocess.check_output("python3 wc.py testinputs/services -l testinputs/os-release 2>&1 >/dev/null", shell=True)
... except subprocess.CalledProcessError as e:
...   e.output
b''
"""

if __name__ == "__main__":
  import doctest
  import subprocess
  doctest.testmod()