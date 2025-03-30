DESCRIÇÃO DO SISTEMA

Lado do Cliente (client.py):
    - Ao executar o programa, será feita a conexão com o servidor.
    - Após a conexão, aparecerá a mensagem "Digite a conta:"
        - A conta deve ser digitada no formato "1°número 2°número operação"
            - As operações possíveis são soma, subtração e multiplicação.
            - A operação deve ser escrita como:
                - sum 
                - sub
                - mult
    - Após a conta ter sido feita e enviada pelo servidor, a mensagem com o resultado aparece para o cliente e o programa é encerrado.

Lado do Servidor (server.py):
    - Não há interação direta do usuário com o servidor.
    - Após receber os dados da operção do cliente.
        - Os dados são decodificdos e extraidos.
        - Os números são convertidos de string (como são recebidos) para float.
        - A operação escolhida pelo usuário é identificada e executada.
            - Caso a operação escolhida não seja válida é enviada um mensagem de erro.
        - O resultado é codificado e mandado de volta para o cliente e o servidor é encerrado.