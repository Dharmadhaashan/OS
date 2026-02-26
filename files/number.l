%{
#include<stdio.h>
int i=0,f=0;
%}

%%
[0-9]+"."+[0-9]+ {f++;}
[0-9]+ {i++;}
%%

int main(){
    yylex();
    printf("Total number of integer is %d",i);
    printf("Total number of float is %d",f);
    return 0;
}