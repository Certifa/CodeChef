#include <stdio.h>

int main(void) {
	int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,x,y;
        scanf("%d%d%d",&n,&x,&y);
        if (n <= (x*y))
        {
            printf("YES \n");
        } else
        {
            printf("NO \n");
        }
    }
	return 0;
}
