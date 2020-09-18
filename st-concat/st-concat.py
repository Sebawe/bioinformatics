import re 
import pandas as pd


x = """ST	cpn60	fusA	gltA	pyrG	recA	rplB	rpoB	clonal_complex	species
1	1	1	1	1	5	1	1		A. baumannii
2	2	2	2	2	2	2	2		A. baumannii
3	3	3	2	2	3	1	3		A. baumannii
4	1	3	3	2	4	1	4		A. baumannii
5	4	1	2	2	4	1	5		A. baumannii
6	5	4	4	1	3	3	4		A. baumannii
7	1	1	1	2	5	1	1		A. baumannii
8	1	1	1	1	1	1	1		A. baumannii
9	3	1	5	3	6	1	3		A. baumannii
10	1	3	2	1	4	4	4		A. baumannii
11	1	2	6	2	3	4	4		A. baumannii
12	3	5	7	1	7	2	6		A. baumannii
13	3	1	2	2	4	1	3		A. baumannii
14	3	3	2	2	3	1	7		A. baumannii
15	6	6	8	2	3	5	4		A. baumannii
16	7	7	2	2	8	4	4		A. baumannii
17	3	29	30	1	9	1	4		A. baumannii
18	1	8	9	2	4	6	4		A. baumannii
19	1	2	1	1	5	1	1		A. baumannii
20	3	1	1	1	5	1	1		A. baumannii
21	3	3	2	2	4	4	8		A. baumannii
22	3	9	3	2	4	1	9		A. baumannii
23	1	3	10	1	4	4	4		A. baumannii
24	1	10	2	2	9	1	10		A. baumannii
25	3	3	2	4	7	2	4		A. baumannii
26	1	2	11	5	3	1	11		A. baumannii
27	3	3	12	2	9	7	4		A. baumannii
28	1	1	2	2	10	4	4		A. baumannii
29	1	3	13	1	5	8	12		A. baumannii
30	1	1	2	5	3	2	3		A. baumannii
31	1	2	2	2	11	1	1		A. baumannii
32	1	1	2	2	3	4	4		A. baumannii
33	3	5	7	1	7	1	4		A. baumannii
34	8	1	14	3	12	1	13		A. baumannii
35	9	3	2	2	5	4	14		A. baumannii
36	1	2	2	2	3	1	2		A. baumannii
37	3	2	2	2	7	1	2		A. baumannii
38	3	2	15	6	6	4	5		A. baumannii
39	10	4	3	2	13	1	2		A. baumannii
40	1	2	2	2	5	1	14		A. baumannii
41	1	1	2	2	12	1	5		A. baumannii
42	3	11	16	1	13	1	15		A. baumannii
43	3	3	13	2	4	4	5		A. baumannii
44	11	2	2	4	13	1	2		A. baumannii
45	2	6	2	2	2	2	2		A. baumannii
46	5	12	11	2	14	9	14		A. baumannii
47	2	13	2	2	2	2	2		A. baumannii
48	3	14	2	2	15	4	5		A. baumannii
49	3	3	6	2	3	1	5		A. baumannii
50	3	15	17	2	3	1	2		A. baumannii
51	3	16	6	2	16	4	2		A. baumannii
52	3	2	2	7	9	1	5		A. baumannii
53	1	1	2	2	3	4	2		A. baumannii
54	12	3	18	2	17	4	5		A. baumannii
55	13	4	2	2	6	1	16		A. baumannii
56	3	17	7	2	18	1	2		A. baumannii
57	1	3	17	5	3	1	14		A. baumannii
58	13	4	2	2	7	1	2		A. baumannii
59	3	2	19	2	5	2	5		A. baumannii
60	14	18	20	8	19	10	17		A. calcoaceticus
61	15	18	21	8	19	11	18		A. calcoaceticus
62	16	19	22	9	19	12	19		A. calcoaceticus
63	17	20	23	10	20	13	20		A. pittii
64	17	21	23	10	20	13	20		A. pittii
65	18	22	24	11	21	14	21		13BJ
66	19	23	25	12	22	15	22		15
67	19	23	25	13	22	15	22		15
68	20	24	26	14	23	16	23		A. nosocomialis
69	21	25	24	15	24	17	24		13BJ
70	23	20	23	16	25	18	20		A. pittii
71	20	26	26	14	26	16	25		A. nosocomialis
72	24	27	27	17	20	18	20		A. pittii
73	23	28	28	10	25	18	26		A. pittii
74	22	26	29	14	27	16	23		A. nosocomialis
75	17	21	23	10	20	13	27		A. pittii
76	20	26	26	18	27	19	23		A. nosocomialis
77	3	2	2	2	3	4	28		A. baumannii
78	25	3	6	2	28	1	29		A. baumannii
79	26	2	2	2	29	4	5		A. baumannii
80	1	1	10	1	4	4	5		A. baumannii
81	1	1	1	1	5	1	2		A. baumannii
82	28	3	2	1	4	4	4		A. baumannii
83	26	4	2	2	9	1	4		A. baumannii
84	6	6	8	2	3	5	30		A. baumannii
85	5	2	4	1	3	3	4		A. baumannii
86	6	30	2	19	31	20	31		
87	29	31	31	20	32	21	32		
88	30	31	32	21	33	21	32		
89	31	32	32	22	34	22	33		
90	32	33	33	23	35	23	34		A. seifertii
91	33	34	34	23	36	23	35		A. seifertii
92	15	18	35	24	37	10	19		A. calcoaceticus
93	17	20	23	10	20	18	27		A. pittii
94	1	2	2	1	5	1	1		A. baumannii
95	1	3	2	2	4	24	2		A. baumannii
96	1	2	36	2	2	2	2		A. baumannii
97	2	2	36	2	2	2	2		A. baumannii
98	1	2	2	2	2	2	2		A. baumannii
99	12	3	18	2	4	4	5		A. baumannii
100	1	1	1	2	1	1	2		A. baumannii
101	1	1	1	2	1	1	1		A. baumannii
102	1	1	1	2	1	5	2		A. baumannii
103	7	3	2	1	7	1	4		A. baumannii
104	2	2	2	2	2	2	14		A. baumannii
105	1	2	2	2	5	1	2		A. baumannii
106	3	3	16	1	13	1	1		A. baumannii
107	34	35	37	1	5	6	36		A. baumannii
108	35	1	11	7	9	25	2		A. baumannii
109	26	4	2	2	9	1	5		A. baumannii
110	3	2	2	4	7	2	2		A. baumannii
111	3	3	2	2	4	8	12		A. baumannii
112	35	36	11	7	9	25	2		A. baumannii
113	3	3	3	4	7	4	4		A. baumannii
114	3	3	3	1	7	4	4		A. baumannii
115	2	2	2	1	2	2	2		A. baumannii
116	1	1	1	4	5	1	1		A. baumannii
117	12	37	2	2	9	2	14		A. baumannii
118	35	2	11	2	9	1	2		A. baumannii
119	36	20	38	16	38	18	20		A. pittii
120	37	1	14	3	12	1	13		A. baumannii
121	17	20	23	10	20	18	37		A. pittii
122	17	20	23	10	20	26	37		A. pittii
123	5	2	1	2	3	1	5		A. baumannii
124	3	3	2	2	28	1	3		A. baumannii
125	2	1	1	1	5	1	1		A. baumannii
126	3	2	7	2	7	1	3		A. baumannii
127	27	2	7	7	2	1	2		A. baumannii
128	1	38	2	2	3	4	4		A. baumannii
129	3	2	3	2	2	2	2		A. baumannii
130	8	1	14	3	12	1	5		A. baumannii
131	3	2	2	2	3	2	6		A. baumannii
132	3	5	5	1	7	1	4		A. baumannii
133	3	1	2	1	18	1	5		A. baumannii
134	27	4	2	2	9	1	2		A. baumannii
135	5	2	39	2	39	1	5		A. baumannii
136	3	2	19	25	5	2	5		A. baumannii
137	3	3	15	2	40	4	4		A. baumannii
138	3	3	7	26	7	1	4		A. baumannii
139	1	4	2	1	42	2	2		A. baumannii
140	3	39	2	6	41	1	14		A. baumannii
141	26	2	2	1	43	4	5		A. baumannii
142	13	4	40	1	42	1	16		A. baumannii
143	2	2	2	2	2	2	38		A. baumannii
144	27	2	7	2	2	1	39		A. baumannii
145	1	4	2	2	13	1	2		A. baumannii
146	1	4	2	2	7	1	3		A. baumannii
147	13	5	2	1	7	1	4		A. baumannii
148	70	34	34	23	36	23	35		A. seifertii
149	3	12	11	2	14	9	14		A. baumannii
150	39	2	2	2	4	27	4		A. baumannii
151	27	5	7	1	7	1	4		A. baumannii
152	8	1	5	3	6	2	3		A. baumannii
153	38	1	14	3	12	1	5		A. baumannii
154	3	41	6	1	3	4	5		A. baumannii
155	3	2	2	2	44	4	4		A. baumannii
156	26	2	2	2	29	4	4		A. baumannii
157	1	3	2	1	4	24	2		A. baumannii
158	41	42	13	1	5	4	14		A. baumannii
159	42	43	41	27	45	28	31		
160	1	1	1	1	5	1	41		A. baumannii
161	20	26	26	14	26	16	40		A. nosocomialis
162	3	2	2	2	2	4	8		A. baumannii
163	3	2	2	2	2	4	5		A. baumannii
164	40	3	7	2	40	4	4		A. baumannii
165	6	6	8	1	3	5	4		A. baumannii
166	26	1	2	2	9	1	5		A. baumannii
167	26	2	2	2	9	1	5		A. baumannii
168	26	3	2	2	9	1	5		A. baumannii
169	26	2	2	2	29	1	5		A. baumannii
170	26	4	2	2	29	4	5		A. baumannii
171	26	16	2	2	29	4	5		A. baumannii
172	1	16	2	6	18	4	4		A. baumannii
173	26	4	1	1	5	1	1		A. baumannii
174	1	2	1	1	5	1	5		A. baumannii
175	26	1	2	2	29	4	5		A. baumannii
176	1	2	2	2	18	4	4		A. baumannii
177	3	3	6	2	4	1	29		A. baumannii
178	3	1	3	4	7	4	4		A. baumannii
179	5	2	8	2	2	1	4		A. baumannii
180	6	6	8	2	30	5	4		A. baumannii
181	3	3	2	2	30	1	3		A. baumannii
182	6	3	8	2	30	5	4		A. baumannii
183	2	23	2	2	2	2	2		
184	43	2	2	2	2	2	2		A. baumannii
185	2	2	2	2	2	2	42		A. baumannii
186	3	3	6	2	30	1	5		A. baumannii
187	2	2	2	2	2	2	43		A. baumannii
188	1	3	6	1	3	4	4		A. baumannii
189	3	2	2	1	2	4	8		A. baumannii
190	1	2	2	2	11	4	5		A. baumannii
191	6	35	8	1	5	5	36		A. baumannii
192	5	35	39	2	3	1	5		A. baumannii
193	3	1	7	1	7	2	4		A. baumannii
194	3	1	15	1	5	1	1		A. baumannii
195	2	2	2	2	2	1	2		A. baumannii
196	2	2	13	2	2	1	2		A. baumannii
197	3	3	3	4	39	4	4		A. baumannii
198	18	22	42	11	21	14	21		13BJ
199	18	22	42	11	21	14	24		13BJ
200	21	25	24	28	46	17	24		13BJ
201	21	25	42	15	24	17	24		13BJ
202	1	4	1	1	5	1	1		A. baumannii
203	3	4	2	2	7	1	2		A. baumannii
204	22	26	47	18	27	16	47		A. nosocomialis
205	23	20	23	16	25	18	26		A. pittii
206	44	20	43	10	47	18	45		A. pittii
207	45	20	44	16	25	29	20		A. pittii
208	17	20	45	10	20	13	20		A. pittii
209	36	20	48	16	25	18	20		A. pittii
210	17	20	23	10	20	18	44		A. pittii
211	24	45	46	29	48	30	46		A. pittii
212	1	1	2	2	3	1	2		A. baumannii
213	3	3	7	1	7	1	4		A. baumannii
214	23	20	28	10	25	18	26		A. pittii
215	27	2	7	2	2	1	2		A. baumannii
216	1	4	2	2	7	1	2		A. baumannii
217	20	24	26	14	23	19	23		A. nosocomialis
218	1	5	40	2	7	1	1		A. baumannii
219	1	5	7	1	7	2	4		A. baumannii
220	45	20	44	16	20	29	20		A. pittii
221	3	1	2	1	18	1	48		A. baumannii
222	46	1	2	6	5	4	4		A. baumannii
223	22	46	49	14	49	16	23		A. nosocomialis
224	47	47	50	14	26	16	49		A. nosocomialis
225	48	20	23	16	25	18	20		A. pittii
226	49	26	49	18	27	19	50		A. nosocomialis
227	45	20	44	2	25	29	20		
228	40	3	2	4	7	2	4		A. baumannii
229	3	3	51	2	28	1	3		A. baumannii
230	1	6	1	1	5	1	1		A. baumannii
231	1	1	1	1	5	1	4		A. baumannii
232	6	6	2	2	3	5	4		A. baumannii
233	1	1	8	1	5	1	1		A. baumannii
234	1	3	1	1	4	24	2		A. baumannii
235	3	5	7	1	7	1	2		A. baumannii
236	3	2	7	26	7	1	4		A. baumannii
237	3	5	7	26	7	1	4		A. baumannii
238	6	3	8	2	3	5	4		A. baumannii
239	1	4	2	2	7	1	4		A. baumannii
240	3	3	2	5	7	2	51		A. baumannii
241	40	3	15	2	40	4	4		A. baumannii
242	1	48	40	2	7	4	9		A. baumannii
243	3	3	2	2	9	2	4		A. baumannii
244	8	1	5	3	7	1	16		A. baumannii
245	3	2	2	2	4	1	4		A. baumannii
246	1	49	3	4	5	2	36		A. baumannii
247	2	2	2	2	2	31	2		A. baumannii
248	17	21	23	10	20	18	27		A. pittii
249	48	20	23	16	25	18	26		A. pittii
250	50	3	6	1	3	4	4		A. baumannii
251	33	33	34	23	35	18	34		A. seifertii
252	1	4	3	2	9	1	5		A. baumannii
253	3	3	13	1	4	4	14		A. baumannii
254	2	2	2	25	2	2	2		A. baumannii
255	3	37	2	2	42	1	14		A. baumannii
256	1	3	10	1	2	4	4		A. baumannii
257	2	9	2	2	2	2	2		A. baumannii
258	1	1	3	1	13	4	14		A. baumannii
259	26	2	2	2	2	4	5		A. baumannii
260	36	20	27	10	25	18	46		A. pittii
261	2	2	2	2	2	2	29		A. baumannii
262	1	1	2	2	13	1	2		A. baumannii
263	2	4	2	2	2	2	2		A. baumannii
264	3	2	6	1	3	1	4		A. baumannii
265	26	2	2	1	43	1	5		A. baumannii
266	27	2	2	2	7	1	5		A. baumannii
267	12	37	2	2	3	2	14		A. baumannii
268	3	2	2	2	3	1	5		A. baumannii
269	3	3	6	7	5	4	4		A. baumannii
270	1	3	2	2	9	2	14		A. baumannii
271	3	3	2	2	29	4	14		A. baumannii
272	1	3	50	2	29	4	5		A. baumannii
273	3	4	7	26	7	1	4		A. baumannii
274	40	2	2	2	9	1	36		A. baumannii
275	40	3	11	2	5	1	8		A. baumannii
276	5	3	2	2	9	1	2		A. baumannii
277	3	3	16	2	13	1	15		A. baumannii
278	51	3	2	5	4	4	14		A. baumannii
279	22	26	47	14	50	16	47		A. nosocomialis
280	6	1	2	4	51	4	5		A. baumannii
281	1	51	6	2	29	4	52		A. baumannii
282	3	3	2	6	52	2	14		A. baumannii
283	3	50	3	5	40	4	5		A. baumannii
284	3	5	2	1	7	1	4		A. baumannii
285	1	52	2	2	9	4	2		A. baumannii
286	3	2	2	2	28	1	29		A. baumannii
287	11	3	2	4	13	25	2		A. baumannii
288	25	3	7	2	4	4	3		A. baumannii
289	1	16	2	2	9	32	5		A. baumannii
290	12	3	2	2	53	4	29		A. baumannii
291	1	53	7	2	3	33	53		A. baumannii
292	1	3	2	1	3	34	4		A. baumannii
293	12	3	2	2	8	2	4		A. baumannii
294	40	3	2	2	4	35	4		A. baumannii
295	3	3	52	2	54	1	6		A. baumannii
296	1	3	2	2	9	1	54		A. baumannii
297	42	30	41	19	9	28	22		
298	1	2	2	2	29	4	5		A. baumannii
299	5	1	2	2	2	4	8		A. baumannii
300	3	3	2	4	3	2	4		A. baumannii
301	20	2	2	2	2	4	8		A. baumannii
302	6	1	1	1	9	1	41		A. baumannii
303	50	3	2	2	3	4	4		A. baumannii
304	3	3	2	4	29	2	4		A. baumannii
305	6	2	8	2	3	5	4		A. baumannii
306	20	26	26	14	3	16	40		
307	3	3	2	4	7	2	30		A. baumannii
308	3	1	6	2	5	1	5		A. baumannii
309	12	1	2	2	9	1	5		A. baumannii
310	1	54	1	1	5	1	1		A. baumannii
311	3	1	2	1	11	2	4		A. baumannii
312	52	55	53	16	55	36	55		A. pittii
313	53	26	47	14	27	16	47		A. nosocomialis
314	25	1	18	1	56	2	14		A. baumannii
315	1	56	1	1	5	1	1		A. baumannii
316	3	1	6	2	4	1	5		A. baumannii
317	3	1	15	2	40	4	4		A. baumannii
318	6	6	8	2	3	5	5		A. baumannii
319	3	1	2	2	7	1	5		A. baumannii
320	54	57	38	16	57	18	20		A. pittii
321	45	58	44	10	20	18	56		A. pittii
322	55	26	54	14	58	16	47		A. nosocomialis
323	56	3	55	2	5	1	14		A. baumannii
324	3	3	2	4	2	2	2		A. baumannii
325	1	2	2	1	5	1	5		A. baumannii
326	3	3	16	25	5	6	1		A. baumannii
327	1	15	2	5	11	1	14		A. baumannii
328	1	1	1	25	5	1	2		A. baumannii
329	26	4	2	2	9	2	2		A. baumannii
330	1	6	8	2	3	5	4		A. baumannii
331	3	2	2	2	7	2	5		A. baumannii
332	1	4	2	2	3	1	2		A. baumannii
333	3	2	2	1	29	1	4		A. baumannii
334	3	1	14	3	12	1	13		A. baumannii
335	40	1	2	2	3	4	4		A. baumannii
336	27	2	2	2	7	2	5		A. baumannii
337	40	2	2	1	3	2	52		A. baumannii
338	8	5	5	26	13	1	2		A. baumannii
339	8	59	5	5	6	2	3		A. baumannii
340	57	3	2	2	9	2	4		A. baumannii
341	3	3	56	2	54	1	3		A. baumannii
342	41	60	13	1	5	4	14		A. baumannii
343	3	1	2	2	2	2	4		A. baumannii
344	2	2	1	1	2	2	2		A. baumannii
345	26	4	2	2	9	2	5		A. baumannii
346	1	2	3	2	9	4	5		A. baumannii
347	1	2	3	2	59	4	5		A. baumannii
348	3	3	2	2	29	27	5		A. baumannii
349	3	3	7	2	13	1	15		A. baumannii
350	3	3	2	2	5	2	5		A. baumannii
351	26	61	2	2	7	1	5		A. baumannii
352	3	2	7	26	60	1	4		A. baumannii
353	1	2	3	2	59	4	57		A. baumannii
354	3	2	2	2	7	1	5		A. baumannii
355	22	26	26	14	61	16	23		A. nosocomialis
356	1	53	3	2	62	1	29		A. baumannii
357	3	4	2	2	7	2	5		A. baumannii
358	3	3	14	26	7	1	4		A. baumannii
359	20	24	26	14	26	16	47		A. nosocomialis
360	1	4	2	1	42	1	4		A. baumannii
361	3	4	2	1	42	1	4		A. baumannii
362	27	2	2	2	29	2	5		A. baumannii
363	1	2	2	2	15	4	5		A. baumannii
364	1	4	2	1	42	1	5		A. baumannii
365	1	3	2	2	7	4	5		A. baumannii
366	1	2	1	1	29	29	5		
367	1	2	14	3	12	1	2		A. baumannii
368	1	62	3	2	40	1	4		A. baumannii
369	3	2	7	2	13	1	15		A. baumannii
370	1	4	3	2	9	1	14		A. baumannii
371	27	2	7	2	5	1	14		A. baumannii
372	1	4	2	1	42	1	2		A. baumannii
373	3	2	2	5	5	1	4		A. baumannii
374	3	2	2	2	3	4	4		A. baumannii
375	8	2	2	3	9	2	4		A. baumannii
376	27	4	2	1	42	1	2		A. baumannii
377	1	2	2	2	3	1	5		A. baumannii
378	2	5	5	1	7	1	4		A. baumannii
379	3	2	2	2	2	1	2		A. baumannii
380	2	2	2	2	4	2	2		A. baumannii
381	1	53	3	1	13	4	4		A. baumannii
382	1	4	2	2	7	1	5		A. baumannii
383	27	7	2	2	7	2	5		A. baumannii
384	13	5	40	1	42	1	2		A. baumannii
385	1	2	4	2	5	1	14		A. baumannii
386	3	2	2	30	3	8	3		A. baumannii
387	3	63	7	2	29	1	5		A. baumannii
388	1	62	3	2	40	4	4		A. baumannii
389	2	64	2	2	2	2	2		A. baumannii
390	45	58	57	10	20	18	20		A. pittii
391	2	2	58	2	2	2	2		A. baumannii
392	1	65	6	2	63	1	4		A. baumannii
393	2	2	2	31	2	2	2		A. baumannii
394	58	58	46	29	64	18	58		A. pittii
395	59	26	59	14	23	16	47		A. nosocomialis
396	60	21	46	10	20	18	20		A. pittii
397	62	48	2	2	3	1	5		A. baumannii
398	61	66	60	32	35	23	34		A. seifertii
399	1	62	3	2	40	4	5		A. baumannii
400	3	3	55	2	66	1	5		A. baumannii
401	55	3	54	2	58	16	5		
402	3	3	2	1	7	2	4		A. baumannii
403	3	2	6	1	3	4	59		A. baumannii
404	3	49	61	2	5	2	4		A. baumannii
405	5	3	16	4	29	1	60		A. baumannii
406	1	1	1	2	65	1	5		A. baumannii
407	56	3	55	2	5	4	14		A. baumannii
408	1	1	1	1	7	1	1		A. baumannii
409	1	1	1	1	2	1	1		A. baumannii
410	20	26	26	14	26	16	23		A. nosocomialis
411	64	52	7	2	29	4	29		A. baumannii
412	1	52	2	2	67	4	5		A. baumannii
413	1	3	2	2	5	8	12		A. baumannii
414	2	2	2	2	2	37	2		A. baumannii
415	2	2	2	2	68	2	2		A. baumannii
416	1	2	2	2	4	1	4		A. baumannii
417	1	2	2	2	11	1	5		A. baumannii
418	56	3	2	2	5	4	14		A. baumannii
419	3	71	2	2	5	4	14		A. baumannii
420	10	4	3	2	5	1	2		A. baumannii
421	3	2	2	7	5	1	5		A. baumannii
422	26	72	2	2	29	4	5		A. baumannii
423	3	2	2	7	5	4	5		A. baumannii
424	3	1	7	1	7	1	4		A. baumannii
425	3	3	63	6	4	9	1		A. baumannii
426	3	4	2	2	5	1	2		A. baumannii
427	13	3	2	3	6	1	16		A. baumannii
428	3	1	2	3	6	1	16		A. baumannii
429	3	74	2	3	6	1	16		
430	1	75	2	2	5	1	2		A. baumannii
431	1	4	2	1	70	1	2		A. baumannii
432	65	73	62	33	69	38	61		A. calcoaceticus
433	22	26	29	14	27	16	47		A. nosocomialis
434	33	26	34	14	27	16	47		
435	1	26	34	14	27	16	47		
436	1	26	34	14	1	16	47		
437	3	2	2	2	30	4	28		A. baumannii
438	3	2	2	7	9	4	5		A. baumannii
439	1	3	2	1	3	1	5		A. baumannii
440	13	40	2	3	7	1	16		A. baumannii
441	3	5	7	1	12	1	2		A. baumannii
442	3	3	2	2	71	1	5		A. baumannii
443	3	67	2	2	13	2	4		A. baumannii
444	39	2	2	2	4	4	4		A. baumannii
445	13	5	7	1	7	1	4		A. baumannii
446	8	1	5	26	6	1	3		A. baumannii
447	3	68	5	2	29	4	29		A. baumannii
448	27	4	7	1	7	1	4		A. baumannii
449	63	2	2	34	5	1	14		A. baumannii
450	37	1	5	3	12	2	3		A. baumannii
451	3	69	64	2	9	2	2		A. baumannii
452	7	2	2	1	8	4	4		A. baumannii
453	3	70	2	1	9	2	5		A. baumannii
454	3	2	2	2	3	1	6		A. baumannii
455	27	3	2	5	7	2	51		A. baumannii
456	27	5	7	1	7	1	2		A. baumannii
457	66	20	48	35	72	18	62		A. pittii
458	40	3	56	2	73	1	63		A. baumannii
459	3	5	65	1	7	1	4		A. baumannii
460	1	1	1	1	5	1	64		A. baumannii
461	67	2	6	2	74	2	5		A. baumannii
462	3	3	2	2	5	4	14		A. baumannii
463	68	76	66	36	72	30	65		A. pittii
464	5	2	4	1	3	4	4		A. baumannii
465	1	3	67	2	29	6	5		A. baumannii
466	69	3	2	2	3	1	10		A. baumannii
467	3	1	68	2	13	1	2		A. baumannii
468	3	67	2	1	75	1	5		A. baumannii
469	1	3	15	2	9	2	5		A. baumannii
470	3	3	13	1	9	1	4		A. baumannii
471	1	3	13	2	2	1	4		A. baumannii
472	1	3	2	4	3	1	5		A. baumannii
473	3	77	3	5	18	1	14		A. baumannii
474	3	78	2	2	73	4	14		A. baumannii
475	22	3	15	2	76	4	4		A. baumannii
476	1	78	2	2	73	1	5		A. baumannii
477	26	2	6	2	5	1	52		A. baumannii
478	3	2	2	5	4	2	3		A. baumannii
479	3	3	11	2	44	4	8		A. baumannii
480	5	3	2	2	9	4	14		A. baumannii
481	1	2	2	2	5	1	5		A. baumannii
482	1	1	2	2	7	2	5		A. baumannii
483	71	79	34	23	77	23	66		A. seifertii
484	15	80	69	8	19	10	19		A. calcoaceticus
485	72	20	46	16	20	39	65		A. pittii
486	3	2	2	2	39	13	4		
487	2	2	1	2	2	2	2		A. baumannii
488	6	6	8	2	10	2	3		A. baumannii
489	2	2	2	2	2	8	2		A. baumannii
490	1	4	3	2	9	1	2		A. baumannii
491	3	3	2	4	2	2	4		A. baumannii
492	2	3	2	2	2	2	2		A. baumannii
493	1	2	1	1	5	1	2		A. baumannii
494	3	3	2	5	4	1	4		A. baumannii
495	1	2	2	1	5	1	14		A. baumannii
496	1	3	52	6	2	8	44		A. baumannii
497	13	1	2	3	6	1	16		A. baumannii
498	27	3	2	3	6	1	16		A. baumannii
499	5	2	39	2	3	1	5		A. baumannii
500	3	3	2	2	28	1	5		A. baumannii
501	22	26	47	14	50	16	25		A. nosocomialis
502	20	26	26	14	23	16	23		A. nosocomialis
503	27	4	56	2	7	1	4		A. baumannii
504	3	3	6	1	29	4	52		A. baumannii
505	13	1	7	3	6	1	16		A. baumannii
506	3	4	16	1	3	1	4		A. baumannii
507	40	1	6	2	7	1	2		A. baumannii
508	12	77	7	2	15	4	5		A. baumannii
509	1	1	7	5	3	1	16		A. baumannii
510	3	53	56	2	9	8	2		A. baumannii
511	1	1	1	2	71	1	5		A. baumannii
512	3	37	3	2	4	1	9		A. baumannii
513	56	3	55	2	9	4	14		A. baumannii
514	1	2	2	2	4	1	5		A. baumannii
515	56	3	2	2	9	4	14		A. baumannii
516	3	4	2	2	9	1	2		A. baumannii
517	66	21	48	35	26	18	62		
518	5	2	2	2	2	2	5		A. baumannii
519	3	2	2	1	9	4	14		A. baumannii
520	1	2	2	2	30	1	2		A. baumannii
521	3	88	2	2	28	1	5		A. baumannii
522	3	3	89	2	28	1	5		A. baumannii
523	2	2	2	2	99	2	2		A. baumannii
524	2	97	2	2	2	2	2		A. baumannii
525	2	2	2	2	2	50	2		A. baumannii
526	2	2	2	2	100	2	2		A. baumannii
527	1	2	2	2	4	51	4		A. baumannii
528	5	98	4	1	3	4	4		A. baumannii
529	3	3	7	52	7	1	4		A. baumannii
530	20	26	90	14	26	16	47		A. nosocomialis
531	22	26	91	14	23	19	47		A. nosocomialis
532	3	2	2	53	11	1	5		A. baumannii
533	13	1	7	3	101	1	16		A. baumannii
534	3	3	2	2	102	4	4		A. baumannii
535	3	3	6	2	103	4	4		A. baumannii
536	3	3	11	54	5	1	2		A. baumannii
537	95	52	2	2	4	4	4		A. baumannii
538	31	32	92	22	34	22	33		
539	88	96	87	51	93	42	83		A. calcoaceticus
540	96	91	85	48	105	54	89		A. calcoaceticus
541	80	99	76	43	19	10	19		A. calcoaceticus
542	23	92	86	10	72	18	90		A. pittii
543	59	26	26	18	27	16	91		A. nosocomialis
544	83	86	34	23	88	23	77		A. seifertii
545	1	86	79	46	88	23	77		A. seifertii
546	75	34	34	23	79	23	69		A. seifertii
547	1	1	2	1	4	4	4		A. baumannii
548	76	33	34	23	80	18	70		A. seifertii
549	84	33	34	23	79	23	82		A. seifertii
550	89	66	34	49	94	23	84		A. seifertii
551	90	89	82	23	95	23	85		A. seifertii
552	91	34	34	23	96	23	86		A. seifertii
553	83	86	79	46	88	23	77		A. seifertii
554	61	33	60	23	89	23	78		A. seifertii
555	84	33	34	23	35	47	79		A. seifertii
556	73	81	70	37	78	40	67		A. calcoaceticus
557	74	82	71	38	33	22	68		
558	79	31	74	41	83	43	73		
559	29	31	75	42	84	21	73		
560	78	94	71	38	82	22	72		
561	82	85	78	45	87	46	76		A. calcoaceticus
562	85	87	80	47	90	48	80		A. calcoaceticus
563	77	20	72	39	81	41	71		A. pittii
564	94	95	88	50	85	44	87		A. dijkshoorniae
565	92	55	83	50	97	45	87		A. dijkshoorniae
566	93	90	84	50	98	44	88		A. dijkshoorniae
567	87	84	73	44	92	41	75		
568	81	93	77	40	86	44	74		A. dijkshoorniae
569	86	55	81	16	91	49	81		A. pittii
570	2	2	2	2	2	2	4		A. baumannii
571	2	2	2	2	104	2	4		A. baumannii
572	1	2	2	2	104	2	4		A. baumannii
573	97	2	2	2	104	2	4		A. baumannii
574	27	2	2	2	104	2	4		A. baumannii
575	1	3	2	1	4	4	92		A. baumannii
576	2	2	2	2	2	2	92		A. baumannii
577	27	2	7	2	2	2	2		A. baumannii
578	97	3	13	1	4	4	14		A. baumannii
579	2	3	2	2	2	4	2		A. baumannii
580	2	2	2	2	2	52	2		A. baumannii
581	1	3	2	2	4	6	93		A. baumannii
582	3	2	2	2	54	53	4		A. baumannii
583	1	54	10	5	75	1	5		A. baumannii
584	7	3	2	1	8	4	4		A. baumannii
585	3	1	2	4	5	1	5		A. baumannii
586	1	3	2	1	4	1	4		A. baumannii
587	1	2	7	5	7	4	2		A. baumannii
588	3	3	2	2	7	2	2		A. baumannii
589	1	1	2	1	9	1	1		A. baumannii
590	1	1	2	2	5	1	2		A. baumannii
591	1	1	2	1	5	2	2		A. baumannii
592	2	2	1	1	5	1	1		A. baumannii
593	2	2	2	4	2	2	4		A. baumannii
594	2	2	1	1	5	1	2		A. baumannii
595	1	1	2	1	2	2	2		A. baumannii
596	1	1	2	2	2	2	2		A. baumannii
597	2	2	2	2	7	2	2		A. baumannii
598	2	2	1	2	5	1	1		A. baumannii
599	2	2	1	1	5	2	1		A. baumannii
600	2	2	2	2	2	2	1		A. baumannii
601	2	2	2	1	5	1	1		A. baumannii
602	12	100	2	2	29	1	4		A. baumannii
603	2	2	93	2	2	2	94		A. baumannii
604	2	2	2	55	2	2	2		A. baumannii
605	1	3	10	1	4	55	2		A. baumannii
606	94	55	77	50	106	44	88		A. dijkshoorniae
607	3	49	2	1	5	4	5		A. baumannii
608	3	53	16	2	13	1	15		A. baumannii
609	4	1	13	1	4	4	14		A. baumannii
610	40	1	7	2	40	4	4		A. baumannii
611	3	41	6	2	3	4	5		A. baumannii
612	3	3	3	4	7	9	4		A. baumannii
613	1	3	10	1	4	55	4		A. baumannii
614	5	2	2	2	3	4	4		A. baumannii
615	41	42	13	1	2	4	14		A. baumannii
616	5	42	2	1	5	1	14		A. baumannii
617	3	2	2	5	9	4	5		A. baumannii
618	1	42	13	1	5	4	14		A. baumannii
619	3	3	2	4	7	2	2		A. baumannii
620	12	3	94	2	5	1	5		A. baumannii
621	1	63	2	2	9	4	3		A. baumannii
622	3	12	11	2	14	4	14		A. baumannii
623	1	1	2	1	5	1	1		A. baumannii
624	3	2	2	1	107	4	14		A. baumannii
625	56	3	55	2	9	1	14		A. baumannii
626	26	3	2	2	18	4	2		A. baumannii
627	3	6	2	4	7	2	4		A. baumannii
628	3	3	7	56	7	1	5		A. baumannii
629	98	20	46	16	20	18	62		A. pittii
630	3	3	2	4	108	2	4		A. baumannii
631	3	6	2	2	109	2	95		A. baumannii
632	2	2	2	2	2	2	96		A. baumannii
633	2	101	2	2	2	2	2		A. baumannii
634	6	1	8	2	3	5	4		A. baumannii
635	99	102	95	57	110	56	97		
636	2	1	2	2	2	1	1		A. baumannii
637	1	1	10	1	6	1	1		A. baumannii
638	100	3	14	1	7	1	4		
639	3	3	2	2	11	57	4		A. baumannii
640	66	20	48	35	72	18	20		A. pittii
641	2	1	2	2	2	2	2		A. baumannii
642	1	1	1	1	9	1	1		A. baumannii
643	45	58	44	10	20	18	20		A. pittii
644	50	3	6	1	3	4	30		A. baumannii
645	2	103	2	2	2	2	2		A. baumannii
646	1	1	96	1	5	1	2		A. baumannii
647	3	3	6	2	51	1	29		A. baumannii
648	1	3	11	5	111	1	14		A. baumannii
649	27	3	2	2	5	58	5		A. baumannii
650	1	104	2	2	4	1	4		A. baumannii
651	3	67	2	2	102	4	4		A. baumannii
652	40	1	6	2	102	1	2		A. baumannii
653	3	5	5	26	13	1	2		A. baumannii
654	3	1	5	3	29	2	3		A. baumannii
655	101	20	97	10	72	18	98		A. pittii
656	1	2	2	2	11	1	99		A. baumannii
657	102	2	98	2	11	1	5		A. baumannii
658	1	105	2	2	11	1	5		A. baumannii
659	1	2	2	2	112	1	4		A. baumannii
660	1	2	99	2	11	1	5		A. baumannii
661	2	106	2	2	2	2	2		A. baumannii
662	2	2	2	58	2	2	2		A. baumannii
663	2	2	8	2	2	2	2		A. baumannii
664	2	2	2	2	2	4	2		A. baumannii
665	1	75	2	2	67	1	2		A. baumannii
666	45	20	44	10	25	29	20		A. pittii
667	23	20	28	10	25	18	20		A. pittii
668	2	2	100	2	2	2	2		A. baumannii
669	5	2	101	2	2	2	5		A. baumannii
670	2	2	102	2	2	2	2		A. baumannii
671	2	2	2	2	113	2	2		A. baumannii
672	2	107	2	2	2	2	2		A. baumannii
673	103	2	103	2	2	2	2		A. baumannii
674	2	2	2	2	114	2	2		A. baumannii
675	104	108	104	10	72	59	100		A. pittii
676	25	109	6	2	28	1	29		A. baumannii
677	1	2	2	2	115	1	5		A. baumannii
678	2	2	2	2	22	2	2		A. baumannii
679	23	60	28	10	25	2	26		A. baumannii
680	36	20	48	16	25	2	20		A. baumannii
681	48	20	23	16	25	2	20		A. baumannii
682	1	48	40	2	7	2	2		A. baumannii
683	23	20	23	16	25	2	20		A. baumannii
684	27	4	2	2	2	2	2		A. baumannii
685	2	62	3	2	40	4	4		A. baumannii
686	6	100	5	6	9	1	4		A. baumannii
687	1	3	2	2	9	1	10		A. baumannii
688	3	5	5	1	7	1	16		A. baumannii
689	1	3	2	2	3	1	5		A. baumannii
690	3	3	2	1	7	2	14		A. baumannii
691	23	20	28	10	25	18	44		A. pittii
692	1	1	7	1	7	1	4		A. baumannii
693	1	4	2	1	42	2	5		A. baumannii
694	3	50	2	2	3	1	4		A. baumannii
695	1	3	2	2	3	4	2		A. baumannii
696	3	1	2	2	4	4	5		A. baumannii
697	3	2	2	2	2	2	2		A. baumannii
698	69	1	1	1	13	1	2		
699	103	2	2	2	2	2	2		
700	2	2	2	2	100	2	1		
701	12	51	2	2	13	4	2		
702	3	1	7	1	7	1	2		
703	103	2	2	2	68	2	2		
704	1	2	1	1	13	4	2		
705	103	1	7	2	2	2	2		
706	2	2	2	6	2	2	1		
707	5	2	2	6	68	2	4		
708	5	2	4	1	30	3	2		
709	103	2	2	2	68	2	4		
710	103	2	2	2	100	2	2		
711	2	1	2	2	100	1	2		
712	103	2	2	2	2	2	4		
713	2	2	2	2	2	2	52		
714	103	1	2	2	2	1	2		
715	2	1	2	2	2	1	4		
716	103	2	2	2	2	2	1		
717	1	1	1	1	5	1	30		A. baumannii
718	1	2	1	1	5	1	30		A. baumannii
719	3	2	2	2	3	2	4		A. baumannii
720	13	4	40	2	7	1	2		A. baumannii
721	35	4	11	7	9	1	2		A. baumannii
722	13	4	2	3	7	1	16		A. baumannii
723	3	2	2	2	7	4	6		A. baumannii
724	2	2	2	2	2	2	5		A. baumannii
725	27	3	2	2	9	2	5		A. baumannii
726	13	4	2	1	42	2	2		A. baumannii
727	1	3	14	3	12	1	2		A. baumannii
728	25	3	2	2	5	4	5		
729	3	3	2	2	3	1	4		A. baumannii
730	26	6	2	2	29	4	5		A. baumannii
731	34	3	37	1	29	6	25		
732	3	35	2	4	7	2	4		
733	7	1	2	1	8	4	36		
734	1	1	1	1	3	1	1		
735	3	3	3	3	7	3	2		A. baumannii
736	1	3	1	1	5	1	1		A. baumannii
737	6	6	8	6	3	5	4		A. baumannii
738	3	3	105	6	4	2	5		
739	8	1	5	1	29	2	3		
740	26	4	2	2	9	1	2		
741	26	2	2	2	2	1	4		
742	3	5	2	5	7	1	52		
743	50	3	2	1	3	4	4		
744	17	21	23	10	20	18	20		
745	2	2	2	2	2	2	101		
746	17	20	23	10	20	13	44		
747	36	20	28	10	25	18	26		
748	107	110	106	60	117	60	102		
749	109	112	108	62	119	61	103		
750	110	113	109	62	120	61	104		
751	108	111	107	61	118	61	102		
752	111	102	110	63	121	56	97		
753	3	3	101	59	4	4	2		
754	26	3	2	52	4	1	4		A. baumannii
755	1	2	2	1	11	2	60		A. baumannii
756	12	1	7	1	7	2	29		A. baumannii
757	3	3	13	2	7	4	5		A. baumannii
758	1	3	2	1	42	2	2		
759	3	2	2	5	5	4	5		
760	3	1	2	1	7	2	4		
761	27	2	5	2	7	2	5		
762	3	3	2	2	109	2	95		
763	3	4	2	2	9	1	5		
764	3	3	2	2	4	1	5		
765	3	2	2	2	6	4	5		
766	3	3	2	2	29	1	4		
767	1	4	2	2	7	2	4		
768	22	26	91	18	23	19	47		
769	1	3	2	5	52	4	4		
770	1	4	2	2	7	2	2		
771	1	4	2	2	5	1	2		
772	34	2	6	2	51	1	105		
773	7	114	2	1	7	1	4		
774	1	115	6	2	3	4	4		
775	25	16	18	1	122	4	14		
776	106	20	48	10	116	18	65		
777	24	20	46	10	123	18	107		A. pittii
778	112	21	111	36	20	18	106		A. pittii
779	113	116	112	64	124	18	108		A. pittii
780	3	3	51	2	28	1	109		A. baumannii
781	20	26	26	14	26	16	47		
782	22	26	47	14	27	16	47		
783	17	21	23	36	20	13	46		
784	20	26	26	14	26	16	49		
785	22	26	91	14	125	16	118		
786	20	117	115	14	126	68	117		
787	123	26	49	14	133	16	23		
788	125	20	113	10	20	18	119		
789	23	20	23	67	25	18	20		
790	115	118	116	36	127	18	46		
791	104	21	117	16	72	65	62		
792	116	55	118	66	128	64	114		
793	117	55	53	66	128	64	110		
794	101	119	120	67	20	66	115		
795	101	20	46	10	129	18	116		
796	94	120	88	50	98	44	88		A. dijkshoorniae
797	118	121	84	50	130	44	88		A. dijkshoorniae
798	119	122	121	50	86	44	113		A. dijkshoorniae
799	120	123	88	50	25	67	87		A. dijkshoorniae
800	121	121	122	50	131	45	87		A. dijkshoorniae
801	92	123	114	50	132	41	112		A. dijkshoorniae
802	122	124	123	50	130	63	88		A. dijkshoorniae
803	124	89	82	23	134	62	34		
804	106	20	119	65	136	36	111		
805	114	118	116	10	123	18	120		A. pittii
806	3	3	2	2	3	4	5		A. baumannii
807	56	56	55	2	9	4	14		
808	1	3	2	1	18	8	5		
809	1	3	5	2	11	1	2		
810	3	51	2	2	5	4	52		
811	3	2	6	5	9	2	5		
812	40	3	2	2	4	2	14		
813	3	3	11	2	9	9	8		
814	3	2	6	2	74	2	5		
815	3	3	2	3	15	2	2		
816	6	53	7	2	3	1	4		
817	1	2	6	2	13	8	52		
818	11	50	18	2	9	1	5		
819	3	1	2	2	4	2	14		
820	3	49	2	2	9	4	4		
821	12	100	2	2	9	1	52		
822	3	2	6	2	74	4	5		
823	2	125	2	2	2	2	2		
824	1	2	2	1	42	1	16		
825	3	2	2	2	7	4	4		
826	1	1	1	1	5	8	1		
827	23	20	23	16	25	18	44		A. pittii
828	3	3	2	2	135	8	12		
829	1	56	124	1	5	1	1		
830	41	6	56	5	8	69	8		
831	40	1	2	2	137	35	4		
832	125	76	46	67	20	66	20		
833	45	58	44	10	20	18	116		
834	33	33	34	23	80	18	70		
835	34	29	37	1	5	6	36		
836	26	2	2	1	29	4	5		
837	13	4	2	3	6	1	16		
838	145	55	121	40	149	44	87		
839	141	21	46	10	20	18	20		A. pittii
840	141	21	46	10	20	18	131		A. pittii
841	3	1	3	2	4	1	9		A. baumannii
842	45	58	44	10	20	18	62		A. nosocomialis
843	5	77	7	2	3	4	14		A. baumannii
844	3	1	6	2	26	1	5		A. baumannii
845	143	137	134	2	7	4	4		A. baumannii
846	144	138	135	23	148	23	132		A. seifertii
847	27	2	2	73	5	4	14		12770
848	13	3	2	3	7	1	16		A. baumannii
849	127	2	2	2	7	1	121		
850	129	126	119	16	127	49	114		
851	3	3	125	2	9	4	88		
852	130	21	44	68	72	18	20		
853	17	127	23	10	20	13	20		
854	93	55	126	50	138	71	88		
855	131	135	116	16	72	36	122		
856	52	55	127	69	139	49	123		
857	3	128	5	2	140	2	1		
858	12	1	128	2	9	1	5		
859	12	3	5	7	141	6	52		
860	133	129	129	70	142	72	76		
861	135	131	88	50	130	44	125		
862	12	3	5	7	141	2	52		
863	136	123	84	50	138	44	87		
864	115	118	130	29	123	18	46		
865	137	132	131	2	144	18	20		
866	3	2	2	30	3	74	3		A. baumannii
867	3	2	2	2	3	4	127		A. baumannii
868	140	134	132	16	25	18	20		
869	5	12	11	2	14	76	14		A. baumannii
870	136	55	84	50	130	44	87		
871	142	20	133	16	20	18	128		
872	94	123	88	50	147	44	129		
873	3	3	7	74	13	1	15		A. baumannii
874	6	115	2	2	29	4	5		A. baumannii
875	8	2	5	2	3	1	51		A. baumannii
876	1	37	2	2	73	4	5		A. baumannii
877	1	100	2	2	9	1	14		A. baumannii
878	3	16	136	2	3	4	29		A. baumannii
879	50	3	2	2	3	1	4		A. baumannii
880	2	2	2	2	2	77	2		A. baumannii
881	1	1	1	1	5	1	130		A. baumannii
882	22	136	47	14	50	16	47		A. nosocomialis
883	1	1	2	2	30	1	4		A. baumannii
884	3	1	2	1	18	4	48		A. baumannii
885	26	2	2	2	29	5	5		A. baumannii
886	6	35	2	1	9	5	36		A. baumannii
887	3	50	2	2	30	78	4		A. baumannii
888	12	37	2	2	30	2	14		A. baumannii
889	5	2	4	1	30	4	4		A. baumannii
890	6	6	8	2	30	5	1		A. baumannii
891	46	2	8	2	5	5	4		A. baumannii
892	6	6	8	2	30	5	133		A. baumannii
893	1	1	5	1	7	1	29		A. baumannii
894	10	3	11	7	9	1	2		A. baumannii
895	1	5	40	2	7	4	9		A. baumannii
896	137	132	137	2	144	18	20		A. pittii
897	50	2	2	2	3	4	4		A. baumannii
898	146	20	138	10	150	18	26		A. pittii
899	6	35	8	2	5	5	36		A. baumannii
900	1	1	14	3	12	1	121		A. baumannii
901	1	3	16	2	13	1	15		A. baumannii
902	1	1	1	1	13	1	1		A. baumannii
903	26	2	2	2	29	4	1		A. baumannii
904	6	6	8	2	2	5	4		A. baumannii
905	1	1	2	2	30	4	4		A. baumannii
906	109	112	106	62	119	61	102		A. ursingii
907	101	92	104	16	20	18	100		A. pittii
908	109	10	110	14	21	54	40		A. soli
909	109	10	24	14	21	54	40		A. soli
910	108	10	110	40	50	1	40		A. bereziniae
911	3	1	5	1	7	1	4		A. baumannii
912	3	2	2	5	7	4	14		
913	3	2	2	5	7	1	14		
914	1	2	2	2	2	1	5		
915	3	3	13	1	43	1	4		
916	1	2	7	1	7	4	2		
917	3	2	2	30	30	74	3		
918	50	3	2	2	30	4	4		
919	5	4	4	1	3	3	14		A. baumannii
920	1	3	2	2	13	1	8		A. baumannii
921	3	3	2	2	3	4	4		A. baumannii
922	2	2	2	75	2	2	2		A. baumannii
923	12	100	2	2	9	1	4		A. baumannii
924	3	4	2	2	7	1	5		A. baumannii
925	137	132	131	77	144	18	20		A. pittii
926	1	2	2	5	141	6	2		A. baumannii
927	1	3	2	2	2	4	29		A. baumannii
928	3	53	139	2	62	1	5		A. baumannii
929	1	1	2	5	141	6	2		A. baumannii
930	3	139	2	1	15	4	4		A. baumannii
931	3	1	2	1	4	4	134		A. baumannii
932	1	78	2	2	73	4	5		A. baumannii
933	1	3	10	1	3	1	14		A. baumannii
934	147	3	2	2	151	1	4		A. baumannii
935	3	16	2	5	4	2	135		A. baumannii
936	40	16	2	2	5	1	3		A. baumannii
937	3	3	6	2	9	1	4		A. baumannii
938	1	100	2	76	9	1	52		A. baumannii
939	3	2	56	2	8	1	136		A. baumannii
940	1	78	2	2	73	4	14		A. baumannii
941	1	3	55	2	40	4	5		A. baumannii
942	8	1	2	3	6	2	3		A. baumannii
943	1	5	15	5	9	1	4		A. baumannii
944	8	5	5	26	7	1	2		A. baumannii
945	3	3	2	4	7	4	4		A. baumannii
946	1	2	2	2	18	1	4		A. baumannii
947	104	20	46	35	72	18	108		A. pittii
948	22	26	47	14	26	16	23		A. nosocomialis
949	22	26	27	14	21	16	23		A. nosocomialis
950	149	141	112	36	152	59	139		A. pittii
951	26	20	2	1	43	4	137		A. baumannii
952	26	2	2	1	43	4	137		A. baumannii
953	12	37	128	2	3	2	14		A. baumannii
954	3	142	2	2	3	2	5		A. baumannii
955	1	52	2	2	9	4	4		A. baumannii
956	139	129	44	70	146	46	20		
957	26	2	2	2	29	53	5		A. baumannii
958	6	2	2	2	29	4	5		A. baumannii
959	1	2	2	1	2	1	5		A. baumannii
960	1	3	17	5	3	1	4		A. baumannii
961	1	3	101	2	4	4	4		A. baumannii
962	1	52	2	2	67	1	4		A. baumannii
963	1	52	2	2	67	5	5		A. baumannii
964	1	52	2	2	67	9	5		A. baumannii
965	3	2	2	2	30	4	47		A. baumannii
966	3	2	2	2	44	4	5		A. baumannii
967	3	2	2	6	4	4	14		A. baumannii
968	3	3	7	2	5	4	2		A. baumannii
969	3	3	55	2	9	1	14		A. baumannii
970	3	3	101	5	3	1	29		A. baumannii
971	3	52	2	2	67	4	4		A. baumannii
972	5	2	4	1	3	1	3		A. baumannii
973	5	4	4	1	3	4	14		A. baumannii
974	5	4	11	1	3	4	14		A. baumannii
975	5	12	2	2	14	9	14		A. baumannii
976	6	3	2	2	9	4	2		A. baumannii
977	8	2	2	2	17	1	5		A. baumannii
978	12	3	5	2	54	6	52		A. baumannii
979	27	4	2	2	7	1	5		A. baumannii
980	69	1	1	1	5	1	2		A. baumannii
981	6	6	8	2	2	25	4		A. baumannii
982	3	2	2	2	2	4	4		A. baumannii
983	1	1	1	1	5	1	5		A. baumannii
984	35	1	11	7	9	25	1		A. baumannii
985	26	2	2	2	29	25	2		A. baumannii
986	1	1	1	1	5	4	1		A. baumannii
987	3	2	2	2	5	4	8		A. baumannii
988	46	1	1	1	5	1	1		A. baumannii
989	5	2	2	2	2	4	4		A. baumannii
990	3	2	2	2	3	2	2		
991	3	3	2	4	7	2	5		A. baumannii
992	3	4	2	2	9	1	16		A. baumannii
993	177	163	160	62	117	90	102		A. ursingii
994	151	143	34	23	153	80	140		A. seifertii
995	152	1	7	1	7	2	4		A. baumannii
996	2	2	2	2	2	2	49		A. baumannii
997	2	2	2	2	2	2	44		A. baumannii
998	2	2	2	2	2	2	20		A. baumannii
999	2	2	2	2	2	2	97		A. baumannii
1000	1	3	2	1	3	1	46		A. baumannii
1001	2	2	2	2	3	1	2		A. baumannii
1002	3	3	3	4	7	4	49		A. baumannii
1003	2	2	2	2	2	2	51		A. baumannii
1004	2	2	2	2	2	2	63		A. baumannii
1005	3	2	2	2	2	2	5		A. baumannii
1006	3	2	2	2	3	4	2		A. baumannii
1007	3	3	2	5	7	2	44		A. baumannii
1008	3	1	2	2	3	2	4		A. baumannii
1009	2	2	2	2	2	2	3		A. baumannii
1010	1	4	2	2	7	1	29		A. baumannii
1011	3	5	5	1	7	1	26		A. baumannii
1012	1	3	40	2	7	1	4		A. baumannii
1013	3	2	11	2	44	4	4		
1014	3	3	2	2	9	1	2		
1015	3	16	2	5	137	2	135		
1016	3	3	2	2	9	1	4		
1017	3	3	2	2	9	1	5		
1018	8	1	2	1	5	1	4		
1019	1	3	2	2	9	4	14		
1020	3	3	2	2	5	4	8		
1021	1	3	2	2	3	2	29		
1022	3	52	6	2	8	4	4		
1023	25	3	7	1	4	4	3		
1024	3	3	2	1	4	1	1		
1025	3	3	11	2	29	4	4		
1026	27	3	6	2	29	4	29		
1027	27	3	6	2	29	4	4		
1028	3	3	2	2	8	1	8		
1029	12	49	2	6	9	1	4		
1030	12	1	6	2	9	1	52		
1031	1	5	2	5	7	1	5		
1032	5	100	11	2	14	9	14		
1033	27	3	6	2	29	4	2		
1034	3	16	2	5	4	2	4		
1035	1	3	2	2	9	1	5		
1036	3	3	2	2	5	1	4		
1037	3	49	2	1	5	7	5		
1038	3	5	2	5	7	1	5		
1039	6	1	3	2	5	2	5		
1040	51	3	3	2	65	4	143		
1041	156	2	5	2	9	1	2		
1042	3	5	141	2	4	83	4		
1043	3	52	6	2	8	85	4		
1044	3	3	6	1	29	4	29		
1045	1	78	2	2	73	6	141		
1046	157	3	2	2	9	4	14		
1047	1	16	144	2	9	2	5		
1048	3	16	145	5	5	1	29		
1049	3	63	3	1	154	82	1		
1050	153	3	2	2	9	1	5		
1051	155	3	6	2	4	1	5		
1052	154	2	11	7	9	1	2		
1053	51	52	140	2	4	4	2		
1054	3	1	143	3	13	1	2		
1055	3	3	2	1	151	1	4		
1056	3	3	2	2	155	4	5		
1057	25	3	2	2	156	4	5		
1058	3	3	2	1	157	4	8		
1059	1	3	2	2	158	4	14		
1060	3	144	56	2	5	1	142		
1061	6	78	2	2	73	4	141		
1062	3	144	56	1	5	1	142		
1063	148	12	11	2	14	9	14		
1064	159	145	34	78	160	87	144		A. seifertii
1065	3	3	2	4	7	1	4		
1066	3	2	148	5	51	8	14		
1067	161	2	2	2	2	2	2		
1068	51	1	140	2	4	4	2		A. baumannii
1069	1	3	142	2	2	4	4		A. baumannii
1070	160	3	6	2	29	4	4		A. baumannii
1071	3	2	147	1	3	1	5		A. baumannii
1072	27	3	7	2	161	84	14		A. baumannii
1073	157	3	11	2	5	1	2		A. baumannii
1074	1	2	39	2	39	1	5		A. baumannii
1075	20	26	26	14	26	19	25		A. nosocomialis
1076	158	20	146	16	159	18	100		A. pittii
1077	25	3	6	2	28	1	2		
1078	2	146	2	2	2	2	2		
1079	3	1	6	2	74	1	5		
1080	3	147	2	4	7	2	4		
1081	162	20	46	16	20	18	145		
1082	22	26	49	14	27	16	49		
1083	6	6	149	2	3	5	4		
1084	1	52	2	2	9	2	2		
1085	3	3	2	1	7	4	4		
1086	56	3	55	2	9	1	146		
1087	163	3	2	2	51	1	4		
1088	1	1	1	2	65	1	4		
1089	1	1	151	2	3	1	4		
1090	1	151	1	1	5	1	1		
1091	1	153	1	2	65	1	5		
1092	1	154	6	2	3	1	14		
1093	1	158	2	2	165	1	2		
1094	1	3	7	5	3	1	14		
1095	1	52	2	2	67	5	4		
1096	1	53	2	2	163	1	14		
1097	1	63	17	2	162	1	36		
1098	12	3	2	1	73	2	4		
1099	12	3	5	2	141	6	52		
1100	12	52	6	2	9	1	52		
1101	12	77	7	2	15	2	5		
1102	13	4	40	1	42	1	2		
1103	164	2	2	2	5	2	2		
1104	165	3	2	2	5	1	2		
1105	166	2	5	3	7	1	3		
1106	2	1	2	1	5	1	1		
1107	2	148	2	2	2	1	2		
1108	2	156	2	2	2	2	2		
1109	2	2	153	2	2	2	2		
1110	20	157	26	14	26	16	23		
1111	26	2	2	1	43	82	5		
1112	26	3	2	52	15	1	4		
1113	26	61	2	1	7	1	5		
1114	27	4	2	2	7	2	2		
1115	3	150	6	1	3	4	5		
1116	3	152	11	2	14	9	14		
1117	3	2	145	2	3	2	28		
1118	3	3	150	4	7	2	4		
1119	3	3	152	26	7	1	4		
1120	3	3	155	2	4	2	5		
1121	3	3	16	1	13	1	29		
1122	3	3	2	2	3	8	5		
1123	3	3	2	2	6	4	5		
1124	3	3	2	4	7	2	147		
1125	3	3	2	4	7	89	4		
1126	3	3	2	79	3	88	4		
1127	3	3	3	4	13	1	5		
1128	3	39	5	6	4	1	14		
1129	3	50	5	2	3	78	5		
1130	3	52	2	2	67	1	3		
1131	40	3	7	2	40	1	4		
1132	56	149	55	2	66	4	29		
1133	7	160	2	1	8	4	4		
1134	77	20	72	39	164	41	71		
1135	8	1	40	3	29	2	3		
1136	8	1	5	26	13	2	3		
1137	8	1	5	26	6	2	3		
1138	8	1	5	5	6	2	3		
1139	8	2	2	80	9	1	5		
1140	3	2	2	1	29	4	4		A. baumannii
1141	77	20	72	39	81	36	71		A. pittii
1142	34	4	37	1	5	6	36		A. baumannii
1143	6	2	8	2	2	2	2		A. baumannii
1144	1	1	2	1	3	4	1		A. baumannii
1145	34	35	37	1	107	6	36		A. baumannii
1146	3	2	1	7	9	1	5		A. baumannii
1147	3	52	2	2	9	1	4		A. baumannii
1148	3	3	2	1	169	1	2		A. baumannii
1149	3	1	2	2	170	4	5		A. baumannii
1150	1	155	2	2	73	4	5		A. baumannii
1151	3	159	6	2	8	4	4		A. baumannii
1152	35	3	2	2	9	1	5		A. baumannii
1153	8	3	10	1	4	2	4		A. baumannii
1154	2	2	2	2	2	2	148		
1155	167	26	54	14	167	16	23		
1156	1	3	2	2	5	58	29		A. baumannii
1157	152	4	7	1	7	1	4		A. baumannii
1158	3	4	2	2	3	1	2		A. baumannii
1159	1	2	2	2	5	4	14		A. baumannii
1160	2	161	2	2	2	2	2		A. baumannii
1161	168	51	2	2	13	4	4		A. baumannii
1162	169	2	2	2	171	1	4		A. baumannii
1163	26	2	2	2	29	4	2		A. baumannii
1164	112	119	28	16	144	81	115		
1165	3	67	154	2	11	1	8		
1166	22	26	29	14	172	16	47		
1167	170	20	46	81	72	18	116		
1168	1	62	156	2	40	4	4		
1169	36	20	38	16	38	18	44		
1170	45	162	138	10	20	18	56		
1171	36	20	157	16	38	18	20		
1172	17	20	46	10	20	13	20		
1173	17	21	158	10	20	13	20		
1174	60	21	46	10	20	13	20		
1175	171	92	28	10	72	18	20		
1176	172	20	23	10	25	18	20		
1177	94	55	88	50	130	44	149		
1178	17	20	159	10	20	29	44		
1179	3	3	2	1	166	2	14		
1180	5	2	39	2	168	1	5		A. baumannii
1181	59	26	26	14	58	16	47		
1182	22	165	161	14	27	19	25		
1183	20	164	26	14	26	16	23		
1184	175	33	34	23	35	23	152		Acinetobacter baumannii
1185	176	166	162	82	174	91	153		A. baylyi
1186	107	110	106	62	117	60	150		A. ursingii
1187	173	110	107	61	118	60	104		A. ursingii
1188	178	33	34	23	175	92	154		
1189	174	163	106	60	173	90	151		A. ursingii
1190	3	9	3	2	71	1	9		A. baumannii
1191	1	15	2	5	11	4	14		A. baumannii
1192	1	167	1	1	5	1	1		A. baumannii
1193	3	3	2	4	7	2	155		A. baumannii
1194	179	55	163	16	176	49	114		A. pittii
1195	27	2	2	2	5	4	8		
1196	26	2	2	2	29	4	29		
1197	1	4	2	2	7	58	2		A. baumannii
1198	56	2	55	2	9	4	14		A. baumannii
1199	1	2	2	2	63	1	29		A. baumannii
1200	3	53	3	2	51	1	9		
1201	157	2	56	2	5	7	5		
1202	4	2	2	2	2	2	2		
1203	94	2	2	50	2	44	2		
1204	103	2	2	59	2	2	2		
1205	103	160	2	74	2	89	136		
1206	17	20	23	2	20	18	1		A. pittii
1207	180	169	164	83	177	93	156		A. radioresistens
1208	1	168	1	1	5	1	1		A. baumannii
1209	2	1	2	1	5	1	2		A. baumannii
1210	8	2	2	7	17	1	57		A. baumannii
1211	1	2	2	2	73	4	5		A. baumannii
1212	3	3	6	2	4	4	14		A. baumannii
1213	182	173	72	39	178	41	71		
1214	1	1	1	1	5	95	1		
1215	15	171	20	43	19	10	157		
1216	183	172	165	43	179	96	83		
1217	3	3	1	1	5	1	1		
1218	3	3	2	4	15	2	4		
1219	3	1	1	1	7	1	1		
1220	12	3	5	2	9	1	14		
1221	3	1	1	4	5	1	1		
1222	3	16	94	2	4	2	4		A. baumannii
1223	13	5	40	1	42	1	16		A. baumannii
1224	1	1	7	1	7	2	1		A. baumannii
1225	3	3	6	2	74	2	5		A. baumannii
1226	12	3	6	2	5	1	3		A. baumannii
1227	1	175	2	2	13	4	2		A. baumannii
1228	25	3	2	2	4	4	4		A. baumannii
1229	155	177	6	2	4	1	5		A. baumannii
1230	3	2	148	1	51	1	5		A. baumannii
1231	3	3	168	5	3	1	14		A. baumannii
1232	40	49	6	1	102	1	2		
1233	3	2	167	2	115	1	4		
1234	132	20	169	16	72	97	159		
1235	1	3	2	1	137	24	137		
1236	2	2	2	53	2	2	99		
1237	1	2	1	1	13	1	148		
1238	17	45	23	10	81	13	20		
1239	2	156	98	2	2	2	2		
1240	2	2	2	2	2	50	148		
1241	41	42	13	1	9	4	14		
1242	23	2	23	16	25	18	26		
1243	1	2	1	1	9	1	2		
1244	2	2	23	55	2	2	2		
1245	2	2	2	2	114	2	96		
1246	5	1	1	1	9	1	1		
1247	1	142	2	1	137	4	117		
1248	1	160	2	1	137	24	2		
1249	2	2	150	2	171	2	57		
1250	1	158	2	1	137	1	148		
1251	188	181	174	88	186	22	33		
1252	1	52	18	2	73	99	4		
1253	2	2	2	2	2	2	162		
1254	22	26	54	14	23	16	49		
1255	22	26	90	14	167	16	23		
1256	189	55	175	50	187	66	163		
1257	190	182	66	10	188	18	164		
1258	191	183	176	89	189	100	165		
1259	22	26	90	90	23	16	49		
1260	59	24	177	14	23	16	23		
1261	22	26	178	14	27	16	47		
1262	192	26	91	14	50	16	47		
1263	22	26	161	18	23	19	47		
1264	22	26	90	14	23	16	49		
1265	22	26	90	18	27	16	40		
1266	83	86	79	78	88	23	77		
1267	59	26	59	14	50	16	47		A. nosocomialis
1268	47	47	50	14	26	16	47		A. nosocomialis
1269	20	184	26	14	61	16	23		A. nosocomialis
1270	20	184	26	14	61	16	91		A. nosocomialis
1271	49	26	54	18	27	16	117		A. nosocomialis
1272	83	26	79	14	27	16	47		
1273	49	26	54	18	27	16	167		
1274	20	185	179	18	191	16	47		
1275	22	26	54	14	191	16	118		
1276	192	26	91	14	192	16	47		
1277	193	33	34	23	190	23	70		
1278	1	52	2	2	9	4	5		
1279	1	3	2	1	3	1	14		
1280	3	63	2	2	29	1	5		
1281	185	178	170	39	182	41	160		
1282	1	88	14	1	12	1	2		
1283	182	173	173	39	178	41	71		
1284	132	21	44	86	20	18	20		
1285	115	179	171	67	183	18	20		
1286	1	3	2	2	13	2	5		
1287	3	2	5	1	3	1	14		
1288	186	180	172	87	184	98	32		
1289	1	52	2	2	73	4	5		
1290	1	8	2	6	4	1	158		
1291	187	34	34	23	185	23	161		
1292	1	174	2	2	13	2	5		
1293	1	175	2	2	73	1	5		
1294	64	5	166	2	9	1	4		
1295	3	50	15	2	4	1	4		
1296	3	176	2	2	180	4	5		
1297	184	1	7	6	3	1	5		
1298	3	52	2	85	181	4	4		
1299	1	3	2	1	2	4	5		
1300	5	1	101	2	2	2	5		
1301	3	3	2	6	51	1	14		
1302	64	52	2	2	9	4	4		
1303	3	3	16	1	13	1	15		
1304	22	26	26	14	23	16	168		
1305	22	26	177	14	193	16	47		
1306	29	26	54	18	27	2	117		
1307	83	86	79	46	88	23	166		
1308	83	26	79	47	27	16	47		
1309	194	186	180	91	194	101	169		A. bereziniae
1310	8	1	5	1	6	2	3		
1311	1	52	2	1	9	4	5		
1312	2	6	181	2	2	2	2		
1313	2	2	182	2	2	2	2		
1314	1	3	67	2	195	2	5		
1315	181	187	183	63	196	56	97		
1316	195	188	184	92	197	102	170		
1317	196	186	185	91	198	101	171		
1318	198	190	180	91	199	104	173		
1319	199	186	180	91	194	101	174		
1320	78	191	71	94	82	22	68		
1321	3	1	56	2	56	4	2		
1322	3	41	6	1	3	3	5		
1323	3	3	2	1	3	3	2		
1324	3	1	2	1	59	1	2		
1325	26	3	2	2	29	4	5		A. baumannii
1326	22	26	54	14	58	16	47		
1327	13	1	5	26	7	1	29		
1328	3	3	2	2	200	4	5		
1329	23	20	28	10	25	18	62		
1330	17	21	23	10	20	13	62		
1331	171	58	46	29	72	18	58		
1332	33	33	34	23	80	18	20		
1333	106	20	119	65	144	36	111		
1334	200	124	53	16	55	36	55		
1335	137	20	132	67	25	105	46		
1336	1	3	40	2	7	1	1		
1337	3	4	5	2	7	1	2		
1338	50	3	56	2	3	4	4		
1339	13	3	2	3	7	1	29		
1340	22	184	26	14	61	16	23		
1341	60	21	46	10	20	13	56		
1342	60	76	48	67	72	18	98		
1343	111	170	183	57	110	56	97		
1344	25	3	6	2	28	1	4		
1345	198	190	2	2	194	104	173		
1346	205	193	190	96	204	107	178		
1347	206	194	191	97	205	108	179		
1348	201	192	132	67	202	18	175		
1349	111	170	188	63	110	56	176		
1350	196	186	185	91	198	106	171		
1351	61	89	82	23	203	23	85		
1352	202	20	189	67	20	18	122		
1353	203	170	183	95	110	56	177		
1354	12	3	5	2	5	1	14		
1355	156	2	2	2	9	1	2		
1356	3	1	2	2	9	1	5		
1357	1	100	2	2	9	1	52		
1358	1	3	2	5	3	1	14		
1359	27	2	2	7	5	4	14		
1360	1	3	17	2	3	1	14		
1361	3	2	2	2	5	4	14		
1362	27	4	2	2	7	1	2		
1363	3	3	7	2	9	4	5		
1364	3	1	2	5	29	1	4		
1365	6	3	2	2	5	2	2		
1366	1	12	11	2	15	9	14		
1367	1	2	2	1	9	1	4		
1368	25	1	2	3	169	1	2		
1369	9	195	2	2	4	1	4		
1370	1	3	192	1	4	4	4		
1371	9	195	7	2	4	1	4		
1372	208	2	3	2	2	110	4		
1373	3	3	2	2	206	4	14		
1374	209	3	3	2	29	110	8		
1375	3	199	7	1	7	1	4		
1376	207	2	7	5	11	1	14		
1377	3	196	101	2	3	1	14		
1378	3	3	7	2	4	2	180		
1379	1	197	193	2	18	2	5		
1380	1	198	6	2	3	1	54		
1381	27	88	167	5	207	109	2		
1382	1	53	3	2	208	9	14		
1383	1	201	193	2	9	2	5		
1384	1	3	194	2	4	4	5		
1385	12	200	5	2	5	1	14		
1386	3	3	2	4	5	4	63		
1387	3	1	1	1	5	1	41		
1388	204	20	195	10	183	18	65		
1389	210	76	196	98	209	36	181		
1390	211	110	106	62	117	60	103		
1391	24	45	46	29	210	30	46		
1392	203	102	197	57	110	56	182		
1393	212	186	180	91	198	111	183		
1394	213	31	74	99	211	22	73		
1395	214	170	95	57	121	56	97		
1396	203	187	183	63	110	56	97		
1397	215	202	198	100	212	112	184		
1398	216	203	199	100	212	112	185		
1399	22	26	200	14	213	16	25		
1400	217	202	201	100	212	112	186		
1401	218	204	202	100	214	112	187		
1402	219	205	203	101	215	113	188		
1403	220	205	203	101	216	113	189		
1404	221	206	204	102	212	112	90		
1405	3	5	5	26	7	1	4		
1406	1	3	2	1	137	4	92		
1407	7	190	2	2	8	82	123		
1408	56	3	2	3	9	35	4		
1409	40	3	4	2	40	4	4		Acinetobacter baumannii
1410	40	3	2	1	2	2	2		
1411	152	5	7	1	7	1	4		
1412	13	5	5	1	7	1	4		
1414	3	3	6	2	3	1	2		
1416	3	3	2	2	2	4	14		
1417	3	3	2	2	9	2	2		
1418	3	2	2	2	3	1	2		
1419	156	3	56	1	13	1	1		
1421	69	4	2	2	7	1	4		
1422	3	3	2	5	29	1	4		
1423	1	2	1	1	28	1	2		
1424	25	3	6	2	5	1	1		
1425	1	5	2	2	217	1	8		
1426	3	16	13	2	71	2	4		
1427	1	3	11	5	3	4	14		
1428	1	100	2	2	9	115	52		
1429	3	3	19	25	5	2	5		
1430	1	56	2	1	3	1	4		
1431	3	3	2	2	5	58	5		
1432	3	39	5	6	41	1	14		
1433	3	1	5	3	6	2	3		
1434	1	1	1	2	28	1	25		
1435	105	3	2	1	4	2	4		
1436	3	3	2	2	3	1	29		
1437	3	3	7	108	7	1	5		
1438	3	8	2	2	226	1	14		
1439	3	1	1	1	5	4	1		
1440	1	5	40	2	7	1	14		
1441	5	2	7	2	7	1	3		
1442	8	1	2	1	9	1	4		
1443	1	49	7	3	12	1	5		
1444	3	2	148	1	137	1	5		
1445	3	3	17	1	137	1	4		
1446	1	2	11	54	9	1	2		
1447	6	6	8	103	3	5	4		
1448	3	3	2	4	7	114	4		
1449	2	2	2	2	67	2	2		
1450	3	49	210	2	5	1	4		
1451	36	20	38	16	20	18	27		
1452	224	209	207	106	222	118	196		
1453	36	20	38	16	218	18	27		
1454	225	210	208	104	221	116	193		
1455	226	211	209	105	219	117	196		
1456	3	2	2	109	7	1	5		
1457	8	4	5	2	7	2	3		
1458	3	3	2	2	3	2	197		
1459	3	4	2	2	7	2	4		
1460	1	3	17	5	168	1	14		
1461	3	3	16	1	3	2	4		
1462	27	4	2	3	6	1	16		
1463	8	1	5	3	7	1	3		
1464	3	4	2	2	7	2	2		
1465	5	1	2	2	7	9	4		
1466	26	199	2	2	29	4	5		
1467	8	1	5	5	6	2	5		
1468	227	2	2	2	7	1	5		
1469	3	4	2	1	42	2	5		
1470	3	69	11	2	9	2	2		
1471	8	52	5	2	9	4	2		
1472	3	1	5	26	13	2	3		
1473	228	215	211	110	231	46	200		
1474	2	2	2	2	2	2	201		
1475	1	1	1	1	5	123	1		Acinetobacter baumannii
1476	8	1	14	3	6	2	3		Acinetobacter baumannii
1477	2	2	7	2	2	2	2		
1478	40	3	2	2	40	4	4		
1479	40	3	212	2	40	4	4		
1480	7	216	2	2	8	4	4		
1481	5	2	2	7	227	1	5		
1482	3	12	11	2	228	9	14		
1483	1	3	2	1	137	4	4		
1484	8	1	7	1	7	1	29		
1485	230	214	214	111	229	122	199		
1486	229	213	213	1	230	121	198		
1487	8	1	16	3	6	2	3		Acinetobacter baumannii
1488	5	3	2	5	65	1	4		Acinetobacter baumannii
1489	231	217	215	23	35	23	202		
1490	83	86	216	46	88	23	77		
1491	83	86	34	46	232	23	77		
1492	33	33	34	32	80	18	203		
1493	61	218	60	23	233	23	78		
1494	232	89	34	23	190	23	204		
1495	83	86	79	46	234	23	77		
1496	83	86	215	46	88	23	77		
1497	233	33	34	23	235	23	205		
1498	234	219	34	23	160	124	85		
1499	159	33	34	23	190	23	70		
1500	159	33	34	23	190	23	85		
1501	235	33	34	23	235	125	70		
1502	236	218	60	23	89	23	206		
1503	196	186	185	91	225	101	169		
1504	237	207	205	107	224	119	194		
1505	223	208	206	1	223	120	195		
1506	1	3	2	1	236	4	92		
1507	27	1	5	3	6	1	3		
1508	3	2	3	1	4	9	135		
1509	3	16	6	1	74	2	5		
1510	1	3	10	1	4	1	29		
1511	3	1	2	4	51	2	5		
1512	1	3	10	1	4	1	4		
1513	1	3	2	1	71	4	207		
1514	3	49	56	2	9	1	29		
1515	3	3	7	2	73	4	2		
1516	2	2	2	2	2	1	1		
1517	1	2	1	1	5	2	1		
1518	26	2	1	1	5	2	1		
1519	1	2	1	2	2	1	1		
1520	25	3	5	2	5	4	5		
1521	1	39	1	1	5	1	1		
1522	1	3	2	5	4	1	4		
1523	238	220	34	23	237	23	77		
1524	239	221	85	112	238	126	83		
1525	3	49	2	2	9	1	5		
1526	1	52	2	2	67	1	2		
1527	203	170	95	57	110	56	211		
1528	240	118	28	10	25	18	20		
1529	243	43	191	19	240	70	212		
1530	61	33	220	23	160	23	34		
1531	240	223	219	104	213	119	213		
1532	2	2	2	114	2	2	2		
1533	2	2	2	115	2	2	2		
1534	6	6	8	2	3	5	215		
1535	169	1	2	2	171	1	4		
1536	245	224	221	113	243	128	214		
1537	2	2	222	2	2	2	2		
1538	2	2	222	2	2	86	2		
1539	47	26	50	14	26	16	49		
1540	241	222	217	106	239	127	216		
1541	242	223	218	104	242	116	193		
"""
def read_fasta(filename):
    dna = []
    sequences = []
    with open(filename) as file:    
        seq = ''        
        #for loop through the lines
        for line in file: 
            header = re.search(r'^>\w+', line)
            #if line contains the header '>' then append it to the dna list 
            if header:
                # Append sequence in the list
                if seq:
                    sequences.append(seq)
                
                line = line.rstrip("\n")
                dna.append(line)
                # Start counting for a new sequence
                seq = ''
            else:               
                seq += line.replace('\n', '')
    return dna, sequences

# Preparing the dataframe with all STs
## Split into lines
z = x.splitlines()
## Turn the mess into a nice dataframe
df = pd.DataFrame([x.split('\t') for x in z], columns=("ST",
                                                       "cpn60",
                                                       "fusA",
                                                       "gltA",
                                                       "pyrG",
                                                       "recA",
                                                       "rplB",
                                                       "rpoB",
                                                       "clonal_complex",
                                                       "species"))
## Ignoring the first row which just contains headers
df = df[1:-1]
## The user inputs the ST they need
print("Please enter ST number:")
input = input()
input = int(input)
## The program goes for that row and takes the alelle numbers
## Then saves them into a single-row dataframe (stype)
stype = df[input-1:input]

import sys
filename = sys.argv[1:8]
print(filename)

def concatenator(file_name):
    concat = '' 
    for genefile in file_name:
        dna, sequences = read_fasta(genefile)
        dna = dna[1:len(dna)]
        d = {'Allele':dna, 'Sequence':sequences}
        df = pd.DataFrame(d)
        df.index += 1
        gene_name = genefile.replace("Pas_", "").replace(".fas", "")
        concat += df["Sequence"][int(stype[gene_name][0:2])]

    return(concat)


print("Here's for ST", input)
print(concatenator(filename))