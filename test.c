#include <sys/sdt.h>

int main()
{
    DTRACE_PROBE(test, probe_noarg_0);
    DTRACE_PROBE(test, probe_noarg_1);
    DTRACE_PROBE1(test, probe_arg_0, "myarg0");
    DTRACE_PROBE1(test, probe_arg_1, "myarg1");

    while(1) {}

    return 0;
}
