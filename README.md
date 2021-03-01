# discord-bot-checkbot
Jak zacząć pracę z botem?

1. Wpisać imiona i nazwiska osób w klasie do odpowiednich numerów do pliku lista.json
2. Wpisać plan lekcji cały do pliku plan.json. Jest on potrzebny do działania komend c!lekcje i c!dmlekcje
3. Uczniowie na serwerze powinni mieć pseudonimy zaczynające sie numerami od 01* do 26
4. By komenda c!invite działała należy wpisać do pliku botconfig.json w miejscu "inviteLink" link do zaproszenia bota
5. Ostatnim krokiem by wszystko działało jest wpisanie komedny c!setUser na serwerze i oznaczenie roli którą posiada każdy uczeń, a nie posiada jej żaden nauczyciel.

Pytania:

1. Co jeśli mam na serwerze dzielenie na grupy?
//W bocie jest przewidziana taka możliwość. Należy jedynie w pliku commands2.py w asynchronicznej funkcji **sprawdz** skopiować elifa z jedna z grup i powielić go tyle razy ile jest grup, a także wpisać w nowych grupach np. zamiast F wpisać K. A także wypisać numery osób w danych grupach znajdujących się.
![image](https://user-images.githubusercontent.com/54802675/109496770-6481b200-7a91-11eb-8c31-d15f1743b987.png)


*0 przed liczbami od 1 do 9 jest wymagane
