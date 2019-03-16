from . import get_random

owoce_podstawowe = ['banany', 'jabłka', 'morele']
owoce_dodatkowe = ['śliwki', 'truskawki', 'winogrona']
owoce_drobne = ['maliny', 'porzeczki', 'jeżyny']

warzywa = ['pomidory', 'ogórki', 'rzodkiewki']
dodatki_korzystne_dla_mozgu = [
    'orzeszki ziemne',
    'orzechy włoskie',
    'pestki dynii'
]


platki_otreby_z_owocami = ['2 jogurty naturalne małe', '4 łyżeczki płatków owsianych',
                           '4 łyżeczki otrębów gryczanych', '2 łyżeczki otrębów owsianych'] + get_random(owoce_drobne)

jogurt_z_otrebami_owsianymi = [
    '1 jogurt naturalny mały',
    '50g otrębów owsianych'
]

jajecznica_na_boczku = ['3 jajka', '50g boczku', '10g olej kokosowy']
serek_wiejski_z_tunczykiem = ['100g tłustego twarogu', '50g tuńczyka w oleju']
omlet_z_warzywami = ['3 jajka', 'papryka', 'pomidory']


piers_z_kurczaka_z_ryzem = [
    '200 g piersi z kurczaka',
    '100 g ryżu'
    'papryka',
]

kurczak_w_sosie_curry = piers_z_kurczaka_z_ryzem + \
    ['90g jogurtu naturalnego', '0,5 ząbka czosnku', '2,5 łyżki curry', 'sól']

kurczak_w_sosie_pomidorowym = piers_z_kurczaka_z_ryzem + \
    ['1 cebula', '0,5 ząbka czosnku', '0,5 puszki pomidorów', '1 łyżka oliwy']

chuda_ryba_z_warzywami = [
    '200g mintaja',
    '100g kaszy gryczanej'] + get_random(warzywa)

wieprzowina_z_ziemniakami = ['200g wieprzowiny', '300g ziemniaków', 'brokuly']


piers_z_kurczaka_z_ryzem_i_rodzynkami = [
    '200 g piersi z kurczaka', '100 g ryżu' '50 g rodzynek'
]
twarog_z_owocami = [
    '200 g chudego twarogu',
    '2 banany',
    '20 g suszonych daktyli'
]
indyk_z_makaronem = [
    '200 g piersi z indyka',
    '100 g makaronu',
    'kukurydza',
    'pomidory',
    'ogórki',
    'rzodkiewki'
]

ryz_na_slodko = ['100g ryzu', '2 miarki odzywki bialkowej', '1 jabłko']
kasza_jaglana_z_rodzynkami = ['100g kaszy jaglanej', '50g rodzynek']
shake_z_ryzem_i_bananami = [
    '100g ryzu',
    '0,5 litra mleka ryzowego',
    '2 banany'
]
