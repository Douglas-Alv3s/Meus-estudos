package LivroLivrariaArraylist;

public class LivroLivraria {
    // Atributos
    private String titulo;
    private String autor;
    private int isbn;
    private String genero;
    private float preco;

    // Construtor Defalt
    public LivroLivraria(){ }
    
    // Sobrecarregando Construtor
    public LivroLivraria(String titulo, String autor, int isbn, String genero, float preco) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.genero = genero;
        this.preco = preco;
    }


    // Métodos de acesso
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getIsbn() {
        return isbn;
    }

    public void setIsbn(int isbn) {
        this.isbn = isbn;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public float getPreco() {
        return preco;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }

    // Método de impressão
    public String imprimir(){
        return "Título: "+ this.titulo+"\nAutor: "+this.autor+
                "\nISBN: "+this.isbn+"\nGênero: "+this.genero+
                String.format("\nPreço: R$%.2f \n", this.preco);
    }


}
