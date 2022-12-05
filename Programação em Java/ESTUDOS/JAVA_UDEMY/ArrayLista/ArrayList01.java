package JAVA_UDEMY.ArrayLista;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


public class ArrayList01 {

    public static void main(String[] args) {
        
        ArrayList<String> list = new ArrayList<>();

        list.add("Douglas");
        list.add("Ana");
        list.add("Genival");
        list.add("Daniel");
        list.add("Andre");

        list.add(1, "Antonio");


        System.out.println(list.size());
        for (String x : list){
            System.out.println(x);
       } 

       System.out.println("-----------------------------");
       
       list.removeIf(x -> x.charAt(0) == 'D'); // Remove todos as Strings que começam com D

        for (String x : list){
            System.out.println(x);
       } 
       
       System.out.println("-----------------------------");
       // Mostrar a posição do item
       System.out.println("Posição de Ana: "+list.indexOf("Ana"));
       System.out.println("Posição de Douglas"+list.indexOf("Douglas"));// Quando não existe na lista retorna -1
       System.out.println("-----------------------------");

       // Filtrando elementos de uma lista e gerando uma nova só com esses elementos
       List<String> result = list.stream().filter(x -> x.charAt(0) == 'A').collect(Collectors.toList());

        for (String x : result){
            System.out.println(x);
       } 
       System.out.println("-----------------------------");

       // Encontrar o primeiro elemento com base no predicado

       String name = list.stream().filter(x -> x.charAt(0)=='A').findFirst().orElse(null);
       System.out.println(name);


    }
    
}
