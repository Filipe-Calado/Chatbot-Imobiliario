arvore={
0 :['bedrooms_discretized <= 1.5',56,1],    
1 :['sqft_living_discretized <= 1.5',27,2],
2 :['locations_discretized <= 0.5',12,3],
3 :['waterfront_discretized <= 0.5',11,4],
4 :['bathrooms_discretized <= 0.5',8,5],
5 :['bedrooms_discretized <= 0.5',7,6],
6 :['MEDIA',0,85] ,
7 :['MEDIA',0,85],
8 :['grade_discretized <= 0.5',10,9],
9 :['MEDIA',0,85],
10 :['MEDIA',0,85], 
11 :['CARA',0,85],
12 :['locations_discretized <= 1.5',20,13],
13 :['sqft_above_discretized <= 0.5',17,14],
14 :['view_discretized <= 0.5',16,15], 
15 :['BARATA',0,85], 
16 :['MEDIA',0,85], 
17 :['sqft_living15_discretized <= 1.5',19,18],
18 :['BARATA',0,85],
19 :['MEDIA',0,85],
20 :['grade_discretized <= 1.5',24,21],
21 :['sqft_living_discretized <= 0.5',23,22],
22 :['MEDIA',0,85],
23 :['MEDIA',0,85], 
24 :['sqft_living15_discretized <= 1.0',26,25],
25 :['MEDIA',0,85],
26 :['MEDIA',0,85],
27 :['bathrooms_discretized <= 1.5',41,28], 
28 :['sqft_living15_discretized <= 1.0',36,29], 
29 :['locations_discretized <= 1.5',33,30],
30 :['bedrooms_discretized <= 0.5',32,31],
31 :['CARA',0,85],
32 :['MEDIA',0,85], 
33 :['bedrooms_discretized <= 0.5',35,34], 
34 :['MEDIA',0,85],
35 :['MEDIA',0,85],
36 :['locations_discretized <= 0.5',38,37],
37 :['CARA',0,85],
38 :['sqft_above_discretized <= 0.5',40,39],
39 :['MEDIA',0,85],
40 :['BARATA',0,85],
41 :['bedrooms_discretized <= 0.5',49,42], 
42 :['locations_discretized <= 0.5',46,43],
43 :['sqft_living15_discretized <= 1.0',45,44],
44 :['CARA',0,85],
45 :['MEDIA',0,85],
46 :['sqft_above_discretized <= 0.5',48,47],
47 :['MEDIA',0,85],
48 :['MEDIA',0,85],
49 :['sqft_living15_discretized <= 1.0',53,50],
50 :['sqft_above_discretized <= 0.5',52,51],
51 :['MEDIA',0,85], 
52 :['MEDIA',0,85],
53 :['grade_discretized <= 0.5',55,54],
54 :['MEDIA',0,85],
55 :['CARA',0,85],
56 :['sqft_living15_discretized <= 1.5',68,57],
57 :['waterfront_discretized <= 0.5',67,58],
58 :['sqft_living_discretized <= 1.5',66,59],
59 :['sqft_living15_discretized <= 0.5',63,60],
60 :['bathrooms_discretized <= 1.5',62,61],
61 :['CARA',0,85], 
62 :['BARATA',0,85], 
63 :['sqft_above_discretized <= 1.5',65,64],
64 :['MEDIA',0,85],
65 :['MEDIA',0,85],
66 :['MEDIA',0,85],
67 :['CARA',0,85],
68 :['sqft_living_discretized <= 0.5',82,69],
69 :['grade_discretized <= 0.5',77,70],
70 :['bathrooms_discretized <= 1.5',74,71],
71 :['locations_discretized <= 1.5',73,72],
72 :['BARATA',0,85],
73 :['BARATA',0,85],
74 :['sqft_above_discretized <= 1.5',76,75],
75 :['MEDIA',0,85],
76 :['BARATA',0,85],
77 :['locations_discretized <= 0.5',81,78],
78 :['bathrooms_discretized <= 1.0',80,79],
79 :['MEDIA',0,85],
80 :['BARATA',0,85],
81 :['MEDIA',0,85],
82 :['bathrooms_discretized <= 0.5',84,83],
83 :['MEDIA',0,85],
84 :['BARATA',0,85],
}
i=0
while i!=85:
    print(arvore[i][0])
    resposta=input('Digite 0 para falso e 1 para verdadeiro')
    if resposta==0:
        i=arvore[i][1]
    else:
        i=arvore[i][2]

