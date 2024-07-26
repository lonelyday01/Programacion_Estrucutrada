import java.util.Scanner;

public class SAGS_P2T2_AdivinarNumero {
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int secret_number = 7;
        int user_number = 0;

        System.out.println("Ingrese un numero del 1 al diez");
        user_number = scanner.nextInt();

        while(user_number != secret_number){
            System.out.println("Ese no es el numero secreto! Intentalo de nuevo :(");
            user_number = scanner.nextInt();
        }

        System.out.println("Felicidades!! Has encontrado el numero secreto!!");

        scanner.close();
    }
}
