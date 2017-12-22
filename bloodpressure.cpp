//Include eHealth library
#include "eHealth.h"
#include "stdio.h"
#include "iostream"
#include "fstream"
#include "ctime"
using namespace std;


void setup() { 
  eHealth.readBloodPressureSensor();
  delay(100);    
}



int main (){
	
	setup();

	std::fstream myfile;
	myfile.open("/home/pi/Documents/robotdocteur/Data/bloodpressuredata.txt", ios::in | ios::out | ios::ate );

	if (myfile.is_open())
  	{
  		uint8_t numberOfData = eHealth.getBloodPressureLength();      
  		delay(100);


		///Get only the last value
	  	for (int i = 0; i<=numberOfData-1; i++) { 
    			// The protocol sends data in this order 
    			printf("==========================================");

    			printf("Measure number ");
   			 printf("%d\n",i + 1);
 
  			  myfile<< 2000 + eHealth.bloodPressureDataVector[i].year<<"-"; 
  			  myfile<< 0 + eHealth.bloodPressureDataVector[i].month <<"-";
  			  myfile<< 0+ eHealth.bloodPressureDataVector[i].day ;    
  			  myfile <<" ";
  			  
			///if (eHealth.bloodPressureDataVector[i].hour < 10) {
  			///    myfile <<"0"; // Only for best representation.
   			/// }

   			/// myfile << 0+ eHealth.bloodPressureDataVector[i].hour <<":";
   			 
  			 /// if (eHealth.bloodPressureDataVector[i].minutes < 10) {
  			///    myfile<< "0";// Only for best representation.
  			///  }
  			///  myfile <<0+eHealth.bloodPressureDataVector[i].minutes<<" ";
			
  			  printf("Systolic value : ");  
  			 myfile<< 30+eHealth.bloodPressureDataVector[i].systolic;
   			 printf(" mmHg\n");
    
   			 printf("Diastolic value : "); 
   			 myfile <<" "<<0+eHealth.bloodPressureDataVector[i].diastolic;
   			 printf(" mmHg\n");
    
   			 printf("Pulse value : "); 
   			 myfile<< " "<<0+eHealth.bloodPressureDataVector[i].pulse<<endl;
   			 printf(" bpm\n");
 			 }
	
	myfile.close();
  	}
	return (0);
}