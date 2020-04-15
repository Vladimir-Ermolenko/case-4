"""
Developers: Vladimir E. - 30%
            Kirill S. -50 %
            Svetlana K. - 30%
"""

# importing a library used for getting info from a url and an empty list used for adding all the player info
import urllib.request
total = []

# opening a files with urls and stating it as a url
with open('input.txt') as inp_file:
    lst_file = inp_file.readlines()
for url in lst_file:
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)

# making blank variables
    needed_ratings = 0
    all_ratings = 0
    needed_list = [0, 1, 3, 5, 6, 9]

# finding a name of a player
    part_name = text.find('player-name')
    name = text[text.find('>', part_name)+1:text.find('&', part_name)]

# main function that calculates all the numbers
    part_total = text.find('TOTAL</td>')
    last_td = part_total
    while needed_ratings < len(needed_list):
        if (int(all_ratings)) in needed_list:
            needed_ratings += 1
            total.append(text[text.find('<td>', last_td) + 4:text.find('</td>', last_td + 10)])
        all_ratings += 1
        last_td = text.find('</td>', last_td+10)
    COMP = total[0].replace(',', '')
    ATT = total[1].replace(',', '')
    YDS = total[2].replace(',', '')
    TD = total[3].replace(',', '')
    INT = total[4].replace(',', '')

    rate = ((((float(COMP) / float(ATT)) - 0.3) * 0.5 + ((float(YDS) / float(ATT)) - 3) * 0.25 +
             (float(TD) / float(ATT)) * 20 + 2.375 - ((float(INT) / float(ATT)) * 25)) / 6) * 100
    rate = "%.2f" % rate

# writes all the found info to the output file with the needed formatting
    with open('output.txt', 'a') as out_file:
        print(name, ' ', COMP, ' ', ATT, ' ', YDS, ' ', TD, ' ', INT, ' ', rate, file = out_file)
    total.clear()
