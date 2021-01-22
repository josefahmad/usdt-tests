#!/usr/bin/python

import bcc
import sys

pid = int(sys.argv[1])
path = sys.argv[2]

bpf_text = """
#include <linux/ptrace.h>

int probe_func(struct pt_regs *ctx) {
    return 0;
}
"""

u = bcc.USDT(pid=pid, path=path)


### works 
u.enable_probe(probe="probe_noarg_0", fn_name="probe_func")
u.enable_probe(probe="probe_noarg_1", fn_name="probe_func")

### doesn't work
u.enable_probe(probe="probe_arg_0", fn_name="probe_func")
u.enable_probe(probe="probe_arg_1", fn_name="probe_func")

b = bcc.BPF(text=bpf_text, usdt_contexts=[u])

while(True):
    pass
