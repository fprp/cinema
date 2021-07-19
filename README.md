# Projeto de Python
Esse projeto foi feito por Filipe Paz para a disciplina de programação utiliazando python em 2018. Consiste em uma simulação de um cinema exibido no terminal. Para rodar, basta baixar e executar o arquivo main.py no diretório. Tudo o que é feito é salvo em ./public/log.txt.

## Comandos
Esses comandos são encontrados no programa em execução e listam suas funcionalidades. 

### Login
Faz o login de algum usuário listado no arquivo ./src/login/usuarios.txt.

### Cadastror Novo Usuario
Cadastro um novo usuário no arquivo ./src/login/usuarios.txt.

### Sair
Encerra o programa.

### Cadastrar sessão
Cadastra uma nova sessão no arquivo ./src/cartaz/elementos.txt quando o usuário logado possui nível de acesso de administrador.

### Atualizar sessão
Atualiza uma sessão do arquivo ./src/cartaz/elementos.txt quando o usuário logado possui nível de acesso de administrador.

### Ver sessão
Exibe na tela as sessões existentes do arquivo ./src/cartaz/elementos.txt.

### Buscar sessão
Exibe na tela sessões disponíveis por nome ou data do filme do arquivo ./src/cartaz/elementos.txt.

### Remover sessão
Remove uma sessão do arquivo ./src/cartaz/elementos.txt quando o usuário logado possui nível de acesso de administrador.

### Ordenar sessão
Ordena pelo nome do filme em ordem alfabética os filmes do arquivo ./src/cartaz/elementos.txt.

### Download das sessões em planilha
Cria uma planilha (.csv) dos filmes em cartaz e salva em ./public/sessoes.csv.

### Gerar Relatório
Cria um arquivo (.txt) dos filmes em cartaz e salva em ./public/relatorio.txt.

### Mudar Nível de Acesso de Algum Usuário
Muda o nível de acesso de um usuário, tanto para conceder mais permissão (administrador) quanto para retirar permissão (cliente), quando o usuário logado possui nível de acesso de administrador.

### Logout
Faz o logout do usuário e volta para a tela de login.