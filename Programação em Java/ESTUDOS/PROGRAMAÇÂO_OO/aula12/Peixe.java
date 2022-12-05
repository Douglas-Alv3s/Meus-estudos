package PROGRAMAÇÂO_OO.aula12;

public class Peixe extends Animal{
    // Atributos
    private String corEscama;

    public String getCorEscama() {
        return corEscama;
    }

    public void setCorEscama(String corEscama) {
        this.corEscama = corEscama;
    }

    public Peixe(float peso, int idade, int membros, String corEscama){
        this.peso = peso;
        this.idade = idade;
        this.membros = membros;
        this.corEscama = corEscama;
    }

    public void soltarBolhas(){
        System.out.println("Soltando Bolhas");
    }


    @Override
    public void locomover() {
        System.out.println("Nadando");        
    }


    @Override
    public void alimentar() {
        System.out.println("Comendo substancias");        
    }


    @Override
    public void emitirSom() {
        System.out.println("Peixe não emiti som");        
    }
    
}
