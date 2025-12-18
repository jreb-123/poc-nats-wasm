#include <stdio.h>

__attribute__((export_name("process")))
int process() {
    printf("WASM processed message\n");
    return 0;
}
