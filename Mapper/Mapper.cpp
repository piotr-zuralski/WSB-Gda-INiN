// Mapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <map>

using namespace std;

int main(int argc, char** argv)
{
	std::map<int, double> mapa;

	mapa[1] = 10;
	mapa[4] = 30;
	mapa[3] = 50;
	mapa[2] = 70;
	
	cout << mapa[2];
	cout << endl;

	mapa.insert(std::pair<int, double>(2, 100));

	//std::map<char, int> second(first.begin(), first.end());
	//std::map<char, int> third(second);

	cout << mapa.size();
	cout << endl;

	std::map<int, double>::iterator item = mapa.begin();
	cout << "mapa contains:\n";
	for (item = mapa.begin(); item != mapa.end(); ++item)
	{
		cout << item->first << " => " << item->second << endl;
	}

	mapa.clear();
	cout << (mapa.size() == 0) << endl;

	//Przygotowaæ testy - testom poddaæ nastêpuj¹ce metody :
	//	• pair<iterator, bool> insert(const value_type& val).
	//	• mapped_type& operator[](const key_type& k).
	//	• iterator find(const key_type& k).
	//	• size_type size() const.
	//	• size_type erase(const key_type& k).
	//	• void clear().
	//	• iterator begin(), iterator end() - iterowaæ po kontenerze

	system("pause");
	
	return 0;
	
}

