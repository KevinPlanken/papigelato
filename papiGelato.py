bakjestellen='.'
opnieuw='yes'
aantalhorentjes = 0
aantalbakjes = 0
aantalbollentjes = 0
toppingprijs = 0
totaalprijstopping= 0

def klant():
    typeklant = input('Bent u 1) particulier of 2) zakelijk?')
    return typeklant

def vraagbolljes():
    while True:
        aantal = int(input(f"Hoeveel bolletjes wilt u? ")) 
        if aantal == 1 or aantal == 2 or aantal == 3:
            return aantal
        elif aantal == 4 or aantal == 5 or aantal == 6 or aantal == 7 or aantal == 8:
            print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
            return aantal
        elif aantal > 8:
            print("Sorry, dat past niet in onze bakken ")
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def liters():
    aantal2 = int(input(f"Hoeveel liter wilt u? ")) 
    return aantal2

def smaakliter():
    numliter = 1
    while numliter <= aantal2:
        smaak = input(f'Welke smaak wilt u voor bolletjes nummer {numliter}? A) Aardbei, C) Chocolade, V) Vanille?').lower()
        if smaak=='a' or smaak=='c' or smaak=='v':
            numliter+=1
        else:
            print('Sorry dat is geen optie die we aanbieden...')

def smaakkiezen():
    Nbolletje = 1
    while Nbolletje <= aantal:
        smaak = input(f'Welke smaak wilt u voor bolletjes nummer {Nbolletje}? A) Aardbei, C) Chocolade, V) Vanille?').lower()
        if smaak=='a' or smaak=='c' or smaak=='v':
            Nbolletje+=1
        else:
            print('Sorry dat is geen optie die we aanbieden...')

def bakjeofhoorntje():
    while True:
        ijshouder = input(f'Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?').lower()
        if ijshouder=='a':
            global aantalhorentjes
            ijshouder = 'Hoorntje'
            aantalhorentjes+=1
            return ijshouder
        elif ijshouder=='b':
            global aantalbakjes
            ijshouder = 'Bakje'
            aantalbakjes+=1
            return ijshouder
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def again():
    while True:
        opnieuw = input(f'Hier is uw {ijshouder} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Yes/No)').lower()
        if opnieuw == 'yes':
            return opnieuw
        elif opnieuw =='no':
            print('Bedankt en tot ziens!')
            return opnieuw
        else:
            print('Sorry dat is geen optie die we aanbieden...')

def toppings():
    topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?').lower()
    if topping!='a' and topping!='b' and topping!='c' and topping!='d':
        print("sorry dat is geen optie die we aanbieden..")
        toppingprijs = 0
    else:
        if topping == 'a':
            toppingprijs = 0
        elif topping == 'b':
            toppingprijs = 0.50
        elif topping == 'c':
            toppingprijs = (0.30 * aantal)
        elif topping == 'd' and ijshouder == 'Hoorntje':
            toppingprijs = 0.60
        elif topping == 'd' and ijshouder != 'Hoorntje':
            toppingprijs = 0.90

    return toppingprijs

def bonnetje():
    if typeklant=='1':
        if  aantalbakjes >= 1:
            totaalbakje=f'bakje {aantalbakjes} x 0,75 = $ {round(aantalbakjes*0.75, 2)}'
        else:
            totaalbakje = ''
        if  aantalhorentjes >= 1:
            totaalhoornje=f'Hoorntje {aantalhorentjes} x 1,25 = $ {round(aantalhorentjes*1.25, 2)}'
        else:
            totaalhoornje = ''
        if  aantalbollentjes >= 1:
            totaalbollentje=f'bolletjes {aantalbollentjes} x 0,95 = $ {round(aantalbollentjes*0.95, 2)}'
        else:
            totaalbollentje = ''
        if  totaalprijstopping >= 0.1:
            totaaltopping=f'''Topping  {totaalprijstopping} = $ {'{0:.2f}'.format(totaalprijstopping)}'''
        else:
            totaaltopping = ''

        totaalmoney=f'Totaal  €{round(aantalbollentjes*0.95, 2)+ round(aantalhorentjes*1.25, 2)+ round(aantalbakjes*0.75, 2) + + round(totaalprijstopping, 2)}' 
        
        print(f'''-------------[papi gelato]------------
        
        {totaalbollentje}
        {totaalhoornje}
        {totaalbakje}
        {totaaltopping}
        

        {totaalmoney}
        ''')
    else:
        totaalprijs = aantal2*9.80

        print(f'''-------------[papi gelato]------------
                
        Liters {aantal2} x 9,80 = {'{0:.2f}'.format(totaalprijs)}

        Totaal = {'{0:.2f}'.format((totaalprijs))}
        BTW (6%) = {'{0:.2f}'.format(((totaalprijs/100)*6))}
        ''')


print("welkom bij papi gelato")  
typeklant = klant()
    
if typeklant=='1':
    while opnieuw=='yes': 
        aantal = vraagbolljes()
        smaakkiezen()
        if aantal<=3:
            ijshouder = bakjeofhoorntje()
        else:
            ijshouder='Bakje'
            aantalbakjes+=1
        totaalprijstopping += toppings()
        opnieuw = again()
        aantalbollentjes+=aantal
else:
    aantal2 = liters()
    smaakliter()

bonnetje()
      

