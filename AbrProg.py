import pyautogui as escolha_opcao


opcao = escolha_opcao.confirm('Clique no botão desejado',
                buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":

    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Excel')
    escolha_opcao.sleep(2)
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(2)
    escolha_opcao.click(x=-845, y=317)
    escolha_opcao.sleep(3)

    print("Você abriu o Excel")

elif opcao == "Word":

    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('winword')
    escolha_opcao.sleep(2)
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(3)
    escolha_opcao.click(x=308, y=236)
    escolha_opcao.sleep(3)

    print("Você abriu o Word")



else:

    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad')
    escolha_opcao.sleep(2)
    escolha_opcao.press('Enter')
    
    print("Você abriu o bloco de notas")
