%{
#include<stdio.h>

int yylex();
void yyerror(char* s);

%}

%token IF ELSE ID 

%%

S : STMD '\n' {printf("Valid Statement");}
  ;

STMD : IF '(' ID ')' STMD
     | IF '(' ID ')' STMD ELSE STMD
     | ID ';'
     ;

%%

int yylex(){
    char c= getchar();

    if(c=='i') return IF;
    if(c=='e') return ELSE;
    if(c=='a' || c=='b') return ID;

    return c;
}

void yyerror(char* s){
    printf("INVALID");
}

int main(){
    printf("Enter the expression : ");
    yyparse();
    return 0;
}