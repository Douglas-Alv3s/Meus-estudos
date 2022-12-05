package PROGRAMAÇÂO_OO.aula02.exercicio;

public class Exerc02 {
    public static void main(String[] args) {
        Mouse mouse1 = new Mouse();
        mouse1.cor= "preto/vermelhor";
        mouse1.marca = "X FIRE";

        mouse1.status();

        mouse1.ligar();
        mouse1.clickDireito();
    }
    
}
