#include<stdio.h>
#include<string.h>

int main(){
    char prod[50];
    char nont,alpha[20],beta[20];
    int i=0,j=0;

    printf("Enter production : ");
    scanf("%s",prod);

    nont = prod[0];

    char *rhs = strchr(prod,'>')+1;
    char *p1 = strtok(rhs,"|");
    char *p2 = strtok(NULL,"|");

    if(p1[0]==nont){
        strcpy(alpha,p1+1);
        strcpy(beta,p2);
    }
    else{
        strcpy(alpha,p2+1);
        strcpy(beta,p1);
    }

    printf("\nAfter removing left recursion:\n");
    printf("%c -> %s%c'\n",nont,beta,nont);
    printf("%c' -> %s%c | e\n",nont,alpha,nont);

    return 0;

}