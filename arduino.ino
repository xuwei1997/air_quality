#include<SoftwareSerial.h>

static unsigned int pm_cf_10;           //定义全局变量
static unsigned int pm_cf_25;
static unsigned int pm_cf_100;
static unsigned int pm_at_10;
static unsigned int pm_at_25;
static unsigned int pm_at_100;
static unsigned int particulate03;
static unsigned int particulate05;
static unsigned int particulate10;
static unsigned int particulate25;
static unsigned int particulate50;
static unsigned int particulate100;
static float HCHO;
static unsigned int sum;

SoftwareSerial mySerial(10, 11); //第10= RX,第11- TX

void getG5(unsigned char ucData)//获取G5的值
{
  static unsigned int ucRxBuffer[250];
  static unsigned int ucRxCnt = 0;
  ucRxBuffer[ucRxCnt++] = ucData; 
  if (ucRxBuffer[0] != 0x42 && ucRxBuffer[1] != 0x4D)//数据头判断
  {
    ucRxCnt = 0;
    return;
  }
  if (ucRxCnt > 32)//数据位判断
  {
         pm_cf_10=(int)ucRxBuffer[4] * 256 + (int)ucRxBuffer[5];                       //CF=1下,PM1.0浓度计算        
         pm_cf_25=(int)ucRxBuffer[6] * 256 + (int)ucRxBuffer[7];		       //CF=1下,PM2.5浓度计算
         pm_cf_100=(int)ucRxBuffer[8] * 256 + (int)ucRxBuffer[9];	               //CF=1下,PM10浓度计算
         pm_at_10=(int)ucRxBuffer[10] * 256 + (int)ucRxBuffer[11];                     //大气环境下PM1.0浓度计算
         pm_at_25=(int)ucRxBuffer[12] * 256 + (int)ucRxBuffer[13];		       //大气环境下PM2.5浓度计算
         pm_at_100=(int)ucRxBuffer[14] * 256 + (int)ucRxBuffer[15];		       //大气环境下PM10浓度计算
         particulate03=(int)ucRxBuffer[16] * 256 + (int)ucRxBuffer[17];		       //0.1L空气中 d>0.3um颗粒物个数 
         particulate05=(int)ucRxBuffer[18] * 256 + (int)ucRxBuffer[19];		       //0.1L空气中 d>0.5um颗粒物个数
         particulate10=(int)ucRxBuffer[20] * 256 + (int)ucRxBuffer[21];		       //0.1L空气中 d>1.0um颗粒物个数
         particulate25=(int)ucRxBuffer[22] * 256 + (int)ucRxBuffer[23];		       //0.1L空气中 d>2.5um颗粒物个数
         particulate50=(int)ucRxBuffer[24] * 256 + (int)ucRxBuffer[25];                //0.1L空气中 d>5.0um颗粒物个数
         particulate100=(int)ucRxBuffer[26] * 256 + (int)ucRxBuffer[27]; 	       //0.1L空气中 d>10.0um颗粒物个数
         //HCHO=((int)ucRxBuffer[28] * 256 +(int)ucRxBuffer[29])/1000.000;    
    if (pm_cf_25 >  999)//如果PM2.5数值>1000，返回重新计算
    {
      ucRxCnt = 0;
      return;
    }
    
    ucRxCnt = 0;
    return;
  }

}

void setup() {

   Serial.begin(9600);		//初始化硬串口 
   mySerial.begin(9600);    //初始化软串口 
}

void loop() {
	char a;
        int sum;
	if(Serial.available())
	{
		a = Serial.read();
		if(a == 'a')
		{
			while (mySerial.available())
                       {
                             getG5(mySerial.read());
                       }
                sum = pm_at_10 + pm_at_25 + pm_at_100;  
                Serial.print("|");
                Serial.print("aaa");
                Serial.print("|");
		Serial.print(pm_at_10);
		Serial.print("|");
		Serial.print(pm_at_25);
		Serial.print("|");
		Serial.print(pm_at_100);
		Serial.print("|");  
		Serial.print(sum);
		Serial.print("|");
		Serial.print("bbb");
                Serial.println("|");
		}		
	}
}
