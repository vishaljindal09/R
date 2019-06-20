#property indicator_chart_window 
#property indicator_buffers 2 
#property indicator_color1 OrangeRed 
#property indicator_color2 Aqua

//---- buffers
double      MSH[]; 
double      MSL[];  

//----------------------------------------------------------------+
int init()
{
   IndicatorShortName ("MSH_MSL");
   SetIndexBuffer (0,MSH);
   SetIndexStyle (0,DRAW_ARROW);
   SetIndexArrow (0,242);
   SetIndexBuffer (1,MSL);
   SetIndexStyle (1,DRAW_ARROW);
   SetIndexArrow (1,241);
   return (0);
}

int start()
{
   /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
   int   limit;
   int   counted_bars = IndicatorCounted ();
   /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

   if (counted_bars < 0) return (-1);

   if (counted_bars > 0) counted_bars -= 10;
   limit = Bars - counted_bars;

   for (int i = 0; i < limit; i++)
   {
      //==============================================
      MSH[i]=EMPTY_VALUE;
      int barH1 = iHighest(NULL, 0, MODE_CLOSE, 500, i+4);
      int barH2 = iHighest(NULL, 0, MODE_CLOSE, 500, i+3);
      if (barH1==i+4 && barH2 == i+3 && Open[i+2] > Close[i+2] && Close[i+1] < Close[i+2] ) MSH[i] = High[i]+ 5*Point;
      //==============================================      
      MSL[i]=EMPTY_VALUE;
      int barL1 = iLowest(NULL, 0, MODE_CLOSE, 500, i+4);
      int barL2 = iLowest(NULL, 0, MODE_CLOSE, 500, i+3);
      if (barL1==i+4 && barL2 == i+3 && Open[i+2] < Close[i+2] && Close[i+1] > Close[i+2] ) MSL[i] = Close[i]- 5*Point;  
      
   }

   return (0);
}

//+------------------------------------------------------------------+