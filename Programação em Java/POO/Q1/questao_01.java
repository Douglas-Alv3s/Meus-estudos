package Q1;

import java.util.Locale;
import java.util.Scanner;

/*Faça um programa para ler a cotação do dólar, e depois leia 
o valor em dólares a ser comprado. A saída será quantos reais a
 pessoa pagará pelos dólares, considerando ainda que a pessoa 
 pagará 6% de IOF sobre o valor em dólar. Criar uma classe 
 CurrencyConverter (Conversor de moeda) para ser responsável pelos cálculos.*/

public class questao_01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("What is the dollar price? ");
        double dollarPrice = sc.nextDouble();
        System.out.print("How many dollars will be bought? ");
        double amount = sc.nextDouble();
        
        double result = CurrencyConverter.dollarToReal(amount, dollarPrice);
        System.out.printf("Amount to be paid in reais = %.2f%n", result);
        sc.close();
 }
}

