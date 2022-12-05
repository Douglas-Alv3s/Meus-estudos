package PROGRAMAÇÂO_OO.aula12;

public class Ave extends Animal{
    private String corPena;

    
    public void setCorPena(String corPena) {
        this.corPena = corPena;
    }


    public String getCorPena() {
        return corPena;
    }


    public Ave(float peso, int idade, int membros, String corPena) {
        this.peso = peso;
        this.idade = idade;
        this.membros = membros;
        this.corPena = corPena;
    }


    public void fazerNinho(){
        System.out.println("Construiu um Ninho");
    }


    @Override
    public void locomover() {
        System.out.println("Voando");
        
    }


    @Override
    public void alimentar() {
        System.out.println("Comendo frutas");
        
    }


    @Override
    public void emitirSom() {
        System.out.println("Som de Ave");
        
    }


}
