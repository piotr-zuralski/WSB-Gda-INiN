// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <stdlib.h>  
#include <stdio.h>  
#include <iostream>
#include "math.h"
using namespace std;

double NWD(int a, int b)
{
	while (a != b)
	{
		if (a > b)
		{
			a -= b;
		}
		else 
		{
			b -= a;
		}
	}
	return a;
}

int main()
{
	int a, b, nwd;
	cout << "Podaj liczbe a: ";
	cin >> a;

	cout << "Podaj liczbe b: ";
	cin >> b;

	nwd = NWD(a, b);

	cout << "Najwiekszy wspolny dzielnik liczb " << a << " oraz " << b << " wynosi " << nwd;
	cout << endl;

	system("pause");
    return 0;
}

