/**
 * Este � o meu primeiro programa em java
 * 1) Que um programa Java � contruido dendo de um projeto Java.
 * 2) Todo programa Java deve ter uma classe com um m�todo main.
 * 3) Como exibir informa��es no terminal (console) do Java.
 * 4) Como Ler uma string do terminal (Console) do Java
 */
package meuPrimeiroProgramaJava;
import java.util.Scanner;

/**
 * @author mathe
 *Data: 03/02/2021
 */
public class Principal { // Classe que contem o metodo principal.
	public static void main(String[] args) {
		System.out.println("Ol� amigo!\nQual � o seu nome?"); // Uso do println
		// TODO Auto-generated method stub

		// Ler uma string do console usando a biblioteca Scanner.
		Scanner X = new Scanner(System.in);
		String nome = X.nextLine();
		
		// Exibir uma string usando printf
		System.out.printf("Ol� %s!\n", nome);
		X.close();
		
	}

}

