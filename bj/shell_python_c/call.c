#include<iostream>

using namespace std;

int multi(int num1, int num2)
{
	return num1*num2;
}

int main(void)
{
	int num1, num2;
	cout << "input two numbers:";
	cin >> num1 >> num2;
	cout << multi(num1, num2) << endl;
}
