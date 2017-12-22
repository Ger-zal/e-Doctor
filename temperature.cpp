//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
#include "iomanip"
using namespace std;


int main (){
	std::fstream myfile;
	myfile.open("Data\temperaturedata.txt", ios::in | ios::out | ios::ate);
if (myfile.is_open())
  {
int i=0;
	//setup();
	while(i<1){
		delay(10000);
		time_t now = time(0);
   		tm *ltm = localtime(&now);
		float temperature = eHealth.getTemperature(); 

		myfile   << 1900+ltm->tm_year<<"-"<< 1+ltm->tm_mon <<"-" << ltm->tm_mday;
		myfile  <<" "<<fixed << setprecision (1) << temperature<<endl;
		
		///myfile  << ltm->tm_hour <<":" ;
		///myfile  <<ltm->tm_min <<":";
		///myfile  << ltm->tm_sec  ;<<" ";
		
		printf("Temperature : %.1f \n", temperature);
		i++;	
	}
	myfile.close();
  }

	return (0);
}
