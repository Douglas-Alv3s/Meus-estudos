package PROGRAMAÇÂO_OO.aula14;

public class Visualizacao {
    //Atributos
    private Gafanhotos espectador;
    private Video filme;
    
    public Visualizacao(Gafanhotos espectador, Video filme) {
        this.espectador = espectador;
        this.filme = filme;
        this.espectador.setTotAssistindo(this.espectador.getTotAssistindo() + 1);
        this.filme.setViews(this.filme.getViews() + 1);

    }

    public Gafanhotos getEspectador() {
        return espectador;
    }
    public void setEspectador(Gafanhotos espectador) {
        this.espectador = espectador;
    }
    public Video getFilme() {
        return filme;
    }
    public void setFilme(Video filme) {
        this.filme = filme;
    }
    
    public void avaliar(){
        System.out.println("Avaliando filme "+ this.filme.getTitulo());
    
    }

    public void avaliar(int valiar){
        this.filme.setAvaliacao(valiar);
        System.out.println("\nAvaliação: "+ this.filme.getAvaliacao());
    }

    public void avaliar(double valiar){
        this.filme.setAvaliacao(valiar);
        System.out.println("\nAvaliação: "+ this.filme.getAvaliacao());
    }

    @Override
    public String toString() {
        return "Visualizacao [espectador=" + espectador + ", filme=" + filme + "]";
    }  

    
}
