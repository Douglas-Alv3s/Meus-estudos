import java.util.Scanner;

public class OperadoresLogicos {
    
    public static void main(String[] args){

        try (Scanner teclado = new Scanner(System.in)) {
            System.out.print("Ano de nascimento: ");
            int ano = teclado.nextInt();
            int idade = 2022 - ano;
            String votar = ((idade >= 16 && idade < 18) || (idade > 70))? "É opicional":"Não é opcional";
            System.out.println(votar);
        }

    }
}
