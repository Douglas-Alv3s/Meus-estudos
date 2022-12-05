package LivroLivrariaArraylist;

import java.util.Scanner;

public class ViewLivro {

    static public void viewsLivro(){
        Scanner entrada = new Scanner(System.in);
        Scanner entradaString = new Scanner(System.in);

        int menu;
        double vInicial, vFinal;
        //Referencia para a classe LivroLivraria
        LivroLivraria objLivro;

        String titulo, autor, genero;
        float preco;
        int isbn;

        do{
            exibirMenu();
            menu = entrada.nextInt();

            switch(menu){
                case 1: // Cadastrar livro
                    System.out.println("====> Cadastar Livro");
                    System.out.print("Digite o título: ");
                    titulo = entradaString.nextLine();
                    System.out.print("Digite o autor: ");
                    autor = entradaString.nextLine();
                    System.out.print("Digite o genero: ");
                    genero = entradaString.nextLine();
                    System.out.print("Digite o ISBN: ");
                    isbn = entrada.nextInt();
                    System.out.print("Digite o preço: ");
                    preco = entrada.nextFloat();

                    // Criar um objeto na classe
                    objLivro = new LivroLivraria(titulo, autor, isbn, genero, preco);

                    // Guardar no ArrayList
                    Acervo.adcionar(objLivro);
                    break;

                case 2: // 
                    System.out.println("====>Listagem de Livros");
                    System.out.println(Acervo.listar());
                    break;
                case 3:
                    System.out.println("====> Exclusão do Livro");
                    System.out.print("Digite o título do livro: ");
                    titulo = entradaString.nextLine();
                    if(!(Acervo.getListaLivros().isEmpty())){   // Acervo não vazio
                        if(Acervo.remove(titulo)){
                            System.out.println("Livro removido com sucesoo!!");
                        }else{
                            System.out.println("Não existem livros no acervo!!");
                        }
                    }else{
                        System.out.println("Não existe livros no acervo!!");
                    }

                    break;
                case 4:
                    System.out.println("====> Pesquisar pelo genero");
                    System.out.print("Digite o genero: ");
                    genero = entradaString.nextLine();
                    System.out.println("Existem "+Acervo.pesquisar(genero)
                                       + " livro(s) do genero " + genero);
                    break;
                case 5:
                    System.out.println("====> Pesquisar por faixa de preço");
                    System.out.print("Digite a faixa de preço inicial e a final: ");
                    vInicial = entrada.nextDouble();
                    System.out.print(" ");
                    vFinal = entrada.nextDouble();
                    System.out.println("Existem "+Acervo.pesquisar(vInicial, vFinal)
                                    + " livro(s) com preço entre " 
                                    + String.format("R$ %.2f e R$ %.2f \n", vInicial, vFinal));
                    break;
                case 6:
                    System.out.println("====> Total em R$ de livros em Acervo ");
                    System.out.println("O total é " + String.format("R$ %.2f \n", Acervo.calcularTotalAcervo()));
                    break;
                case 7:
                    System.out.println("Encerrando aplicação");
                    break;
                case 8:
                    System.out.println("===> Modificar nome: ");
                        Acervo.getListaLivros().get(0).setAutor("sfda");;

                    break;
                default:
                    System.out.println("Opção no menu Invalida");
                }
        }while(menu != 7);

        entrada.close();
        entradaString.close();

    }

    static private void exibirMenu(){
        System.out.println("=========== LIVRO LIVRARIA ==============");
        System.out.println("1 - CADASTRAR");
        System.out.println("2 - LISTAR");
        System.out.println("3 - EXCLUIR LIVRO");
        System.out.println("4 - PESQUISAR POR GENERO");
        System.out.println("5 - PESQUISAR POR FAIXA DE PREÇO");
        System.out.println("6 - CALCULAR TOTAL ACERVO");
        System.out.println("7 - SAIR\n");
        System.out.print("====> Escolha uma opção: ");
    }
    
}
