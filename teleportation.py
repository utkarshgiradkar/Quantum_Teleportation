#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import random_statevector


# In[2]:


import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.result import marginal_counts
from qiskit.quantum_info import random_statevector


# In[3]:


qr = QuantumRegister(3, name="q")
crz, crx = ClassicalRegister(1, name="crz"), ClassicalRegister(1, name="crx")


# In[4]:


psi = random_statevector(2)
display(array_to_latex(psi, prefix="|\\psi\\rangle ="))


# In[5]:


tel=QuantumCircuit(qr, crz, crx)
tel.append(Initialize(psi),[0])
tel.h(1)
tel.cx(1,2)
tel.barrier()
tel.cx(0,1)
tel.barrier()
tel.h(0)
tel.barrier()
tel.measure(0,0)
tel.measure(1,1)
tel.barrier()
tel.x(2).c_if(crx, 1) 
tel.z(2).c_if(crz, 1) 
tel.draw()


# In[6]:


sim = Aer.get_backend('aer_simulator')
tel.save_statevector()
out_vector = sim.run(tel).result().get_statevector()
display(array_to_latex(out_vector, prefix="|\\psi\\rangle ="))
plot_bloch_multivector(out_vector)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




