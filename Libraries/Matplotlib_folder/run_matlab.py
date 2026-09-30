import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
companies = ['Meta', 'Amazon', 'Apple', 'Netflix', 'Google', 'SapceX', 'Tesla', 'Youtube', 'MI', 'OpenAI', 'Uber']
share = [0.12, 0.16, 0.22, 0.04, 0.18, 0.05, 0.08, 0.06, 0.02, 0.04, 0.03]
plt.title('Share by Companies')
plt.subplot(1,2,1)
plt.pie(share, labels=companies, autopct='%.1f%%')


months = ['Jan', 'Feb', 'March', 'April', 'May']
sales = [23000, 31512, 17903, 45094, 21436]
plt.xlabel('months')
plt.ylabel('sales')
plt.subplot(1,2,2)
plt.plot(months, sales, marker = 'o', color = 'b', linestyle = '--')

plt.show()