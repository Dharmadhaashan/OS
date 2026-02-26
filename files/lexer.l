%{
#include<stdio.h>
#include<string.h>

int iskeyword(char *str){
    char *kw[] = {"int","float","if","else","while","return"};
    for(int i=0;i<6;i++){
        if(strcmp(str,kw[i])==0){
            return 1;
        }
    }
    return 0;
}
%}

%%
[0-9]+ { printf("NUMBER\t\t%s\n",yytext); }

"int"|"float"|"if"|"else"|"while"|"return" { printf("KEYWORD\t\t%s\n",yytext); }

[a-zA-Z_][a-zA-Z0-9_]* {
if(iskeyword(yytext))
printf("KEYWORD\t\t%s\n",yytext);
else
printf("IDENTIFIER\t%s\n",yytext);
}

"+"|"-"|"*"|"/"|"="|"=="|"<"|">"|"<="|">="|"!=" { printf("OPERATOR\t%s\n",yytext); }

";"|","|"("|")"|"{"|"}" { printf("DELIMITER\t%s\n",yytext); }

[ \t\n]+ ;

. { printf("UNKNOWN\t\t%s\n",yytext); }
%%

int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}
