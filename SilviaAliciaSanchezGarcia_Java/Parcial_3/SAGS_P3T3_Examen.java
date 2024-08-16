import java.util.*;

public class SAGS_P3T3_Examen{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int numero = 0;
        
        System.out.println("Ingresa un numero menor a 1001");
        numero = scanner.nextInt();

        /*Evaluacion de que el numero sea menor a 1001 */
        if(numero > 1001){
            System.out.println("El numero es muy grande!! Ingresa un numero MENOR a 1001");
            numero = scanner.nextInt();
        }

        /*Se llama a la funcion que realiza la conversion y se guarda el resultado en una variable */
        String respuesta = enteroRomano(numero);        

        System.out.println("El equivalente al numero " + numero + " en numero romano es: " +respuesta);

        scanner.close();
    }

    public static String enteroRomano(int numero){
        int resta = numero;
        String resultado = "";

        /*Se crea el diccionario, en este caso utilice un SortedMap*/
        SortedMap<Integer, String> roman = new TreeMap<>(Collections.reverseOrder());
        /*Se rellena el diccionario con los valores necesarios */
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
        /*Genera el conjunto que se utilizara para iterar */
        Set<Map.Entry<Integer, String>> s = roman.entrySet();
        /*Se crea el iterador*/
        Iterator<Map.Entry<Integer, String>> i = s.iterator();
        /*Se itera cada elemento del conjunto */
        while(i.hasNext()){
            /*Se almacena el elemento del diccionario para poder acceder a la clave y al valor por separado */
            Map.Entry<Integer, String> entrada = i.next();
            /*Mientras la resta sea igual o mayor a la clave del elemento se agregara el 
              valor correspondiente a la variable de respuesta y se restara la clave a la resta */
            while(resta >= entrada.getKey()){
                resultado = resultado + entrada.getValue();
                resta = resta - entrada.getKey();
            }
        }

        return resultado;
    }
}