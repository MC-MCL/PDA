# PDA_Runner.py
import sys, os, re, random
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class PDA:
    def __init__(self, out, inp):
        self.vars = {}
        self.out = out
        self.inp = inp
        self.stop = False

    def run(self, code):
        lines = code.replace('\\n', '\n').split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and not line.startswith('#'):
                result = self.exec_line(line)
                if result == 'break':
                    break
                elif result == 'continue':
                    while i < len(lines) and not lines[i].strip().startswith('ru'):
                        i += 1
            i += 1

    def exec_line(self, line):
        if line.startswith('pda(') and line.endswith(')'):
            content = line[4:-1].strip('"')
            self.out(content)
        elif '=' in line:
            parts = line.split('=', 1)
            var = parts[0].strip()
            val = self.eval_expr(parts[1].strip())
            self.vars[var] = val
        elif line.startswith('ru '):
            cond = self.eval_expr(line[3:])
            return cond
        elif line == 'ru':
            return 'break'
        elif line.startswith('否则'):
            return 'else'
        elif line.startswith('xunhuan '):
            var, lst = line[8:].split('=', 1)
            var = var.strip()
            lst = self.eval_expr(lst.strip())
            for item in lst:
                self.vars[var] = item
                return 'loop'
        elif line.startswith('dang '):
            cond = self.eval_expr(line[5:])
            return cond
        return None

    def eval_expr(self, expr):
        expr = expr.strip()
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        if expr in self.vars:
            return self.vars[expr]
        try:
            return int(expr)
        except:
            try:
                return float(expr)
            except:
                return expr

class Runner:
    def __init__(self, file):
        self.root = tk.Tk()
        self.root.title(os.path.basename(file))
        self.root.geometry('700x500')
        self.out = scrolledtext.ScrolledText(self.root, font=('Consolas', 10))
        self.out.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        with open(file, encoding='utf-8') as f:
            PDA(self.out, self.get_input).run(f.read())
        tk.Button(self.root, text='关闭', command=self.root.quit).pack(pady=5)
        self.root.mainloop()

    def get_input(self, msg):
        return simpledialog.askstring('输入', msg)

if __name__ == '__main__' and len(sys.argv) > 1:
    Runner(sys.argv[1])
