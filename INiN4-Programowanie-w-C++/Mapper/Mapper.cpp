// Mapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <map>

using namespace std;

class Mapper {

	private: 
		std::map<int, double> mapa;

	public: Mapper() {
		
	}
	public: int init()
	{
		mapa[1] = 10;
		mapa[4] = 30;
		mapa[3] = 50;
		mapa[2] = 70;

		cout << mapa[2];
		cout << endl;
	}
	
	public: string show()
	{
		string result = "";
		std::map<int, double>::iterator item = mapa.begin();
		for (item = mapa.begin(); item != mapa.end(); ++item)
		{
			result += item->first + " => " + item->second + endl;
		}
		return result;
	}

	public: void clear()
	{
		mapa.clear();
	}

	public: int main()
	{
		// mapa.insert(std::pair<int, double>(2, 100));

		//std::map<char, int> second(first.begin(), first.end());
		//std::map<char, int> third(second);

		cout << mapa.size();
		cout << endl;

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

};