import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def allowance(x):
    """
    https://www.nta.go.jp/taxanswer/shotoku/1410.htm
    Refer to the above URL.
    :param x:給与収入(Allowance)
    :return: 給与控除(Payroll Deduction)
    """
    # "Return"  depends on which range the "x" is in.
    if 0 <= x < 180:
        y_value = x * 0.4
        if y_value < 65.0:
            return 65
        elif y_value > 65.0:
            return y_value
        else:
            pass

    elif 180 <= x < 360:
        y_value = x * 0.3 + 18
        return y_value

    elif 360 <= x < 660:
        y_value = x * 0.2 + 54
        return y_value

    elif 660 <= x < 1000:
        y_value = x * 0.1 + 120
        return y_value

    elif 1000 <= x :
        return 220
    else:
        pass


x = []
y = []
z = []

for i in range(1100):
    x.append(i)
    y.append(allowance(i))
    z.append((y[i]/(x[i]+0.00001))*100)

for i in range(65):
    z[i] = 100

plt.xlabel("Allowance(*10000yen)")
plt.ylabel("Payroll Deduction(*10000yen),  Ratio(DottedLine)")
plt.ylim(0,230)
plt.plot(x, y, 'g^', x, z, 'r--')
plt.show()

