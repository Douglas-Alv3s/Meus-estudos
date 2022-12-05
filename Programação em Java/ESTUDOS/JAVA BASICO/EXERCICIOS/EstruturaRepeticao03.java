package EXERCICIOS;

import java.util.Arrays;
import java.util.Scanner;

public class EstruturaRepeticao03 {
    public static void main(String[] args){

        Scanner teclado = new Scanner(System.in);
        int lista[] = new int [7];
        Arrays.fill(lista, 0);
        String resp ="s";
        int opcao;
        int local, valor;
        // i = 0;
        

        while (resp.equals("s")){
            for(int i: lista){
                System.out.print(i+" ");
            }
            System.out.println("\n---Escolha a tarefa---\n[1] Adicionar\n[2] Remover\n[3] Ordenar");
            opcao = teclado.nextInt();
            if(opcao == 1){
                System.out.println("-=-=--=-=-=-=-=-=-");

                System.out.print("Posição: ");
                local = teclado.nextInt();
                System.out.print("Valor: ");
                valor = teclado.nextInt();
                lista[local] = valor;
                System.out.println("-=-=--=-=-=-=-=-=-");
            }else if(opcao == 2){
                System.out.print("Posição: ");
                local = teclado.nextInt();
                lista[local] = 0;
            }else if(opcao == 3){
                Arrays.sort(lista);
            }

            for(int i: lista){
                System.out.print(i+" ");
            }
            System.out.println("\n-=-=--=-=-=-=-=-=-\n  ");

            System.out.print("Deseja continuar?[s/n] ");
            resp = teclado.next();
        }
        teclado.close();

    }
    
}
