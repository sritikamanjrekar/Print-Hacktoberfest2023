import java.util.*;
class Calculate
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter 1 for pattern");
  System.out.println("Enter 2 for pattern");
  System.out.println("Enter your choice");                     
  int ch=sc.nextInt();                                                          
  switch(ch)                                                                              
  {                                                                                              
   case 1: int i,j;                                                                           
               for(i=1;i<=9;i=i+2)
               {
                 for(j=i;j<=9;j=j+2)
                 {
                   System.out.print('j');
                 }
                System.out.println();
                }
                break;
    case 2: 
                 for(i=65;i<=69;i++)
                 {
                   for(j=69;j>=i;j--)
                   {
                     System.out.print(char('j')) ;
                   }
                  System.out.println();
                 }
                  break;
    }                                                                                   
  }                                                                                      
}                                                                                      
                                                                                          
                                                                                                                                 