# ⚙️ Configuração do Ambiente Google Cloud

Para executar este projeto, você precisa autenticar sua máquina local com o Google Cloud. Siga os passos abaixo.

### 1. Instalação do Google Cloud SDK

O Google Cloud SDK é um conjunto de ferramentas de linha de comando, incluindo o `gcloud`, que você usará para se autenticar.

* **Siga o guia de instalação oficial para o seu sistema operacional:**
    * [Instalar o Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

Após a instalação, feche e reabra seu terminal para garantir que o comando `gcloud` esteja disponível.

### 2. Inicialização e Autenticação

Com o SDK instalado, você precisa configurar suas credenciais de usuário para que as aplicações (como scripts Python) possam usá-las.

1.  **Inicialize o `gcloud`:** Este comando configura seu projeto padrão e a conta.
    ```bash
    gcloud init
    ```
    Ele abrirá uma janela do navegador para você fazer login com sua Conta Google e selecionar um projeto na nuvem.

2.  **Crie as Credenciais de Aplicação Padrão (ADC):** Este é o passo crucial que permite que seu código se autentique.
    ```bash
    gcloud auth application-default login
    ```
    Este comando também abrirá uma janela do navegador para que você autorize o acesso às APIs do Google Cloud em seu nome.

---

Após completar esses passos, seu ambiente estará configurado. O script encontrará e usará automaticamente essas credenciais para se conectar ao BigQuery.
