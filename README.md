### 1. Install necessary libraries

`pip install -r requirements.txt`


### 2. Run the algorithm
`python main.py --name_dataset 1_ALOI --batch_size 128 --num_epochs_vae 500 --learning_rate_d 0.0005 --grow 2000`

| Number | Data | # Samples | # Features | # Anomaly | % Anomaly | Category |
|:--:|:---:|:---------:|:----------:|:---------:|:---------:|:---:|
|1| ALOI                    |   49534   |     27     |   1508    |   3.04    |     Image     |
|2| annthyroid   |   7200    |     6      |    534    |   7.42    |      Healthcare    |
|3| backdoor|   95329   |    196     |   2329    |   2.44    | Network|
|4| breastw                              |    683    |     9      |    239    |   34.99   | Healthcare  |
|5|campaign|   41188   |     62     |   4640    |   11.27   | Finance|
|6| cardio                               |   1831    |     21     |    176    |   9.61    | Healthcare |        
|7| Cardiotocography    |   2114    |     21     |    466    |   22.04   | Healthcare         |
|8|celeba|  202599   |     39     |   4547    |   2.24    | Image|
|9|census|  299285   |    500     |   18568   |   6.20    | Sociology|
|10| cover                                |  286048   |     10     |   2747    |   0.96    | Botany    | 
|11|donors|  619326   |     10     |   36710   |   5.93    | Sociology|
|12| fault                      |   1941    |     27     |    673    |   34.67   | Physical         |
|13|fraud|  284807   |     29     |    492    |   0.17    | Finance|
|14| glass |    214    |     7      |     9     |   4.21    | Forensic          |
|15| Hepatitis           |    80     |     19     |    13     |   16.25   | Healthcare         |
|16| http                                 |  567498   |     3      |   2211    |   0.39    | Web   |      
|17| InternetAds   |   1966    |    1555    |    368    |   18.72   | Image         |
|18| Ionosphere        |    351    |     32     |    126    |   35.90   | Oryctognosy         |
|19| landsat                         |   6435    |     36     |   1333    |   20.71   | Astronautics    |     
|20| letter                               |   1600    |     32     |    100    |   6.25    | Image     |    
|21| Lymphography       |    148    |     18     |     6     |   4.05    | Healthcare       |  
|22| magic.gamma                     |   19020   |     10     |   6688    |   35.16   | Physical        | 
|23| mammography                          |   11183   |     6      |    260    |   2.32    | Healthcare  |       
|24| mnist                                |   7603    |    100     |    700    |   9.21    | Image      |   
|25| musk                                 |   3062    |    166     |    97     |   3.17    | Chemistry   |      
|26| optdigits                            |   5216    |     64     |    150    |   2.88    | Image     |    
|27| PageBlocks         |   5393    |     10     |    510    |   9.46    | Document         |
|28| pendigits                            |   6870    |     16     |    156    |   2.27    | Image        | 
|29| Pima                |    768    |     8      |    268    |   34.90   | Healthcare         |
|30| satellite                            |   6435    |     36     |   2036    |   31.64   | Astronautics     |    
|31| satimage-2                           |   5803    |     36     |    71     |   1.22    | Astronautics    |     
|32| shuttle                              |   49097   |     9      |   3511    |   7.15    | Astronautics  |       
|33| skin                            |  245057   |     3      |   50859   |   20.75   |    Image      |
|34| smtp                                 |   95156   |     3      |    30     |   0.03    | Web        | 
|35| SpamBase            |   4207    |     57     |   1679    |   39.91   | Document         |
|36| speech                               |   3686    |    400     |    61     |   1.65    | Linguistics    |     
|37| Stamps              |    340    |     9      |    31     |   9.12    | Document         |
|38| thyroid                              |   3772    |     6      |    93     |   2.47    | Healthcare      |   
|39| vertebral                            |    240    |     6      |    30     |   12.50   | Biology       |  
|40| vowels                               |   1456    |     12     |    50     |   3.43    | Linguistics  |       
|41| Waveform           |   3443    |     21     |    100    |   2.90    | Physics         |
|42| WBC                |    223    |     9      |    10     |   4.48    | Healthcare         |
|43| WDBC               |    367    |     30     |    10     |   2.72    | Healthcare         |
|44| Wilt                |   4819    |     5      |    257    |   5.33    | Botany         |
|45| wine                                 |    129    |     13     |    10     |   7.75    | Chemistry   |      
|46| WPBC             |    198    |     33     |    47     |   23.74   | Healthcare   |      
|47| yeast                           |   1484    |     8      |    507    |   34.16   | Biology|
