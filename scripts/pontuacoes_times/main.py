import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

RODADAS = 33


class Node:
    def __init__(self, nome_time, id_rodada, pontuacao, ponts_cap):
        self.nome_time = nome_time
        self.id_rodada = id_rodada
        self.pontuacao = pontuacao


def sort_node_points(node):
    return node.pontuacao


browser = webdriver.Firefox(executable_path=PATH_TO_GECKO_DRIVER)

browser.get("https://cartolafc.globo.com/#!/login")

time.sleep(5)
username = browser.find_element_by_id("login")
username.clear()
username.send_keys(YOUR_EMAIL)

time.sleep(5)
password = browser.find_element_by_id("password")
password.clear()
password.send_keys(YOUR_PASSWORD)

browser.find_element_by_css_selector('button.ng-scope').click()

time.sleep(10)
browser.find_element_by_name("Competições").click()

time.sleep(5)
browser.find_element_by_class_name("cartola-button.button").click()

time.sleep(5)
browser.find_element_by_class_name("cookie-banner-lgpd_accept-button").click()

time.sleep(3)
browser.find_element_by_class_name("card-liga__titulo").click()

"""
My league only had 7 teams
"""
eric = []

caio = []
ibobesta = []

calil = []
canela = []

rafa = []
janderson = []

qtd_times = 7
index_times = range(qtd_times)
for i in index_times:
    time.sleep(3)
    time_ = browser.find_elements_by_xpath("//span[@class='cartola-card-thin__nome__time']")[i]
    team = time_.text
    time_.click()
    time.sleep(5)

    print(team)
    nro_rodadas = RODADAS
    index_rodadas = range(nro_rodadas)
    for j in index_rodadas:
        time.sleep(3)
        dropdown = browser.find_element_by_xpath("//span[@class='cartola-dropdown-bg__titulo']")
        dropdown.click()

        time.sleep(3)
        rodada = browser.find_elements_by_xpath("//div[@class='cartola-dropdown-bg__selecao']")[j]
        round = rodada.text
        rodada.click()

        print(round)
        time.sleep(3)
        points = 0.00

        try:
            if browser.find_element_by_xpath("//div[contains(@class, 'cartola-time-adv__pontuacao') and (contains(@class, 'pont-positiva') or contains(@class, 'pont-negativa'))]").is_displayed():
                points = browser.find_element_by_xpath("//div[contains(@class, 'cartola-time-adv__pontuacao') and (contains(@class, 'pont-positiva') or contains(@class, 'pont-negativa'))]").text
        except NoSuchElementException:
            points = 0.00

        capitao = 0.00
        try:
            if browser.find_element_by_xpath("//div[contains(@class, 'cartola-time-adv__pontuacao') and (contains(@class, 'pont-positiva') or contains(@class, 'pont-negativa'))]").is_displayed():
                capitao = browser.find_element_by_class_name("pontuacao-atleta__pts-reais").text
        except NoSuchElementException:
            capitao = 0.00

        nd = Node(team, round, float(points), capitao)
        print(points)
        if team == "Unichampions":
            eric.append(nd)
        elif team == "Gigante de JF":
            calil.append(nd)
        elif team == "Caio do Céu":
            caio.append(nd)
        elif team == "Vanculotte Atiantino":
            rafa.append(nd)
        elif team == "Ibobesta Líbero":
            ibobesta.append(nd)
        elif team == "Janderson maisdez":
            janderson.append(nd)
        elif team == "Do Pescoço pra Baixo é Canela EC":
            canela.append(nd)
        browser.back()
    browser.back()
eric = sorted(eric, key=sort_node_points)

calil = sorted(calil, key=sort_node_points)

rafa = sorted(rafa, key=sort_node_points)

caio = sorted(caio, key=sort_node_points)

ibobesta = sorted(ibobesta, key=sort_node_points)

canela = sorted(canela, key=sort_node_points)

janderson = sorted(janderson, key=sort_node_points)

resultado = []
resultado_total = []
for i in range(RODADAS):
    resultado_total.append(eric[i])

for i in range(RODADAS):
    resultado_total.append(calil[i])

for i in range(RODADAS):
    resultado_total.append(rafa[i])

for i in range(RODADAS):
    resultado_total.append(caio[i])

for i in range(RODADAS):
    resultado_total.append(ibobesta[i])

for i in range(RODADAS):
    resultado_total.append(canela[i])

for i in range(RODADAS):
    resultado_total.append(janderson[i])

for i in range(RODADAS):
    max_eric = eric[-1]
    max_caio = caio[-1]
    max_calil = calil[-1]
    max_rafa = rafa[-1]
    max_ibobesta = ibobesta[-1]
    max_canela = canela[-1]
    max_janderson = janderson[-1]

    max_total = max(max_caio.pontuacao, max_calil.pontuacao, max_eric.pontuacao,
                    max_canela.pontuacao, max_janderson.pontuacao, max_rafa.pontuacao, max_ibobesta.pontuacao)

    if max_total == max_ibobesta.pontuacao:
        resultado.append(ibobesta[-1])
        ibobesta.pop(-1)
    elif max_total == max_rafa.pontuacao:
        resultado.append(rafa[-1])
        rafa.pop(-1)
    elif max_total == max_eric.pontuacao:
        resultado.append(eric[-1])
        eric.pop(-1)
    elif max_total == max_calil.pontuacao:
        resultado.append(calil[-1])
        calil.pop(-1)
    elif max_total == max_janderson.pontuacao:
        resultado.append(janderson[-1])
        janderson.pop(-1)
    elif max_total == max_caio.pontuacao:
        resultado.append(caio[-1])
        caio.pop(-1)
    elif max_total == max_canela.pontuacao:
        resultado.append(canela[-1])
        canela.pop(-1)

colors = []
uni = 0
jf = 0
ceu = 0
vanc = 0
ib = 0
jand = 0
pesc = 0

for i in range(len(resultado)):
    if resultado[i].nome_time == "Unichampions":
        uni += 1
        colors.append('b')
    elif resultado[i].nome_time == "Gigante de JF":
        jf += 1
        colors.append('g')
    elif resultado[i].nome_time == "Caio do Céu":
        ceu += 1
        colors.append('r')
    elif resultado[i].nome_time == "Vanculotte Atiantino":
        vanc += 1
        colors.append('c')
    elif resultado[i].nome_time == "Ibobesta Líbero":
        ib += 1
        colors.append('m')
    elif resultado[i].nome_time == "Janderson maisdez":
        jand += 1
        colors.append('y')
    elif resultado[i].nome_time == "Do Pescoço pra Baixo é Canela EC":
        pesc += 1
        colors.append('k')

data = []
for i in range(len(resultado_total)):
    line = [resultado_total[i].id_rodada, resultado_total[i].nome_time, resultado_total[i].pontuacao]
    data.append(line)

df = pd.DataFrame(data, index=[i for i in range(1, len(resultado_total)+1)], columns=['RODADA', 'TIME', 'PONTUAÇÃO'])

df.head()
df.to_csv(rPATH_WHERE_YOU_WANT_TO_STORE_THE CSV, index=False)

# I used to plot a bar graph with the highest [_RODADAS_] points
N = RODADAS
ind = np.arange(N)
plot = plt.bar(ind, [resultado[i].pontuacao for i in range(len(resultado))], color=colors)

plt.ylabel("Pontuações")
plt.title("Quem Cair Calil: As {} Maiores Pontuações".format(RODADAS))
plt.yticks(np.arange(0, max(resultado, key=sort_node_points), 10))
plt.xticks(ind, [resultado[i].id_rodada for i in range(len(resultado))], rotation='vertical')
colors = {'Unichampions {}'.format(uni): 'b', 'Gigante de JF {}'.format(jf): 'g',
          'Caio do Céu {}'.format(ceu): 'r',
          'Vanculotte Atiantino {}'.format(vanc): 'c',
          'Ibobesta Líbero {}'.format(ib): 'm', 'Janderson maisdez {}'.format(jand): 'y',
          'Do Pescoço pra Baixo é Canela EC {}'.format(pesc): 'k'}
labels = list(colors.keys())
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.show()

