import matplotlib.pyplot as plt
money=[55959,222525,225292,228854,151524]
type=["1號","2號","3號","4號","5號"]
plt.rcParams["font.family"]="Microsoft JhengHei"
plt.bar(type,money,color="b")
plt.title("我亂做的")
plt.grid(True)
plt.show()
