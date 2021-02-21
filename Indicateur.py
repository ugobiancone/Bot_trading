"""
Function
"""
#retourn le SMA sur num minutes
def SMA(data,num):
    m = 0.0
    d2 = data['Close'].tail(num).to_numpy()
    for i in range(num):
        m = m+d2[i]
    m = m/num
    print(m)
    return m