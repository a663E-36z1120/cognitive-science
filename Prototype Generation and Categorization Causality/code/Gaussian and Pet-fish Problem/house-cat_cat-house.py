import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from scipy.stats import norm

x = np.arange(-4, 11, 0.01)

cat_mu = -2
cat_sigma = 1.7
typical_cat = np.arange(cat_mu - 0.1, cat_mu + 0.1, 0.01)

def cat_gaussian(domain):
    return norm.pdf(domain, loc=cat_mu, scale=cat_sigma)

house_mu = 2
house_sigma = 1.7
typical_house = np.arange(house_mu - 0.1, house_mu + 0.1, 0.01)

def house_gaussian(domain):
    return norm.pdf(domain, loc=house_mu, scale=house_sigma)

catHouse_median = 1.7
typical_catHouse = np.arange(catHouse_median - 0.1, catHouse_median + 0.1, 0.01)
houseCat_median = -1.7
typical_houseCat = np.arange(houseCat_median - 0.1, houseCat_median + 0.1, 0.01)

def catHouse_gaussian(domain):
    return (cat_gaussian(domain) + house_gaussian(domain)) / 2


fig, ax = plt.subplots()


plt.plot(x, cat_gaussian(x),
         label='Distribution of Concrete Cat Exemplars')
plt.fill_between(typical_cat, cat_gaussian(typical_cat), alpha=0.5,
                 label='Domain of ''Typical Cat''')

plt.plot(x, house_gaussian(x),
         label='Distribution of Concrete House Exemplars')
plt.fill_between(typical_house, house_gaussian(typical_house), alpha=0.5,
                 label='Domain of ''Typical House''')

plt.plot(x, catHouse_gaussian(x), color='purple',
         label='Distribution of Cat and House\nCompound Concepts')
plt.fill_between(typical_catHouse, catHouse_gaussian(typical_catHouse),
                 color='maroon', alpha=0.5,
                 label='Domain of ''Typical Cat-house''')
plt.fill_between(typical_houseCat, catHouse_gaussian(typical_houseCat),
                 color='red', alpha=0.5,
                 label='Domain of ''Typical House-cat''')

h, l = plt.gca().get_legend_handles_labels()
h[0], h[1], h[2], h[3], h[4], h[5] = h[0], h[3], h[1], h[4], h[2], h[5]
l[0], l[1], l[2], l[3], l[4], l[5] = l[0], l[3], l[1], l[4], l[2], l[5]

plt.title("One-dimensional Gaussian Modelling of Cat and House \n"
          "Compound Concept")
plt.legend(h, l, prop={'size': 7})
plt.xlabel('Degrees of ''Possession'' of an Arbitrary Feature (in Arbitrary Units)')
plt.ylabel('Degree of Conceptual Category Membership\n(Probability Density)')
plt.ylim((0, 0.3))


cat = mpimg.imread('cat.jpg')
newax = fig.add_axes([0.2,0.71,0.11,0.11], anchor='NE', zorder=1)
newax.axis('off')
newax.annotate('Prototypical\nCat', (0,0))
newax.imshow(cat)

houseCat = mpimg.imread('houseCat.jpg')
newax1 = fig.add_axes([0.20,0.45,0.12,0.12], anchor='NE', zorder=1)
newax1.axis('off')
newax1.annotate('Prototypical\nHouse-cat', (0,0))
newax1.imshow(houseCat)

catHouse = mpimg.imread('catHouse.jpg')
newax2 = fig.add_axes([0.376,0.45,0.12,0.12], anchor='NE', zorder=1)
newax2.axis('off')
newax2.annotate('Prototypical\nCat-house', (0,0))
newax2.imshow(catHouse)

house = mpimg.imread('house.jpg')
newax3 = fig.add_axes([0.39,0.72,0.1,0.1], anchor='NE', zorder=1)
newax3.axis('off')
newax3.annotate('Prototypical\nHouse', (0,0))
newax3.imshow(house)

plt.draw()

plt.savefig("house-cat_cat-house.png")
plt.show()


