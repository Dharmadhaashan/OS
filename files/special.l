%{
#include<stdio.h>
%}

%%
[^a-zA-Z0-9 \n]   { printf("Special Character: %s\n", yytext); }
%%

int main(){
    yylex();
    return 0;
}