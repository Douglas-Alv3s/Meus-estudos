package PROGRAMAÇÂO_OO.aula14;

public class Gafanhotos extends Pessoa{
    // Atributos
    private String login;
    private int totAssistindo;

    public Gafanhotos(String nome, int idade, String sexo, String login) {
        super(nome, idade, sexo);
        this.login = login;
        this.totAssistindo = 00;
    }

    public void viuMaisUm(){
        totAssistindo++;
        System.out.println("Mais um video assistido");
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public int getTotAssistindo() {
        return totAssistindo;
    }

    public void setTotAssistindo(int totAssistindo) {
        this.totAssistindo = totAssistindo;
    }

    @Override
    public String toString() {
        return "Gafanhotos ["+super.toString()+"\nlogin=" + login + ", totAssistindo=" + totAssistindo + "]";
    }

    
    
    
}
