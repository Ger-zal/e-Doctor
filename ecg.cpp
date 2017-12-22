//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
using namespace std;


// The loop routine runs over and over again forever:
void loop() {

  float ECG = eHealth.getECG();

  printf("ECG value :  %f V\n",ECG);
  delay(10);
}

int main (){


std::ofstream myfile;
	myfile.open("/home/pi/Documents/robotdocteur/Data/ecgdata.txt", ios::out );
if (myfile.is_open())
  {
int i=0;
int j=0;
	while(i<1000){
		float ECG = eHealth.getECG();
		myfile  <<ECG<<" ";
		myfile  <<j   <<endl;
		printf("ECG value :  %f V\n",ECG);
		i++;
		j+=10;
		delay(10);
		
	}
	myfile.close();
  }
	return (0);
}
