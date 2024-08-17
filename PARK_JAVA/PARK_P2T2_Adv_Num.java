import java.util.Scanner;
//Kevin Alejandro Parra Ramos  Ing.software  3er cuatrimestre 
public class PARK_P2T2_Adv_Num {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int ale = (int) (Math.random() * 5);
        System.out.println("+++++++++++++++++++++++++++++++++\n");
        System.out.println("    ADIVINA EL NUMERO OCULTO\n");
        System.out.println("+++++++++++++++++++++++++++++++++\n");
        System.out.println("Ingresa un numero del 0 al 5 :)");
        int num = scanner.nextInt();
        while (num != ale) {
            System.out.println("fallaste intenta de nuevo:\t");
            num = scanner.nextInt();
        }
        System.out.println(" ''has adivinado el numero oculto'':"+ ale);
}
}