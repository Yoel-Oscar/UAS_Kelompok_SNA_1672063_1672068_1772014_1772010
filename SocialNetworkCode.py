#!/usr/bin/env python
# coding: utf-8

# In[159]:


import networkx as nx
G_symmetric = nx.Graph()
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR','Penanya 180 JONG TIMO')
G_symmetric.add_edge('Penjawab 163 ALDI TAHIR',' Penanya 185 ROBBY SETIAN')         
G_symmetric.add_edge('Penjawb 163 ALDI TAHIR',' Penanya 186 FAQIH SALBAN')
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 189 RIAN')
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 191 TAN TAN RHMAN')
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 197 MATTHEW')
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 203 WELLY')
G_symmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 220 ZANANG')


G_symmetric.add_edge('Penjawab 185 ROBBY SETIAN',' Penanya 179 Anonim-Linked-in')
G_symmetric.add_edge('Penjawab 174 PETER SURYA','Penanya 182 HENDRA')
G_symmetric.add_edge('Penjawab 174 PETER SURYA',' Penanya 171 FELIX ALFERDO')
G_symmetric.add_edge('Penjawab 174 PETER SURYA','Penanya 220 ZANANG')
G_symmetric.add_edge('Penjawab 189 RIAN','Penanya 300 MHS')
G_symmetric.add_edge('Penjawab 171 FELIX ALFERDO','Penanya300 MHS')

nx.draw_networkx(G_symmetric)


# In[160]:


G_asymmetric = nx.DiGraph()
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR','Penanya 180 JONG TIMO')
G_asymmetric.add_edge('Penjawab 163 ALDI TAHIR',' Penanya 185 ROBBY SETIAN')         
G_asymmetric.add_edge('Penjawb 163 ALDI TAHIR',' Penanya 186 FAQIH SALBAN')
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 189 RIAN')
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 191 TAN TAN RHMAN')
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 197 MATTHEW')
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 203 WELLY')
G_asymmetric.add_edge(' Penjawab 163 ALDI TAHIR',' Penanya 220 ZANANG')


G_asymmetric.add_edge('Penjawab 185 ROBBY SETIAN',' Penanya 179 Anonim-Linked-in')
G_asymmetric.add_edge('Penjawab 174 PETER SURYA','Penanya 182 HENDRA')
G_asymmetric.add_edge('Penjawab 174 PETER SURYA',' Penanya 171 FELIX ALFERDO')
G_asymmetric.add_edge('Penjawab 174 PETER SURYA','Penanya 220 ZANANG')
G_asymmetric.add_edge('Penjawab 189 RIAN','Penanya 300 MHS')
G_asymmetric.add_edge('Penjawab 171 FELIX ALFERDO','Penanya300 MHS')


# In[161]:


nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)


# In[152]:


G_weighted = nx.Graph()
G_weighted.add_edge('ALDI TAHIR','JONG TIMO', weight=25)
G_weighted.add_edge('ALDI TAHIR','ROBBY SETIAN', weight=8)
G_weighted.add_edge('ALDI TAHIR','FAQIH SALBA', weight=11)
G_weighted.add_edge('ALDI TAHIR','RIAN', weight=1)
G_weighted.add_edge('ALDI TAHIR','TAN TAN RAHMAN', weight=4)
G_weighted.add_edge('ALDI TAHIR','MATTHEW', weight=4)

G_weighted.add_edge('ROBBY SETIAN','Anonim-Linked-in', weight=20)
G_weighted.add_edge('PETER SURYA',' HENDRA', weight=16)
G_weighted.add_edge('PETER SURYA',' FELIX ALFERDO', weight=5)
G_weighted.add_edge('PETER SURYA',' ZANANG', weight=7)

G_weighted.add_edge('RIAN',' MHS', weight=15)
G_weighted.add_edge('FELIX ALFERDO',' MHS', weight=13)


# In[156]:


nx.draw_networkx(G_weighted)

