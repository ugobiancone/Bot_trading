"""
Function
"""
#retourn le SMA sur num minutes
def SMA(data,num):
    n = num
    m = 0.0
    d2 = data['Close'].tail(n).to_numpy()
    for i in range(n):
        m = m+d2[i]
    m = m/n
    print(m)
    return m