package PROGRAMAÇÂO_OO.aula07;

public class Lutador implements Config{
    
    // Atributos
    private String nome;
    private String nacionalidade;
    private int idade;
    private float altura;
    private float peso;
    private String categoria;
    private int vitorias;
    private int derrotas;
    private int empates;

    public Lutador(String nome, String nacionalidade, int idade, float altura, float peso,
            int vitorias, int derrotas, int empates) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.idade = idade;
        this.altura = altura;
        this.peso = peso;
        this.categoria = olharCategoria();
        this.vitorias = vitorias;
        this.derrotas = derrotas;
        this.empates = empates;
    }

    public void apresentar(){
        System.out.println("-------LUTADOR-------\n");
        System.out.println("Nome: "+this.nome);
        System.out.println("Nacionalidade: "+this.nacionalidade);
        System.out.println("Idade: "+this.idade);
        System.out.println("Altura: "+this.altura);
        System.out.println("Peso: "+this.peso);
        System.out.println("Categoria: "+this.categoria);
        System.out.println("Vitoria: "+this.vitorias);
        System.out.println("Derrotas: "+this.derrotas);
        System.out.println("empates: "+this.empates+"\n");
        // System.out.println("APRESENTAÇÃO CONCLUIDA...");
    }

    @Override
    public void status() {
        System.out.println("Nome: "+this.nome);
        System.out.println("Categoria: "+this.categoria);
        System.out.println("Vitoria: "+this.vitorias);
        System.out.println("Derrotas: "+this.derrotas);
        System.out.println("empates: "+this.empates+"\n");
    }

    @Override
    public void ganharLuta(){
        this.vitorias++;
    }

    @Override
    public void perderLuta(){
        this.derrotas++;
    }
    
    @Override
    public void empatarLuta(){
        this.empates++;
    }

    private String olharCategoria(){
        if (this.peso < 52.2){
            return categoria = "Invalido";
        }else if (this.peso <= 70.3){
            return categoria = "Leve";
        } else if (this.peso <=83.9){
            return categoria = "Médio";
        } else if (this.peso <=120.2){
            return categoria = "Pesado";
        } else{
            return "Invalido";
        }
    }

    public String mostrarCategoria(){
        return this.categoria;
    }
    
    public String mostrarNome(){
        return this.nome;
    }
}
