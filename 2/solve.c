#include <stdio.h>
#include <limits.h>

#define N 5000

int piles[N];
int reductions[N]; // total from the left
struct {
    int child;
    int parent;
} cache[N+1];

int main() {
    int total = 0;

    for (int i=0; i<N; ++i) {
        scanf("%d\n", &piles[i]);
        total += piles[i];
        reductions[i] = total;
    }

    // i represents how many piles are left; for any i < 2, the game is over
    // and for i=2 the score the player whose move it is gets is the total of all piles
    cache[2].child = total;
    cache[2].parent = -total;
    for (int i=3; i<=N; ++i) {
        // for all available moves, calculate the final score 
        cache[i].child = INT_MIN;
        cache[i].parent = INT_MAX;

        for (int m=2; m<=i; ++m) {
            int j = i - m + 1;
            // for the child, the best outcome is a total score as large as possible
            int child = reductions[N - j] + cache[j].parent;
            if (child > cache[i].child) cache[i].child = child;

            // for the parent, the opposite is true
            int parent = -reductions[N - j] + cache[j].child;
            if (parent < cache[i].parent) cache[i].parent = parent;
        }
    }

    printf("best = %d\n", cache[N].child);
}
