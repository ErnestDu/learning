#include <iostream>
using namespace std;
int main()
{
	string user_name;
	cin >> user_name;
	cout << user_name << endl;
	int num_tries(0);
	cout << num_tries << endl;
	int ival = 1024;
	int *pi;
	cout << ival << endl;
	cout << &ival << endl;
	pi = &ival;
	cout << *pi << endl;
	return 0;
}
