package PROGRAMAÇÂO_OO.aula12;

public class Mamifero extends Animal{
    // Atributos
    private String corPelo;

    public String getCorPelo() {
        return corPelo;
    }

    public void setCorPelo(String corPelo) {
        this.corPelo = corPelo;
    }

    public Mamifero(float peso, int idade, int membros, String corPelo) {
        this.peso = peso;
        this.idade = idade;
        this.membros = membros;
        this.corPelo = corPelo;
    }

    @Override
    public void locomover() {
        System.out.println("Andando");
        
    }

    @Override
    public void alimentar() {
        System.out.println("Mamando");
        
    }

    @Override
    public void emitirSom() {
        System.out.println("Som de Mamifero");
        
    }

}
