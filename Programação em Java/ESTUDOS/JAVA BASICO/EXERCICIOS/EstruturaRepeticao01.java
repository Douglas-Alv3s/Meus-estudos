package EXERCICIOS;

import java.util.Scanner;

public class EstruturaRepeticao01 {
    public static void main(String[] args) {
        int n, s=0;
        String resp;

        Scanner teclado = new Scanner(System.in);
        do{
            System.out.print("Digite um valor: ");
            n = teclado.nextInt();
            s += n;

            System.out.print("Deseja continuar[S/N]? ");
            resp = teclado.next();

        }while(resp.equals("s"));
        System.out.println("A soma total dos valores enviados é: "+ s);

        teclado.close();
    }
    
}
