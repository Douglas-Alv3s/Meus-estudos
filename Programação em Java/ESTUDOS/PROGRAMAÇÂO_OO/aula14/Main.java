package PROGRAMAÇÂO_OO.aula14;

public class Main {
    
    public static void main(String[] args) {

        
        Video v[] = new Video[3];
        v[0] = new Video("NOiva cadaver");
        v[1] = new Video("Espiçoes");
        v[2] = new Video("dinossoura");

        Gafanhotos g[] = new Gafanhotos[2];
        g[0] = new Gafanhotos("Jubileu", 22, "M", "juba");
        g[1] = new Gafanhotos("Creuza", 12, "F", "creuzita");

        System.out.println("\n*****ASSISTIR******\n");
        Visualizacao vis[] = new Visualizacao[2];

        vis[0] = new Visualizacao(g[0], v[2]);
        vis[0].avaliar();
        vis[0].avaliar(10);
    
        System.out.println("VIDEOS\n--------------------------------------------------------");
        System.out.println(v[0].toString());
        System.out.println(v[1].toString());
        System.out.println(v[2].toString());
        System.out.println("\nGAFANHOTOS\n--------------------------------------------------------");
        System.out.println(g[0].toString());
        System.out.println(g[1].toString());

        
    }
}
