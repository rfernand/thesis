#!/usr/bin/python

# Numpy is a library for handling arrays (like data points)
import numpy as np

# Pyplot is a module within the matplotlib library for plotting
import matplotlib.pyplot as plt

import math as m


def m_graph(formula, x_range, filename, title):
  x = np.array(x_range)  
  y = formula(x)
  plt.ylabel('Overhead Messages cost')
  plt.xlabel('Leafset size L')
  plot = plt.plot(x, y, 'r', marker="o")  
  plt.ylim(min(y), max(y))
  plt.xlim(min(x_range), max(x_range))
  plt.xticks([0,8,16,32])
  plt.yticks([formula(0),formula(8),formula(16),formula(32)])
  plt.autoscale(False)

  # LOL
  #plt.xkcd(True)

  #plt.legend(plot, title, loc='lower left')
  #plt.plot(x_range, y, 'r')  
  
  #plt.annotate(str(j), xy=(i,j), xytext=(10,10), textcoords='offset points')
# Turn on a grid
  plt.grid(True)
  plt.savefig(filename)
  plt.show()

#fail probability


#message complexity

N = 100000

# secure routing
def secure_routing(x):
  Q = x
  return 5 * m.log(N, 10) + Q

m_graph(secure_routing, range(1,33),
#graph("5 * m.log(N, 10) + x", [0, 8, 16, 32],
  "secure_routing_messages.png",
  "Secure routing messages costs")


# account registration
def account_registration(x):
  return 5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6
m_graph(account_registration, range(1,33),
#graph("5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6", [0, 8, 16, 32],
  "account_registration_messages.png",
  "Account registration messages costs")


# sign in 
def sign_in(x, q=8):
  L = x
  Q = q
  return (L+2)*(5 * m.log(N, 10) + Q + 4) + 4 * L ** 2  + 12 * L + 8
m_graph(sign_in, range(1,33),
#graph("5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6", [0, 8, 16, 32],
  "sign_in_messages.png",
  "Sign in messages costs")


# logout
def logout(x, q=8):
  L = x
  Q = q
  return (5 * m.log(N, 10) + Q + 4) + 4 * (L + 1)
m_graph(logout, range(1,33),
#graph("5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6", [0, 8, 16, 32],
  "logout_messages.png",
  "Logout messages costs")


# password change
def password_change(x, q=8):
  L = x
  Q = q
  return 5 * m.log(N, 10) + Q + 4 +  L ** 2 + 4 * L + 3
m_graph(password_change, range(1,33),
#graph("5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6", [0, 8, 16, 32],
  "password_change_messages.png",
  "Password change messages costs")


# Private key recovery 
def recovery_a(x, q=8):
  L = x
  Q = q
  return 5 * m.log(N, 10) + Q + 4 + 4 * L + 4
m_graph(recovery_a, range(1,33),
#graph("5 * m.log(N, 10) + 2  * x ** 2 + 8 * x + 6", [0, 8, 16, 32],
  "private_key_recovery_a_messages.png",
  "Private key recovery protocol A messages costs")

