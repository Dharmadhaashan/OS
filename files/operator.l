%{
#include <stdio.h>
%}

%%
"=="|"<="|">="|"!="|"<"|">" {printf("Relational operator : %s\n",yytext);}
"&&"|"||"|"!" {printf("Logical Operator : %s",yytext);}
%%

int main(){
    yylex();
    return 0;
}