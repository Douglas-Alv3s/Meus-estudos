package PROGRAMAÇÂO_OO.aula07;

import java.util.Random;

public class Luta {
    // Atributos
    private Lutador desafiado;
    private Lutador desafiante;
    // private int rounds;
    private boolean aprovada;
    

    public void marcarLuta(Lutador l1, Lutador l2){
        if((l1.mostrarCategoria().equals(l2.mostrarCategoria()) && (l1 != l2))){
            this.aprovada = true;
            this.desafiado = l1;
            this.desafiante = l2;
        } else{
            this.aprovada = false;
            this.desafiado = null;
            this.desafiante = null;
        }

    }

    public void lutar(){
        if (this.aprovada){
            System.out.println("### A LUTA IRÁ COMEÇAR###\n");
            System.out.println("-------DESAFIADO-------");
            this.desafiado.apresentar();
            System.out.println("\n-------DESAFIANTE-------");
            this.desafiante.apresentar();
            Random aleatorio = new Random(); 
            int vencedor = aleatorio.nextInt(3);
            switch (vencedor){
                case 0:
                    System.out.println("Empatou");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                    break;
                case 1:
                    System.out.println("Vitória do "+ this.desafiado.mostrarNome());
                    this.desafiado.ganharLuta();
                    this.desafiante.perderLuta();
                    break;
                case 2:
                    System.out.println("Vitória do "+ this.desafiante.mostrarNome());
                    this.desafiado.perderLuta();
                    this.desafiante.ganharLuta();
                    break;
            }
        }else {
            System.out.println("Luta não pode acontecer");
        }
    }
}
