package PROGRAMAÇÂO_OO.aula08;

public class Livro implements Publicacao {
    // Atributos
    private String titulo;
    private String autor;
    private int totPaginas;
    private int pagAtual;
    private boolean aberto;
    private String leitor;

    public Livro(String titulo, String autor, int totPaginas, int pagAtual, Pessoas leitorr) {
        this.titulo = titulo;
        this.autor = autor;
        this.totPaginas = totPaginas;
        this.pagAtual = pagAtual;
        this.aberto = false;
        this.leitor = leitorr.mostrarNome();
    }

    // public void detalhes(){
    //     System.out.println("\n==== DETALHES ====");
    //     System.out.println("Titulo: "+this.titulo);
    //     System.out.println("Autor: "+this.autor);
    //     System.out.println("Total de Paginas: "+this.totPaginas);
    //     System.out.println("Pagina atual: "+this.pagAtual);
    //     System.out.println("Leitor: "+this.leitor);
    //     System.out.println("=====================\n");

        
    // }

    @Override
    public void abrir() {
        if (this.aberto == false){
            System.out.println("Livro aberto!");
            this.aberto = true;
            // return this.aberto;
        }else{
            System.out.println("ERRO: Já está aberto");
            this.aberto = true;
            // return this.aberto;
        }
    }

    @Override
    public void fechar() {
        if (this.aberto == true){
            System.out.println("Livro fechado!");
            this.aberto = false;
            // return this.aberto;
        }else{
            System.out.println("Erro: já esta fechado");
            this.aberto = false;
            // return this.aberto;
        }
    }

    @Override
    public void folhear(int pagina) {
        this.pagAtual = pagina;
    }

    @Override
    public void avançaPag() {
        if (this.aberto){
            if (this.pagAtual < this.totPaginas){
                this.pagAtual++;
                System.out.println("Pagina atual: "+this.pagAtual);
            }else{
                System.out.println("ERRO: Pagina Maxima alcançada");
            }
        }else{
            System.out.println("Impossivel");
        }
        
    }

    @Override
    public void voltarPag() {
        if (this.aberto){
            if (this.pagAtual < this.totPaginas){
                this.pagAtual--;
                System.out.println("Pagina atual: "+this.pagAtual);
            }else{
                System.out.println("ERRO: Pagina Maxima alcançada");
            }
        }else{
            System.out.println("Impossivel");
        }
        
    }

    public String detalhes() {
        return "Livro [titulo=" + titulo + ", autor=" + autor + 
                ", totPaginas=" + totPaginas + ", pagAtual=" + pagAtual
                + ", aberto=" + aberto + ", leitor=" + leitor + "]";
    }

}
