// Kalkulator.cpp : Defines the entry point for the console application.

#include "stdafx.h"
#include <string>
#include <stdlib.h>  
#include <stdio.h>  
#include <iostream>
#include "math.h"
using namespace std;

int main()
{
	string liczba1, liczba2, wynik;
	int start_point = 0, przeskok1 = 0, przeskok2 = 0;
	
	//cout << "Podaj 1 liczbe: ";
	//cin >> liczba1;
	liczba1 = "1245";

	//cout << "Podaj 2 liczbe: ";
	//cin >> liczba2;
	liczba2 = "78";

	if (liczba1.length() > liczba2.length()) {
		start_point = liczba2.length();
		przeskok1 = liczba1.length() - liczba2.length();
	} else {
		start_point = liczba1.length();
		przeskok2 = liczba2.length() - liczba1.length();
	}

	for (int i = 0; i < start_point; i++) {
		if (liczba1.length() > liczba2.length()) {
			wynik += liczba1[i];
		}
		else {
			wynik += liczba2[i];
		}
	}

	cout << "start_point " << start_point << endl;
	cout << "1 " << liczba1 << " len " << liczba1.length() << endl;
	cout << "2 " << liczba2 << " len " << liczba2.length() << endl;
	cout << "Przeskok 1 " << przeskok1 << " Przeskok 2 " << przeskok2 << endl;
	cout << "wynik " << wynik << endl;
	
	int tmp = 0;
	for (int i = 0; i < start_point; i++) {
		tmp = (liczba1[przeskok1 + i] + liczba2[przeskok2 + i]);
		wynik += tmp;
		tmp = 0;
	}

	cout << "wynik " << wynik << endl;
	
	
	system("pause");
	return 0;
}

