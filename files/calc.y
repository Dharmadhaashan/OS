%{
#include <stdio.h>
#include <ctype.h>

int yylex();
void yyerror(char* s);
%}

%token NUM

%%

S : E '\n' { printf("Result : %d\n", $1); }
  ;

E : E '+' T { $$ = $1 + $3; }
  | E '-' T { $$ = $1 - $3; }
  | T
  ;

T : T '*' F { $$ = $1 * $3; }
  | T '/' F { $$ = $1 / $3; }
  | F
  ;

F : '(' E ')' { $$ = $2; }
  | NUM
  ;

%%

int yylex(){
    int c = getchar();

    if(isdigit(c)){
        yylval = c - '0';
        return NUM;
    }

    if(c == '\n')
        return c;

    return c;
}

void yyerror(char* s){
    printf("Invalid Expression\n");   
}

int main(){
    printf("Enter the expression : ");
    yyparse();
    return 0;
}