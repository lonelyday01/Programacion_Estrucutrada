import java.util.*;

public class PARK_P3_EXAMEN{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int numero = 0;
        System.out.println("*************************************");
        System.out.println("       DE ENTEROS A ROMANOS");
        System.out.println("*************************************");
        System.out.println("INGRESA UN NUMERO QUE NO EXCEDA 1001: ");
        numero = scanner.nextInt();

        if(numero > 1001){
            System.out.println("ecxedes la limitante intenta otro numero: ");
            numero = scanner.nextInt();
        }

        String respuesta = enteroRomano(numero);        

        System.out.println("Tu numero es: " + numero + " a Romano es:" +respuesta);

        scanner.close();
    }

    public static String enteroRomano(int numero){
        int resta = numero;
        String resultado = "";

        SortedMap<Integer, String> roman = new TreeMap<>(Collections.reverseOrder());
        roman.put(1000, "M");
        roman.put(900, "CM");
        roman.put(500, "D");
        roman.put(400, "CD");
        roman.put(100, "C");
        roman.put(90, "XC");
        roman.put(50, "L");
        roman.put(40, "XL");
        roman.put(10, "X");
        roman.put(9, "IX");
        roman.put(5, "V");
        roman.put(4, "IV");
        roman.put(1, "I");
       
        Set<Map.Entry<Integer, String>> s = roman.entrySet();
        
        Iterator<Map.Entry<Integer, String>> i = s.iterator();
        
        while(i.hasNext()){
           
            Map.Entry<Integer, String> entrada = i.next();
           
            while(resta >= entrada.getKey()){
                resultado = resultado + entrada.getValue();
                resta = resta - entrada.getKey();
            }
        }

        return resultado;
    }
}