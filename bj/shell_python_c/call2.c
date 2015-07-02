#include <stdio.h>
#include <string.h>

char* output(char* name)
{
	char tmp[100] = "Welcome to my home zoon!";
	printf("Welcome to my zoon %s\n",name);
	printf("%s", strcat(tmp, name));
	return name;
}

int multiply(int a, int b)
{
	return a * b;
}

int main(void)
{
	int a,b;
	char *name = "zyp";
	printf("please input two numbers:\n");
	scanf("%d %d",&a,&b);
	printf("output:%d\n",multiply(a,b));
	printf("%s",output(name));
	//printf("**:%s\n",output(name));


}
