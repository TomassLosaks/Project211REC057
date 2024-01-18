# Project211REC057
NewsBot, kurš atsūta Latvijas galveno dienas ziņu Telegramma.

1. # Projekta uzdevums:
Savā projektā es izveidoju kodu, kura uzdevums ir izņemt caur noteiktu vietni datus, manā gadījumā Latvijas ziņu portālu LSM.lv (https://www.lsm.lv/zinas/latvija/). Kods paņem galvenās dienas ziņas Latvijā un nosūta tās uz telegram ziņu botu, kas tika izveidots speciāli šim nolūkam. Ar 30 minūšu intervālu kods tiek automātiski atjaunināts un meklē jaunas ziņas. Ja ziņu nav, tad bots nesūta neko, bet, ja ir, tad tās nosūta telegram botā. Vēl ir tekstu fails (news_database.txt), kur saglabājas visas ziņas, kurus kods atsūtīja telegram botā.
Gadījumā, ja kods dabūs kļūdu, terminālā rādīs 'Error' un kods beigs savu darbu.
Kods ņem no galvenās ziņas virsrakstu, galveno aprakstu un unikālo linku.

2. # Izskaidrosiet kādas Python bibliotēkas un kāpēc tiek izmantotas projekta izstrādes laikā:
Savā projektā es izmantoju bibliotēkas:

    1. pip install telebot - Šī bibliotēka izmantota priekš Telegram bota

    2. pip install selenium - Priekš veb-brauzera automatizācijas

    3. pip install beautifulsoup4 - Lai analizētu HTML kodu tīmekļa lapai

    4. import time (Standarta biblitēka Python) - Lai var likt pauzi kodā
    
    5. Drivers ChromeDriver - ChromeDriver tiek izmantots kopā ar Selenium bibliotēku, lai automatizētu Google Chrome tīmekļa pārlūkprogrammu

3. #  Aprakstīsies programmatūras izmantošanas metodes:
Programmu var izmantot ērtai un ātrai galveno Latvijas ziņu apskatei. Nav nepieciešams doties uz ziņu lapu ar lielu informācijas daudzumu.
Es bieži izmantoju sociālos tīklus un vēl vairāk sarakstes tīklus. Man ir ērtāk iegūt informāciju telegramā, neka lasīt ziņas no lapas, jo sen jau izmantoju šo sarakstes tīklu ne tikai sarakstēm. Vēl tur nav reklāmas un citas lietas, kas traucē skatīties ziņas.

4. # Pa šo linku var apskatities kodu darbību(Video):
    https://youtu.be/HLIdZcWYu3Y

5. # Pa šo linku atrodas pats bots, kur atnāk ziņas:
    https://t.me/News211REC057Bot

Bota nosaukums: @News211REC057Bot
Bota token: 6366025247:AAHxq1ItTERwWPuRFI1OUhWasEDaS_r4CEg
Čata ID: 507643624