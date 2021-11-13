#include <stdio.h>
#include <limits.h>

#define N 5000

int piles[N];
int reductions[N]; // total from the left
int cache[N+1];

int main() {
    int total = 0;

    for (int i=0; i<N; ++i) {
        scanf("%d\n", &piles[i]);
        total += piles[i];
        reductions[i] = total;
    }

    // i represents how many piles are left; for any i < 2, the game is over
    // and for i=2 the score the player whose move it is gets is the total of all piles
    cache[2] = total;
    for (int i=3; i<=N; ++i) {
        // for all available moves, calculate the final score 
        cache[i] = INT_MIN;

        for (int m=2; m<=i; ++m) {
            // for the current player, the best outcome is a total
            // score as large as possible, but the next turn is the opponent!
            int j = i - m + 1;
            int score = reductions[N - j] - cache[j];
            if (score > cache[i]) cache[i] = score;
        }
    }

    printf("best = %d\n", cache[N]);
}
