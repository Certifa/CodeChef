#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int m,n;
	    scanf("%d%d",&m,&n);
	    if(m<=n){
	        printf("0\n");
	    }
	    else {
	        printf("%d\n",m-n);
	    }
	}
	return 0;
}

