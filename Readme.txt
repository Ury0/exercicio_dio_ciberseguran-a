📌 README.md
⚠️ Aviso Importante

Este projeto não deve ser utilizado para fins maliciosos.
O código aqui apresentado tem finalidade exclusivamente educacional, para estudo de:

Criptografia simétrica com Fernet

Manipulação de arquivos em Python

Funcionamento básico de ransomware em ambientes controlados

Análise de segurança e conscientização em cibersegurança

⚠️ Nunca execute este código fora de um ambiente de testes isolado, como:

Máquina virtual

Diretório específico criado apenas para testes

Ambiente acadêmico supervisionado

📚 Descrição do Projeto

Este script em Python simula o funcionamento básico de um ransomware educacional, realizando as seguintes ações:

Geração de uma chave criptográfica (Fernet)

Busca recursiva por arquivos em um diretório específico

Criptografia dos arquivos encontrados

Criação de uma mensagem simulando pedido de resgate

O objetivo é compreender o funcionamento técnico, não causar danos.


📌 README.md
⚠️ AVISO LEGAL E ÉTICO

Este projeto é exclusivamente educacional e tem como objetivo demonstrar como keyloggers funcionam para fins de:

Estudo de cibersegurança

Análise de malware / spyware

Conscientização sobre engenharia social e vigilância indevida

Aprendizado de event listeners, threads e automação em Python

🚫 É ilegal e antiético utilizar este código para monitorar usuários sem consentimento explícito.
🚫 Nunca execute este código fora de um ambiente controlado.

📚 Descrição do Projeto

Este projeto implementa um keylogger educacional em Python utilizando a biblioteca pynput, com duas funcionalidades principais:

Captura de teclas digitadas

Envio periódico dos dados capturados por e-mail

O código demonstra como dados podem ser coletados e exfiltrados, permitindo que estudantes entendam como ataques reais funcionam e como se proteger contra eles.
🔍 Funcionamento do Código
⌨️ Captura de Teclas

O programa utiliza pynput.keyboard.Listener para monitorar eventos de teclado:

Teclas normais são registradas como caracteres

Teclas especiais recebem tratamento específico:

Espaço → " "

Enter → nova linha

Tab → tabulação

Backspace → marcador [<]

ESC → [ESC]

Teclas modificadoras (Shift, Ctrl, Alt, etc.) são ignoradas

📝 Registro dos Dados

Há duas abordagens no código:

Escrita direta em arquivo (log.txt)

Armazenamento em variável global (log) para envio por e-mail

Isso demonstra diferentes técnicas de persistência de dados.

📧 Envio Automático por E-mail

Os dados capturados são enviados automaticamente via SMTP (Gmail):

Envio ocorre a cada 60 segundos

Utiliza threading.Timer para execução periódica

O conteúdo do log é enviado como corpo do e-mail

📌 Observação:
O uso de credenciais reais no código não é recomendado. Para estudos, utilize:

Contas de teste

Variáveis de ambiente

SMTP simulado

🧪 Ambiente Seguro para Testes

✔️ Máquina virtual (VirtualBox / VMware)
✔️ Sistema isolado
✔️ Conta de e-mail de testes
❌ Nunca execute em máquinas de terceiros
❌ Nunca use sem consentimento

🎓 Objetivos Educacionais

Este projeto pode ser usado em:

Aulas de Segurança da Informação

Treinamentos de Blue Team / Red Team

Demonstrações de spyware

Estudos de exfiltração de dados

Conscientização sobre privacidade digital

🛡️ Como se Proteger (Aprendizado Defensivo)

Ao estudar este código, aprende-se a:

Identificar comportamentos suspeitos

Reconhecer uso indevido de listeners

Monitorar processos em segundo plano

Implementar políticas de segurança

Usar antivírus e EDRs de forma eficaz