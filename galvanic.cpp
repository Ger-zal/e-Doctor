//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
#include "iomanip"
using namespace std;


void loop() { 
	
  float conductance = eHealth.getSkinConductance();
  float resistance = eHealth.getSkinResistance();
  float conductanceVol = eHealth.getSkinConductanceVoltage();

  printf("Conductance : %f \n", conductance);    
  printf("Resistance : %f \n", resistance);  
  printf("Conductance Voltage : %f \n", conductanceVol);       

  printf("\n");

  // wait for a second  
  delay(1000);   
}

int main (){

std::fstream myfile;
	myfile.open("/home/pi/Documents/robotdocteur/Data/galvanicdata.txt",ios::out);
if (myfile.is_open())
  {

	int i=0;
	while(i<5){
	float resistance = eHealth.getSkinResistance();
 	float conductanceVol = eHealth.getSkinConductanceVoltage();
	printf("Resistance : %f \n", resistance);  
	printf("Conductance Voltage : %f \n", conductanceVol);   	
	myfile <<fixed << setprecision (2) <<conductanceVol<<" "<<fixed << setprecision (0)<< resistance<<endl;
	delay(200);
	i++;
	}
	myfile.close();
  }
	return (0);
}
