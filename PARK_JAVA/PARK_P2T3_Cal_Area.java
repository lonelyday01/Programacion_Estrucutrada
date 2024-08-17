//Kevin Alejandro Parra Ramos  Ing.software  3er cuatrimestre 
import java.util.Scanner;
public class PARK_P2T3_Cal_Area 
{
    public static void main(String[] args)
    {
       Scanner scanner = new Scanner(System.in);
       System.out.println("+++++++++++++++++++++++++++++++++++++++");
       System.out.println("    Calcula el area de un poligono");
       System.out.println("+++++++++++++++++++++++++++++++++++++++");  
       System.out.println("ingresa el numero de loados de la figura:");
       double nlados = scanner.nextInt();
       System.err.println("ingresa la longitud de cada lado:");
       double longitud = scanner.nextInt();
       System.out.println("+++++++++++++++++++++++++++++++++++++++");
       System.out.println("el area de la figura es:  "+CalcArea(longitud,nlados));
    }
    public static double CalcArea(double longitud,double nlados)
    {
        double area = ((nlados * longitud) * 4.1 / 2 );
        return area;
    }
}
