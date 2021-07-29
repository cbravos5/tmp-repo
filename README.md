## Dependencias
### Python3.9

```bash
sudo apt update

sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install python3.9
```
Checar versão
```bash
python3.9 --version
```
Atualizar $PATH se necessário

### PIP

```bash
# Baixa os arquivos no diretorio atual
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 

python3.9 get-pip.py
```

Caso encontre algum erro basta acessar:

https://stackoverflow.com/questions/65644782/how-to-install-pip-for-python-3-9-on-ubuntu-20-04

### Docker
```bash
sudo apt-get update

sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Se tudo deu certo entao o comando abaixo vai baixar um container de teste, que só printa um hello world no terminal

```bash
sudo docker run hello-world
```

### SQLAlchemy

```bash
pip install SQLAlchemy
```

Pode ser que não tenha uma das dependencias do SQLAlchemy, então é melhor rodar:

```bash
pip install psycopg2-binary
```

## Repositório

Com o repositório clonado pode-se rodar os seguintes comandos:

```bash
# Cria um container postgresql na porta 5433
make create-repo
```
Sempre que ligar o computador e acessar este repositório tem que subir o container

```bash
make start-repo
```

Ao rodar <code>make create-tables</code> as tabelas devem ser criadas e uma mensagem *'Tables created successfully'* deve aparecer no terminal. Caso isso não ocorra deve-se rodar os seguintes comandos para gerar as tabelas:

```bash
export ENV='commit'
python3.9 ./src/repo
export ENV='desenv'
```
O comando acima seta uma variável de ambiente, que indica se as tabelas devem ser commitadas ou não. Após rodar o arquivo do repositório a variável deve ser alterada.