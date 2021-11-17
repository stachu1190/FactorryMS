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
* [UC1](#uc1): Adding an employee
* [UC2](#uc2): Adding an order
* [UC3](#uc3): Finishing an order
* [UC4](#uc4): Submitting material delivery info
* [UC5](#uc5): Adding a contractor
* [UC6](#uc6): Adding new product
* [UC7](#uc7): Reporting employee attendance

---
<a id="uc1"></a>
### UC1: Adding an employee

**Aktorzy:** [Administrator](#ac1)

**Main scenario:**
1. [Administrator](#ac1) requests adding an employee to the database
2. System asks for information about the employee
3. [Administrator](#ac1) submits informations
4. System verifies if given informations are correct
5. System informs about succesfully adding an employee

**Alternative scenarios:** 

4.A. Given informations are incorrect
* 4.A.1. System alerts that informations are incorrect.
* 4.A.2. Go to step 2.



## Business Objects

### BO1: Order
An order is a transaction between the factory and contractor to exchange products for money or money for materials

### BO2: Employee
A person working in the factory

## Business rules

<a id="br1"></a>
### BR1: Recieving buy order

Recieving an buy order is an agreement to fulfill an order for the factory's products.


<a id="br2"></a>
### BR2: Sending buy order

Sending buy offer is an agreement to exchange money for materials.

## Macierz CRUDL


| Przypadek użycia                                  | Aukcja | Produkt | Kwota |
| ------------------------------------------------- | ------ | ------- | ------|
| UC1: Wystawienia produktu na aukcję               |    C   |    C    |    C  |
| UC2: Przebicie aktualnej oferty                   |  R,U   |    R    |  R,U  |
| UC3: Wygranie aukcji                              |    D   |  ...    | ..... |
| UC4: Przeprowadzenie transakcji                   |  ...   |    D    |    D  |


