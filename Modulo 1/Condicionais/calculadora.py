
def adicionar():
    nome = input("digite qual tarefa voce vai fazer: ")
    descrição = input("descreva sua tarefa: ")
    status = input("a tarefa esta concluida? (sim/não): ")
    if status == "s":
            concluida = True
    else:
            concluida = False



def visualisar():
    for t in tarefas:
        if t[2]:
            print(f"{t[0]} - {t[1]} concluida")
        else:
            print(f"{t[1]} - {t[0]} nao concluida")

   
