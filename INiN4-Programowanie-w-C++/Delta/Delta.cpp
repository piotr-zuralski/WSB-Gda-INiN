// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <stdlib.h>  
#include <stdio.h>  
#include <iostream>
#include "math.h"
using namespace std;

double Delta(int a, int b, int c)
{
	return ((b*b) - (4 * a*c));
}

double DeltaPierwiastek(double delta)
{
	return sqrt(delta);
}

int main()
{
	int a, b, c;
	double delta, delta_pierwiastek;
	cout << "Podaj liczbe a: ";
	cin >> a;

	if (a == 0)
	{
		cout << "Nieprawidlowy argument - to nie jest rownanie kwadratowe";
		system("pause");
		return 0;
	}

	cout << "Podaj liczbe b: ";
	cin >> b;

	cout << "Podaj liczbe c: ";
	cin >> c;

	cout << endl << endl;

	double x0, x1, x2;
	delta = Delta(a, b, c);
	delta_pierwiastek = DeltaPierwiastek(delta);

	x1 = ((b - delta_pierwiastek) / 2 * a);
	x2 = ((b + delta_pierwiastek) / 2 * a);
	x0 = (-b / (2 * a));

	cout << "Delta: " << delta;
	cout << endl;
	cout << "Pierwiastek z delty: " << delta_pierwiastek;
	cout << endl << endl;

	if (delta < 0)
	{
		cout << "Funkcja nie posiada mniejsc zerowych.";
		cout << " " << endl;
	}
	else if (delta == 0)
	{
		cout << "x0: " << x0;
		cout << " " << endl;
	}
	else if (delta > 0)
	{
		cout << "x1: " << x1;
		cout << " " << endl;
		cout << "x2: " << x2;
	}
	cout << endl;

	system("pause");
	return 0;
}

