package JAVA_UDEMY.ArrayLista;

public class Product {

    private String nome;
    public String getNome() {
        return nome;
    }

    private double preço;
    
    public Product(String nome, double preço) {
        this.nome = nome;
        this.preço = preço;
    }
    
    public double mostrarPreço(){
        return preço;
    }
    
}
