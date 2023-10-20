class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)

    def listar_livros(self):
        return self.livros


def test_adicionar_e_listar_livros():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    biblio.adicionar_livro("Livro C")
    assert biblio.listar_livros() == ["Livro A", "Livro B", "Livro C"]

def test_remover_livro():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    biblio.adicionar_livro("Livro C")
    
    biblio.remover_livro("Livro B")
    assert biblio.listar_livros() == ["Livro A", "Livro C"]
    
    biblio.remover_livro("Livro D")  # Testando a remoção de um livro que não existe na biblioteca
    assert biblio.listar_livros() == ["Livro A", "Livro C"]

def test_biblioteca_vazia():
    biblio = Biblioteca()
    assert biblio.listar_livros() == []

def test_adicionar_livros_duplicados():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    assert biblio.listar_livros() == ["Livro A", "Livro A", "Livro B"]

def test_listar_livros_sem_modificar():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    livros = biblio.listar_livros()  # Faz uma cópia da lista
    biblio.adicionar_livro("Livro C")
    assert livros == ["Livro A", "Livro B", "Livro C"]  # A lista original não foi modificada
