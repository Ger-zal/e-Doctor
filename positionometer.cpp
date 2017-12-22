//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
#include "iomanip"
using namespace std;


void setup(){
	eHealth.initPositionSensor();
}

void loop(){
	printf("Current position : \n");
	uint8_t position = eHealth.getBodyPosition(); 
	eHealth.printPosition(position);  

	printf("\n");
	delay(3000);
}

int main (){
std::ofstream myfile;
	myfile.open("/home/pi/Documents/robotdocteur/Data/positionometerdata.txt", ios::out );
if (myfile.is_open())
	{
int i=0;
std::string pos="";
	setup();
	while(i<10){
		time_t now = time(0);
   		tm *ltm = localtime(&now);
		uint8_t position = eHealth.getBodyPosition();
		if      (position == 1) {pos="Prone position" ;
					printf("Prone position\n");} 
		else if (position == 2) {pos="Stand or sit position";
					printf("Stand or sit position\n");} 
		else if (position == 3) {pos="Left lateral decubitus";
					printf("Left lateral decubitus\n");} 
		else if (position == 4) {pos="Supine position";
					printf("Supine position\n");} 
		else if (position == 5) {pos="Rigth lateral decubitus";
					printf("Rigth lateral decubitus\n");} 
		else 		        {pos="non-defined position";
					printf("non-defined position\n");}

		myfile  <<"At" <<ltm->tm_hour <<":" ;
		myfile  <<ltm->tm_min <<":";
		myfile  << ltm->tm_sec  <<" you have been in "<<pos <<endl;
		delay(2000);
		i++;
	
		}
	myfile.close();
  	}
	

	return (0);
}
