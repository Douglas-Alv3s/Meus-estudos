package EXERCICIOS;

import java.util.Scanner;

public class EstruturaDecisao02 {
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Quantia de pernas: ");
        int pernas = teclado.nextInt();
        String tipo;
        
        System.out.print("Isso é um(a): ");

        switch(pernas){
            case 1:
                tipo = "Saci";
                break;
            case 2:
                tipo = "Bipede";
                break;
            case 4:
                tipo = "Quadrupede";
                break;
            case 6, 8:
                tipo = "Aranha";
                break;
            default:
                tipo = "ET";
        }
        System.out.println(tipo);
        teclado.close();
    }

    
}
