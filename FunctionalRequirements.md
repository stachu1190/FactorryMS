# Factory Management System

## Introduction

Functional requirements specification for a database system designed to help in factory management.

## Business processes

---
<a id="bc1"></a>
### BC1: Sprzedaż aukcyjna 

**Aktorzy:** [Sprzedający](#ac1), [Kupujący](#ac2)

**Opis:** Proces biznesowy opisujący sprzedaż za pomocą mechanizmu aukcyjnego. |

**Scenariusz główny:**
1. [Sprzedający](#ac1) wystawia produkt na aukcję. ([UC1](#uc1))
2. [Kupujący](#ac2) oferuje kwotę za produkt wyższą od aktualnie najwyższej oferty. ([BR1](#br1))
3. [Kupujący](#ac2) wygrywa aukcję ([BR2](#br2))
4. [Kupujący](#ac2) przekazuje należność Sprzedającemu.
5. [Sprzedający](#ac1) przekazuje produkt Kupującemu.

**Scenariusze alternatywne:** 

2.A. Oferta Kupującego została przebita, a [Kupujący](#ac2) pragnie przebić aktualnie najwyższą ofertę.
* 2.A.1. Przejdź do kroku 2.

3.A. Czas aukcji upłynął i [Kupujący](#ac2) przegrał aukcję. ([BR2](#br2))
* 3.A.1. Koniec przypadku użycia.

---

## Actors

<a id="ac1"></a>
### AC1: Administrator

A person that manages the system.

## Use Cases

### Actors and their goals

[Administrator](#ac1):
* [UC1](#uc1): Wystawienie produktu na aukcję

---
<a id="uc1"></a>
### UC1: Wystawienie produktu na aukcję

**Aktorzy:** [Sprzedający](#ac1)

**Scenariusz główny:**
1. [Sprzedający](#ac1) zgłasza do systemu chęć wystawienia produktu na aukcję.
2. System prosi o podanie danych produktu i ceny wywoławczej.
3. [Sprzedający](#ac1) podaje dane produktu oraz cenę wywoławczą.
4. System weryfikuje poprawność danych.
5. System informuje o pomyślnym wystawieniu produktu na aukcję.

**Scenariusze alternatywne:** 

4.A. Podano niepoprawne lub niekompletne dane produktu.
* 4.A.1. System informuje o błędnie podanych danych.
* 4.A.2. Przejdź do kroku 2.

---

<a id="uc2"></a>
### UC2: Przebicie aktualnej oferty

**Aktorzy:** [Kupujący](#ac2)

**Scenariusz główny:**
1. [Kupujący](#ac2) sprawdza cenę i parametry produktu
2. [Kupujący](#ac2) wyraża chęć przebicia aktualnej ceny produktu
3. System prosi [Kupującego](#ac2) o podanie kwoty jaką oferuje za produkt
4. System weryfikuje podaną kwotę

**Scenariusze alternatywne:** 

4.A. Podano niepoprawną kwotę.
* 4.A.1. System informuje o błędnie podanej kwocie.
* 4.A.2. Przejdź do kroku 3.
---

<a id="uc3"></a>
### UC3: Wygranie aukcji

**Aktorzy:** [Kupujący](#ac2), [Sprzedający](#ac1)

**Scenariusz główny:**
1. Mija czas pozostały na podbicie oferty za produkt.
2. System informuje [Sprzedającego](#ac1) i [Kupującego](#ac2) o wyniku aukcji.
3. System przydziela [Kupującemu](#ac2) i [Sprzedającemu](#ac1) wierzyciela który zaautoryzuje przekazanie pieniedzy i produktu
---

<a id="uc4"></a>
### UC4: Przeprowadzenie transakcji

**Aktorzy:** [Kupujący](#ac2), [Sprzedający](#ac1), [Wierzyciel](#ac3)


**Scenariusz główny:**
1. [Kupujący](#ac2) przekazuje kwotę, którą zadeklarował się zapłacić [Wierzycielowi](#ac3)
2. [Wierzyciel](#ac3) weryfikuje kwotę jaką przekazał [Kupujący](#ac2)
3. [Sprzedający](#ac1) przekazuje produkt [Wierzycielowi](#ac3) 
4. [Wierzyciel](#ac3) weryfikuje zgodnosć produktu przekazanego z produktem zaprezentowanym na aukcji.
5. [Wierzyciel](#ac3) przekazuje [Sprzedającemu](#ac1) zadeklarowaną kwotę, a [Kupującemu](#ac2) produkt z aukcji.

**Scenariusze alternatywne:** 

2.A. Przekazana kwota nie zgadza się z zadeklarowaną na aukcji
* 2.A.1. [Wierzyciel](#ac3) informuje o niezgodności kwoty
* 2.A.2. Jeśli [Kupujący](#ac2) zgadza się na przekazanie poprawnej kwoty wracamy do kroku 1, jeśli nie to transakcja jest anulowana.

4.A. Przekazany produkt nie zgadza się z zadeklarowanym na aukcji
* 4.A.1. [Wierzyciel](#ac3) informuje o niezgodności towaru
* 4.A.2. Jeśli [Sprzedający](#ac1) zgadza się na przekazanie poprawnego produktu wracamy do kroku 1, jeśli nie to transakcja jest anulowana.
---

## Obiekty biznesowe (inaczej obiekty dziedzinowe lub informacyjne)

### BO1: Aukcja

Aukcja jest formą zawierania transakcji kupna-sprzedaży, w której Sprzedający określa cenę wywoławczą produktu, natomiast Kupujący mogą oferować własną ofertę zakupu każdorazowo proponując kwotę wyższą od aktualnie oferowanej kwoty. Aukcja kończy się po upływie określonego czasu. Jeśli złożona została co najmniej jedna oferta zakupy produkt nabywa ten Kupujący, który zaproponował najwyższą kwotę. 

### BO2: Produkt

Fizyczny lub cyfrowy obiekt, który ma zostać sprzedany w ramach aukcji.

### BO3: Kwota

Ilość pieniędzy, która ma zostać przekazana


## Reguły biznesowe

<a id="br1"></a>
### BR1: Złożenie oferty

Złożenie oferty wymaga zaproponowania kwoty wyższej niż aktualnie oferowana o minimum 1,00 PLN.


<a id="br2"></a>
### BR2: Rozstrzygnięcie aukcji

Aukcję wygrywa ten z [Kupujący](#ac2)ch, który w momencie jej zakończenia (upłynięcia czasu) złożył najwyższą ofertę.

## Macierz CRUDL


| Przypadek użycia                                  | Aukcja | Produkt | Kwota |
| ------------------------------------------------- | ------ | ------- | ------|
| UC1: Wystawienia produktu na aukcję               |    C   |    C    |    C  |
| UC2: Przebicie aktualnej oferty                   |  R,U   |    R    |  R,U  |
| UC3: Wygranie aukcji                              |    D   |  ...    | ..... |
| UC4: Przeprowadzenie transakcji                   |  ...   |    D    |    D  |


