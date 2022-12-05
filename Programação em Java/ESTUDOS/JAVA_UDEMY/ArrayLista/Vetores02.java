package JAVA_UDEMY.ArrayLista;

import java.util.Scanner;

public class Vetores02 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Quantidade de produtos: ");
        int n = input.nextInt(); 

        Product[] vect = new Product[n];

        double soma = 0; 
        for (int i=0; i<vect.length; i++){
            System.out.print("Nome do produto ["+i+"]: ");
            String nomeprod = input.next();
            System.out.print("Preço do produto ["+i+"]: R$");
            double preçoprod = input.nextDouble();
            vect[i] = new Product(nomeprod, preçoprod);

            soma += vect[i].mostrarPreço();
        }

        double media = soma/n;
        System.out.println("A média de preço dos produtos é: R$"+media);



        input.close();
    }
    
}
