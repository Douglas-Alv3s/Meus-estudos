package PROGRAMAÇÂO_OO.aula12;

public class Main {
    public static void main(String[] args) {
        Mamifero mamifero = new Mamifero(30f, 5, 4, "Preto");
        Reptil reptil = new Reptil(1f, 1,4,"verde");
        Peixe peixe = new Peixe(0.5f, 2, 0, "dourada");
        Ave ave = new Ave(3, 5, 4, "Azul/Amarelo");

        mamifero.alimentar();
        peixe.alimentar();
        ave.emitirSom();
        reptil.emitirSom();


    }
    
}
