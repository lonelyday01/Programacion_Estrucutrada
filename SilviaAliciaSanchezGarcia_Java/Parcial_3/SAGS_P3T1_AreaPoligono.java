import java.util.Scanner;

public class SAGS_P3T1_AreaPoligono{
    
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String[] tareas = {" ", " ", " ", " ", " "};
        String tarea = "";
        int choice = -1;


        while (choice != 0) {
            System.out.println("Elige la accion que deseas realizar: \n");
            System.out.println("1: Agregar una tarea \n2: Listar las tareas");
            System.out.println("3: Completar tarea \n4: Eliminar tarea");
            System.out.println("0: Salir del programa \n");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.println("Ingresa tu tarea:");
                    tarea = scanner.nextLine();

                    boolean espacio = false;
                    for(int i = 0; i < tareas.length; i++){
                        if(tareas[i].equals(" ")){
                            tareas[i] = tarea;
                            espacio = true;
                            break;
                        }
                    }
                    if(!espacio){
                        System.out.println("Son demasiadas tareas!!");
                    }
                    break;

                case 2:
                    System.out.println("Tus tareas de hoy son las siguientes: ");
                    for(int i = 0; i < tareas.length; i++){
                        System.out.println(i+1 + "- " + tareas[i]);
                    }
                    break;

                case 3:
                    System.out.println("Ingresa la tarea que has completado: ");
                    tarea = scanner.nextLine();

                    boolean busqueda = false;
                    for(int i = 0; i < tareas.length; i++){
                        if(tareas[i].equals(tarea)){
                            tareas[i] = tareas[i] + " Completada!";
                            busqueda = true;
                        }
                    }
                    if(!busqueda){
                        System.out.println("No se ha encontrado esa tarea.");
                    }
                    break;

                case 4:
                    System.out.println("Ingresa la tarea que deseas eliminar: ");
                    tarea = scanner.nextLine();

                    for(int i = 0; i < tareas.length; i++){
                        if(tareas[i].equals(tarea)){
                            tareas[i] = " ";
                            break;
                        }
                    }

                    for(int j = 0; j < tareas.length - 1; j++){
                        if(tareas[j].equals(" ")){
                            tareas[j] = tareas[j+1];
                            tareas[j+1] = " ";
                        }
                    }
                    break;
                case 0:
                    System.out.println("Bye!!");
                    break;

                default:
                    System.out.println("Que elijas un numero entre 0 y 4 BURRO!!!");
                    break;
            }
        }
        scanner.close();
    }
}
