package LivroLivrariaArraylist;

import java.util.ArrayList;

public class Acervo {

    private static ArrayList<LivroLivraria> listaLivros = new ArrayList<>();

    // Metodo get
    public static ArrayList<LivroLivraria> getListaLivros() {
        return listaLivros;
    }
    
    // Adicionar um objeto na lista
    static public void adcionar(LivroLivraria l){
        listaLivros.add(l);
    }

    // listas de dados de todos os objetos da lista
    static public String listar(){
        String saida = "";
        int i = 1;
        for(LivroLivraria l : listaLivros){
            saida += "\n======= Livro Nº " + (i++)+" =======\n";
            saida += l.imprimir() + "\n";
        }

        return saida;
    }
    

    // Pesquisar por genero
    static public int pesquisar (String genero){
        int qtd = 0;

        for (LivroLivraria l : listaLivros){
            if(l.getGenero().equalsIgnoreCase(genero)){
                qtd++;
            }
        }

        return qtd;
    }


    // Pesquisar pro faixa de preço
    static public int pesquisar(double vInicial, double vFinal){
        int qtd =0;
        
        for(LivroLivraria l: listaLivros){
            if(l.getPreco() >= vInicial && l.getPreco() <= vFinal){
                qtd++;
            }
        } 

        return qtd;
    }

    // Remove um livro pelo titulo
    static public boolean remove(String titulo){
        for(LivroLivraria l: listaLivros){
            if(l.getTitulo().equalsIgnoreCase(titulo)){
                listaLivros.remove(l);
                return true;
            }
        }
        return false;
    }

    // Total do acervo
    static double calcularTotalAcervo(){
        double total = 0;
        
        for(LivroLivraria l : listaLivros){
            total += l.getPreco();
        }
        return total;
    }

    static int mudarValor(int i){
        
        
        return i;
    }
}
