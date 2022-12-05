package JAVA_UDEMY.ArrayLista;

import java.util.Scanner;

public class Vetores01 {
    
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.print("Tamanho do vetor: ");
        int n = input.nextInt();
        double[] vect = new double[n]; 
        double soma = 0;
        double valor;

        for (int i=0; i<n; i++){
            System.out.print("Valor: ");
            valor = input.nextDouble();
            vect[i] = valor;
            soma += vect[i]; 
        }

        double media = soma/n;

        System.out.println("Média: "+media);

        input.close();
    }
}

