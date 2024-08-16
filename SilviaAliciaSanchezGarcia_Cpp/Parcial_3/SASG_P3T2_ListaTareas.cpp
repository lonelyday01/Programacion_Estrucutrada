#include <iostream>
using namespace std;

int main()
{
    string tareas[5] = {" ", " ", " ", " ", " "};
    string tarea = "";
    int arraySize = sizeof(tareas)/sizeof(tareas[0]);
    int choice = -1;
    string completed = "";
    string deleteTask = "";


    while(choice != 0)
    {
        cout << "Elige la accion que deseas realizar: " << endl;
        cout << "1- Agregar una tarea" << endl << "2- Listar las tareas" << endl;
        cout << "3- Completar tarea" << endl << "4- Eliminar tarea" << endl << "0- Salir" << endl;
        cin >> choice;
        cin.ignore();

        switch(choice)
        {
        case 1:
        {
            /*agregar tarea*/
            cout << "Ingresa tu tarea: " << endl;
            getline(cin, tarea);

            bool espacio = false;
            for(int i = 0; i < arraySize; i++){
                if(tareas[i] == " "){
                    tareas[i] = tarea;
                    espacio = true;
                    break;
                }
            }
            if(!espacio){
                cout << "Son demasiadas tareas!!!" << endl;
            }
            break;
        }
        case 2:
        {
            /*listar tareas*/
            cout << "Tus tareas de hoy son las siguientes: " << endl;
            for(int i = 0; i < arraySize; i++){
                cout << i+1 << "- " << tareas[i] << endl;
            }
            break;
        }
        case 3:
        {
            /*completar tarea*/
            cout << "Ingresa la tarea que haz completado: " << endl;
            getline(cin, completed);

            bool busqueda = false;
            for(int i = 0; i < arraySize; i++){
                if(tareas[i] == completed){
                    tareas[i] = tareas[i] + " Completada!";
                    busqueda = true;
                }
            }

            if(!busqueda){
                cout << "Esa tarea no existe!!!" << endl;
            }
            break;
        }
        case 4:
        {
            /*eliminar tarea*/
            cout << "Ingresa la tarea que quieres eliminar: " << endl;
            getline(cin, deleteTask);

            for(int i = 0; i < arraySize; i ++){
                if(tareas[i] == deleteTask){
                    tareas[i] = " ";
                    break;
                }
            }

            for (int j = 0; j < arraySize - 1; j++){
                    if(tareas[j] == " "){
                    tareas[j] = tareas[j+1];
                    tareas[j+1] = " ";
                }
            }
            break;
        }
        case 0:
        {
            cout << "Bye!!!" << endl;
            break;
        }
        default:
        {
            cout<< "Que elijas un numero entre 0 y 4 BURRO!!!" << endl;
            break;
        }
        }
    }

}
