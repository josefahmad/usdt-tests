Reproducer of https://github.com/iovisor/bcc/issues/3240

```
$ gcc -o test test.c
$ ./test &
$ sudo python test-usdt.py $(pidof test) $(pwd)/test
```

This should fail with something similar to `/virtual/main.c:7:28: error: redefinition of '_bpf_readarg_probe_func_1'`

Then open up `test-usdt.py`, comment out the attach_probe for probe_arg_0 and
probe_arg_1 and re-run test-usdt.py to see it work fine.
