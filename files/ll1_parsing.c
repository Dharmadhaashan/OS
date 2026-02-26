#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char stack[50], input[50];
int top = -1, i = 0;

char table[5][6][10] = {
    {"TE'", "", "", "TE'", "", ""},        // E
    {"", "+TE'", "", "", "#", "#"},        // E'
    {"FT'", "", "", "FT'", "", ""},        // T
    {"", "#", "*FT'", "", "#", "#"},       // T'
    {"i", "", "", "(E)", "", ""}           // F
};

char nonTerm[5] = {'E','A','T','B','F'};
char term[6] = {'i','+','*','(',')','$'};

int getNonTerm(char c)
{
    if(c=='E') return 0;
    if(c=='A') return 1;
    if(c=='T') return 2;
    if(c=='B') return 3;
    if(c=='F') return 4;
    return -1;
}

int getTerm(char c)
{
    for(int j=0;j<6;j++)
        if(term[j]==c) return j;
    return -1;
}

void push(char c)
{
    stack[++top]=c;
}

void pop()
{
    top--;
}

int main()
{
    printf("Enter string (end with $): ");
    //i+i*i$ ->a
    //i+*i$  ->na
    scanf("%s", input);

    push('$');
    push('E');

    while(top!=-1)
    {
        if(stack[top]==input[i])
        {
            pop();
            i++;
        }
        else
        {
            int row=getNonTerm(stack[top]);
            int col=getTerm(input[i]);

            if(row==-1 || col==-1 || strlen(table[row][col])==0)
            {
                printf("Rejected\n");
                return 0;
            }

            pop();
            char prod[10];
            strcpy(prod, table[row][col]);

            if(prod[0]!='#')
                for(int k=strlen(prod)-1;k>=0;k--)
                    push(prod[k]);
        }
    }

    if(input[i]=='\0')
        printf("Accepted\n");
    else
        printf("Rejected\n");

    return 0;
}