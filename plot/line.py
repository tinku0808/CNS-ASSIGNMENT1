import matplotlib.pyplot as plt
year=[1920,11930,1940,1950,1960,1970,1980,1990,2000]
unem=[9.8,12,2.2,2,4,5,6,7,8]

plt.plot(year,unem,marker='o')
plt.xlabel("year")
plt.ylabel("unem")
plt.title("year vs unemply rate")
plt.show()
