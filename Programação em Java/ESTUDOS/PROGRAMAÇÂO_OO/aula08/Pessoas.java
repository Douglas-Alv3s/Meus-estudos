package PROGRAMAÇÂO_OO.aula08;

public class Pessoas {
    // Atributos
    private String nome;
    private int idade;
    private String sexo;


    public Pessoas(String nome, int idade, String sexo) {
        this.nome = nome;
        this.idade = verificarIdade(idade);
        this.sexo = verificarSexo(sexo);
    }

    public void fazerAniver(){
        if(this.idade > 0){
            if ((this.sexo.equals("masculino")) || (this.sexo.equals("feminino"))){
                this.idade++;
                System.out.println("Parabens pelos seus "+this.idade+" anos");
            }else{
                System.out.println("Sexo Invalido");
            }
        }else{
            System.out.println("Idade Invalida");
        } 
    }

    private int verificarIdade(int idade){
        if  (idade>0){
            return idade;
        }else{
            idade = -1;
            return idade;
        }
    }
    
    private String verificarSexo(String sexo){
        if ((sexo.equals("masculino")) || (sexo.equals("feminino"))){
            return sexo;
        }else{
            // System.out.println("Sexo Invalido");
            sexo = null;
            return sexo;
        }
    }

    public String mostrarNome(){
        return this.nome;
    }

    public void dadosPessoa(){
        System.out.println("Nome: "+this.nome);
        System.out.println("Idade: "+this.idade);
        System.out.println("Sexo: "+this.sexo);

    }

}