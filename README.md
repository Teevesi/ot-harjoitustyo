# Slime-harvester

Tänne tulee ohjelmistotekniikan harjoitustyö, **yksinkertainen** *tower-defence-peli*.

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/Teevesi/ot-harjoitustyo/blob/main/slime-harvester/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/Teevesi/ot-harjoitustyo/blob/main/slime-harvester/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Teevesi/ot-harjoitustyo/blob/main/slime-harvester/dokumentaatio/arkkitehtuuri.md)

- [Vaatimusmäärittely](https://github.com/Teevesi/ot-harjoitustyo/blob/main/slime-harvester/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

- [Käyttöohje](https://github.com/Teevesi/ot-harjoitustyo/blob/main/slime-harvester/dokumentaatio/kayttoohje.md)

## Käynnistysohjeet

Kloonaa repositorio koneellesi tai lataa tiedosto release-kohdasta.

Suorita slime-harvester hakemistossa komento:

    poetry install

Suorita komento

    poetry run invoke start

Käynnistääksesi ohjelman.

## Komennot

Ohjelman voi suorittaa komennolla:

    poetry run invoke start

Ohjelman voi testata komennolla:

    poetry run invoke test

Testikattavuusraportin voi generoida komennolla:

    poetry run invoke coverage

Pylint tarkastuksen ohjelmalle voi tehdä komennolla:

    poetry run invoke lint
