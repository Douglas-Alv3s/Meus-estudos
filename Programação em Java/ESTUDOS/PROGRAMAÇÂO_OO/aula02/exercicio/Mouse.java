package PROGRAMAÇÂO_OO.aula02.exercicio;

public class Mouse {
    String marca;
    String cor;
    boolean funcionando;

    void ligado() {
        if (this.funcionando == true) {
            System.out.println("\nMouse ligado");
        } else {
            System.out.println("\nMouse desligado");
        }
    }

    void clickEsquerdo(){
        if (this.funcionando == true){
            System.out.println("\nClicou com o botão esquerdo");

        }
    }

    void clickDireito(){
        if (this.funcionando == true){
            System.out.println("\nClicou com o botão direito");

        }
    }

    void desligar(){
        this.funcionando = false;
        System.out.println("\nMouse desligadoo");
    }

    void ligar(){
        this.funcionando = true;
        System.out.println("\nMouse ligado");
    }

    void status(){
        System.out.println("Marca: " + this.marca);
        System.out.println("Cor" + this.cor);
    }
}
