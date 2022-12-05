package JAVA_UDEMY.ArrayLista;

import java.util.ArrayList;

public class ArrayLista02 {

    public static void main(String[] args) {
        
        ArrayList<String> client = new ArrayList<>(); 

        client.add("Douglas");
        client.add("Ana");
        client.add("Genival");

        //client.remove(1); // Remove através do indice
        //client.clear(); // Limpa todo o conteudo dentro da lista

        System.out.println(client.get(1)); //Mostra uma posição especifica

        System.out.println(client.isEmpty()); // Verifica se a lista está vazia

        System.out.println(client.contains("Genival")); // Verifica se o item está contido na lista

        System.out.println(client.size()); // Mostra o tamanho da lista
        
        System.out.println( client.toString());



    }
    
}
