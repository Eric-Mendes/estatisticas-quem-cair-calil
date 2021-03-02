import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def times_do_brasileirao(t):
    if t == 'INT':
        return 'INTERNACIONAL'
    elif t == 'FLA':
        return 'FLAMENGO'
    elif t == 'ATL':
        return 'ATLÉTICO MINEIRO'
    elif t == 'SAO':
        return 'SÃO PAULO'
    elif t == 'FLU':
        return 'FLUMINENSE'
    elif t == 'PAL':
        return 'PALMEIRAS'
    elif t == 'GRE':
        return 'GRÊMIO'
    elif t == 'CAP':
        return 'ATHLÉTICO PARANAENSE'
    elif t == 'CEA':
        return 'CEARÁ'
    elif t == 'COR':
        return 'CORINTHIANS'
    elif t == 'SAN':
        return 'SANTOS'
    elif t == 'ACG':
        return 'ATLÉTICO GOIANIENSE'
    elif t == 'BGT':
        return 'BRAGANTINO'
    elif t == 'VAS':
        return 'VASCO'
    elif t == 'BAH':
        return 'BAHIA'
    elif t == 'SPO':
        return 'SPORT'
    elif t == 'FOR':
        return 'FORTALEZA'
    elif t == 'GOI':
        return 'GOIÁS'
    elif t == 'CFC':
        return 'CORITIBA'
    elif t == 'BOT':
        return 'BOTAFOGO'
    return ''


RODADAS = 33

# entrar na competição
browser = webdriver.Firefox(executable_path=PATH_TO_GECKO_DRIVER)
browser.get("https://cartolafc.globo.com/#!/login")
time.sleep(5)
username = browser.find_element_by_id("login")
username.clear()
username.send_keys(EMAIL)
time.sleep(5)
password = browser.find_element_by_id("password")
password.clear()
password.send_keys(PASSWORD)
browser.find_element_by_css_selector('button.ng-scope').click()
time.sleep(10)
try:
    if browser.find_element_by_class_name("cartola-popin-header__close__icone").is_displayed():
        browser.find_element_by_class_name("cartola-popin-header__close__icone").click()
except NoSuchElementException:
    print('OK')

time.sleep(10)
browser.find_element_by_name("Competições").click()
time.sleep(5)
browser.find_element_by_class_name("cartola-button.button").click()
time.sleep(5)
browser.find_element_by_class_name("cookie-banner-lgpd_accept-button").click()
time.sleep(3)
browser.find_element_by_class_name("card-liga__titulo").click()

data = []

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
        for k in range(12):
            pont = '-'
            nome_jog = '-'
            pos = '-'
            team_ = '-'
            capitao = '-'
            try:
                if browser.find_element_by_xpath("//div[contains(@class, 'cartola-time-adv__pontuacao') and (contains(@class, 'pont-positiva') or contains(@class, 'pont-negativa'))]").is_displayed():

                    nome = browser.find_elements_by_xpath("//div["
                                                          "contains(@class, 'cartola-atletas__apelido')]")[k]
                    nome_jog = nome.text
                    posicao = browser.find_elements_by_xpath("//div["
                                                             "contains(@class, 'cartola-atletas__posicao')]")[k]
                    pos = posicao.text

                    time__ = browser.find_elements_by_xpath("//div["
                                                            "contains(@class, 'cartola-atletas__time__abreviacao')]")[k]
                    team_ = time__.text

                    pontuacao = browser.find_elements_by_xpath("//div[@class='pontuacao-atleta__pts-calculados']")[k]
                    pont = pontuacao.text
                    jog = browser.find_elements_by_xpath(
                        "//div[@class='columns small-22 small-offset-1 large-20 large-offset-2 xxlarge-14 xxlarge-offset-5']")[k]

                    if jog.find_element_by_xpath("./div[@class='cartola-atletas__card cartola-atletas__card--com-parciais']/*[name()='svg']").is_displayed():
                        capitao = 'SIM'
            except NoSuchElementException:
                capitao = 'NÃO'
            line = [team, round, nome_jog, pos, pont, capitao, team_]
            print(line)
            data.append(line)
        browser.back()
    browser.back()
df = pd.DataFrame(data, index=[i for i in range(1, len(data) + 1)],
                  columns=['EQUIPE', 'RODADA', 'JOGADOR', 'POSIÇÃO', 'PONTUAÇÃO', 'CAPITÃO', 'TIME'])

df.head()
times = list(df['TIME'])
times_completos = list(map(times_do_brasileirao, times))
df['TIME'] = times_completos

df.to_csv(rPATH_TO_WHERE_YOU_WANT_TO_STORE_CSV, index=False)
