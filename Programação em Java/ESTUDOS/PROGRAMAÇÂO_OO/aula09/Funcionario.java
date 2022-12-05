package PROGRAMAÇÂO_OO.aula09;

public class Funcionario extends Pessoa {
    private String setor;
    private boolean trabalhando;
    
    
    public Funcionario(String setor) {
        this.setor = setor;
        this.trabalhando = true;
    }

    public void mudarTrabalho(String trab){
        this.setor = trab;
        System.out.println("Setor alterado para "+this.setor);

    }
    
    
    public void dadosFuncionario(){
        System.out.println("Nome: "+mostarNome());
        System.out.println("Idade: "+mostarIdade());
        System.out.println("Sexo: "+mostarSexo());
        System.out.println("Setor: "+this.setor);
        System.out.println("Trabalhando: "+this.trabalhando);

    }
    

}
