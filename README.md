# coopmaster-room-assistant
- komunikator mezi home assistantem a room driverem

## funkcionalita
- s home assistantem komunikuje pomocí messagingového protokolu **mqtt**
- data načítá a posílá příkazi pomocí http protokolu posílá na room driver
- akce jsou vyvolány pomocí zpráv posílaných home assistantem na topici které aplikace subscribuje (topici pro příkazy dvířek a světla)
- jednou za čas aktualizuje data ze senzorů a stav arduina. ty pak publishuje na topici home assistanta (topici pro teplotu, vlhkost, stav dvířek, stav světla)
- lze doimplementovat automatické ovládání světel a dvířek pro případ nefunkčnosti home assistanta
  - resi rano otevirani dveri kurniku a vecer zavirani
  - Integrace se sluzbou  - https://api.sunrise-sunset.org/json?lat=50&lng=14.5
  - dvere se nezavrou pokud nejsou slepice doma (kontrolu lze provézd zavoláním přímo na chicken watch guarda)
  - dvere v modu automatickeho zavirani si volaji o data kdy zavirat https://kodim.cz/czechitas/daweb/js2/server-komunikace/cv-volani-api/vychod-zapad 

## technologie
- python
- knihovny pro python
  - **Flask**: Lehký webový framework pro rychlý vývoj webových aplikací.
  - **colorama**: Manipulace s barvami v textovém výstupu na terminálu.
  - **waitress**: Rychlý WSGI server pro produkční nasazení webových aplikací.
  - **APScheduler**: Plánování a automatizace úloh v Pythonu.
  - **requests**: Jednoduché HTTP požadavky (GET, POST, atd.).
  - **paho-mqtt**: MQTT klient pro komunikaci s IoT zařízeními.
  - **Werkzeug**: WSGI nástroje pro webové aplikace (routování, správa relací).
  - **python-dotenv**: Načítání konfigurace z `.env` souborů.

## hardware
- Nuc


