# Assignment 1

We are tasked to implement and analyze the performance of different algorithms. The project is structured into several tasks, each focusing on a specific algorithm or analysis. This is made as part of the course 1DV018 at LNU.

## Requirements

- Python

## How to run

1. Start by installing the required packages.

```bash
pip install -r requirements.txt
```

2. Run the following command in your terminal to execute the main script.:

```bash
python main.py
```

3. OPTIONAL: If you want to generate graphs, run:

```bash
python MatPlot.py
```

To find the graphs, navigate to the `graphs` folder.

## Conclusion in Swedish

### Task 3

Jag har testat med olika storlekar på listorna och sett att tiden ökar med storleken. Detta är i linje med förväntningarna. Jag har också testat med olika antal `unions` och `connected`. Alla är testade med samma antal iterationer för att få en rättvis jämförelse. Förväntningarna innan var inte att det skulle skilja så mycket mellan de olika implementationerna. Men det skiljer en hel del i prestanda. Om vi tar en närmare titt på grafen nedan kan vi se hur `quickfind` presterar i förhållande till `unionfind`.

![Graf över prestanda](graphs/task3_combined_graph.png)

Kollar vi på Union (den första grafen) kan vi se att `quickfind` presterar sämre än `unionfind` när listorna blir större. Detta är rimligt eftersom den itererar över hela listan för att hitta roten. Medan `unionfind` använder en mer effektiv metod för att hitta roten, vilket förklarar den bättre prestandan.

Kollar vi sedan på Connected (den andra grafen) kan vi se att de båda algoritmerna presterar ungefär lika bra. Det skiljer bara några millisekunder, vilket inte är någon betydande tid i det stora hela.

För QuickFind växer tiden linjärt med antalet element. Detta kan vi enkelt visa genom att jämföra tider för olika storlekar:

- Vid 100 000 element tar union-operationen cirka 0,55 sekunder
- Vid 1 000 000 element (10 gånger fler) tar det cirka 5,8 sekunder (ungefär 10 gånger längre tid)

En linjär algoritm (O(n)) förväntas ta ungefär 10 gånger längre tid när indata blir 10 gånger större, vilket stämmer med våra mätvärden (5,8 / 0,55 ≈ 10). Detta bekräftar att QuickFind växer linjärt.

UnionFind däremot ligger kvar på ungefär samma tidsnivå oavsett storlek, vilket visar att dess prestanda i praktiken är nästan konstant. Teoretiskt har den O(log n) komplexitet, men eftersom log n växer mycket långsamt när n ökar, ser vi i praktiken en nästan konstant prestanda för de datamängder vi testat.

### Task 6

Jag har även här testat med olika storlekar på listorna och sett att tiden ökar med storleken, framför allt med ThreeSum (O(n³)). Testar vi den algoritmen med 10 000 element tar det väldigt lång tid. Detta är i linje med förväntningarna då ThreeSum använder sig av 3 loopar, vilket ökar tiden eftersom den måste iterera över alla element i listan för varje loop, jämfört med andra algoritmer som har en lägre tidskomplexitet.

FasterThreeSum (O(n² log n)) presterar bättre än ThreeSum. Detta beror på att den använder sig av en sorterad lista samt en smartare algoritm för att hitta tripletter vars summa blir 0. Den sätter första siffran på plats 0 i arrayen och sedan flyttar den andra och tredje siffran beroende på om summan är mindre eller större än 0. Detta gör att den inte behöver iterera över alla element i listan för varje loop, vilket minskar tiden avsevärt.

När vi testar ThreeSum (O(n³)) ser vi att algoritmen inte växer linjärt, som exempelvis QuickFinds union, utan i praktiken följer en kubisk tillväxt. Vid 200 element tar beräkningen cirka 0,4 sekunder, vid 400 element cirka 3,6 sekunder, och vid 800 element hela 43 sekunder. När vi når 1000 element ökar tiden till närmare 100 sekunder.

Vi kan enkelt se den kubiska tillväxten (O(n³)) genom att jämföra tiderna:

- Vid 400 element tar beräkningen cirka 3,6 sekunder
- Vid 800 element (dubbelt så många) tar det hela 43 sekunder

Om vi fördubblar storlek för en kubisk algoritm, förväntar vi oss att tiden ökar med 2³ = 8 gånger. Vår ökning är 43 / 3,6 ≈ 12 gånger, vilket är i närheten av det förväntade och bekräftar att algoritmen växer ungefär kubiskt.

För den andra varianten, FasterThreeSum (O(n² log n)), är resultatet betydligt bättre. Vid 1000 element tar körningen endast omkring 0,2 sekunder – en mycket stor skillnad jämfört med de nästan 100 sekunder som den kubiska algoritmen kräver. Även denna algoritm växer snabbare än linjärt, men betydligt långsammare än ThreeSum.

Vi kan bekräfta att FasterThreeSum har lägre komplexitet (O(n² log n)) genom att jämföra med ThreeSum:

- ThreeSum med 1000 element: cirka 100 sekunder
- FasterThreeSum med 1000 element: endast 0,2 sekunder

En förbättring med 500 gånger! Detta visar tydligt att FasterThreeSum har en mycket lägre komplexitet än den kubiska algoritmen, vilket stämmer med den teoretiska O(n² log n) tidskomplexiteten.

![Graf över prestanda](graphs/3sum_graph.png)
