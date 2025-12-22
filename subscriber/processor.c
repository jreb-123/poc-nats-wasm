#include <stdio.h>
#include <unistd.h>

int main() {
    printf("WASM subscriber listening...\n");
    fflush(stdout);

    while (1) {
        sleep(5);
    }
    return 0;
}
