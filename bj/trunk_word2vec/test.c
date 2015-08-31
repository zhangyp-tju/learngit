#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <pthread.h>

#define MAX_STRING 60

const int vocab_hash_size = 500000000; // Maximum 500M entries in the vocabulary

typedef float real;                    // Precision of float numbers

struct vocab_word 
{
  long long cn;//¥ ∆µ
  char *word;//¥ ”Ô
};



int main(int argc,char **argv)
{
    printf("33333\n");
    if(argc < 2)
        printf("Usage: ./test <FILE>\n");
    char filename[100];
    char ch;
    char word[100];
    strcpy(filename,argv[1]);
    printf("$$$$$\n");
    FILE *fin = fopen(filename,"r");
    if (NULL == fin)
        printf("the file %s is not existing",filename);
    int a = 0;
    while (!feof(fin))
    {
       ch =  fgetc(fin);
       //if (ch == 13) continue;
       if ((' '== ch) || ('\t' == ch) || ('\n' == ch))
       {
            word[a] = '\0';
            if (0 == a) continue;
            printf("words = %s\n",word);
            a = 0;
            continue;
       }
       word[a++] = ch;
       //printf("***%c\n",ch);
    }
    FILE *fw = fopen("./test2.data","w");
    fseek(fin,0,SEEK_SET);
    char buf[6];
    while (!feof(fin))
    {
        fgets(buf,5,fin);
        printf("%s\t",buf);
        //fwrite(buf,fw);
        fputs(buf,fw);
    }
    fclose(fin);
    fclose(fw);

    return 0;
}




