#include<stdio.h>
#include<string.h>

int main()
{
    char prod[50];
    char part1[20], part2[20];
    char common[20];
    int i=0;

    printf("Enter production (A->ab|ac): ");
    scanf("%s", prod);

    char *rhs = strchr(prod,'>')+1;
    char *p1 = strtok(rhs,"|");
    char *p2 = strtok(NULL,"|");

    strcpy(part1,p1);
    strcpy(part2,p2);

    while(part1[i]==part2[i]){
        common[i]=part1[i];
        i++;
    }
    common[i]='\0';

    printf("\nAfter left factoring:\n");
    printf("%c -> %s%c'\n", prod[0], common, prod[0]);
    printf("%c' -> %s | %s\n", prod[0], part1+i, part2+i);

    return 0;
}