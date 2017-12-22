//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
using namespace std;



void loop() { 
	int air = eHealth.getAirFlow();
	printf("AIR= %d\n",air);	
	///eHealth.airFlowWave(air);  
	delay(50);
}

int main (){


std::ofstream myfile;
	myfile.open("/home/pi/Documents/robotdocteur/Data/airflowdata.txt", ios::out );
if (myfile.is_open())
  {
int i=0;
int j=0;
	while(i<200){
	
	int air = eHealth.getAirFlow();
	myfile  <<air<<" ";
	myfile  <<j   <<endl;	


	printf("AIR= %d\n",air);	
	///eHealth.airFlowWave(air);  
	i++;
	j+=50;
	delay(50);

	}
	myfile.close();
  }
	return (0);
}
