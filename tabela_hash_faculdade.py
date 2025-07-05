tabelaHash = [None] * 10;



class Nodo:
    def __init__(self, sigla, nomeEstado, proximo=None):
        self.sigla = sigla;
        self.nomeEstado = nomeEstado;
        self.proximo = proximo;


def hashFuncao (sigla):
    if sigla == "DF":
        return 7;
    sigla = list(sigla);
    return (ord(sigla[0]) + ord(sigla[1])) % 10;


def inserir (sigla, nomeEstado):
    indice = hashFuncao(sigla);
    novoNodo = Nodo(sigla, nomeEstado);
    novoNodo.proximo = tabelaHash[indice];
    tabelaHash[indice] = novoNodo;


def imprimirTabelaHash():
    for i in range(len(tabelaHash)):
        print(f"Posibão {i}: ", end="");
        atual = tabelaHash[i];
        while atual is not None:
            print(f"{atual.sigla} -> ", end="");
            atual = atual.proximo;
        print("None");

inserir("AC", "Acre");
inserir("AL", "Alagoas");
inserir("AP", "Amapá");
inserir("AM", "Amazonas");
inserir("BA", "Bahia");
inserir("CE", "Ceará");
inserir("ES", "Espírito Santo");
inserir("GO", "Goiás");
inserir("MA", "Maranhão");
inserir("MT", "Mato Grosso");
inserir("MS", "Mato Grosso Do Sul");
inserir("MG", "Minas Gerais");
inserir("PA", "Pará");
inserir("PB", "Paraíba");
inserir("PR", "Paraná");
inserir("PE", "Pernambuco");
inserir("PI", "Piauí");
inserir("RJ", "Rio De Janeiro");
inserir("RN", "Rio Grande Do Norte");
inserir("RS", "Rio Grande Do Sul");
inserir("RO", "Rondônia");
inserir("RR", "Roraima");
inserir("SC", "Santa Catarina");
inserir("SP", "São Paulo");
inserir("SE", "Sergipe");
inserir("TO", "Tocantins");
inserir("DF", "Distrito Federal");
inserir("MD", "Matheus Teixeira Diogenes");

imprimirTabelaHash()