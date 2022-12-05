package EXERCICIOS;

import java.util.Scanner;

// Exercicio basico sobre estrutura de decisão, fazendo relação aos votos.

public class EstruturaDecisao {
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        System.out.print("Ano de Nascimento: ");
        int ano = teclado.nextInt();
        int idade = 2022 - ano;
        System.out.println("Idade de: " + idade);
        
        if (idade < 16) {
            System.out.println("Não pode votar");
        }
        else if ((idade >= 16 && idade < 18) || idade > 70) {
            System.out.println("Voto facutativo");
        }
        else {
            System.out.println("Voto Obrigatorio.");
        }

        teclado.close();
    }
    
}
