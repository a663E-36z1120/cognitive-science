import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from scipy.stats import norm

x = np.arange(-3, 8, 0.01)

pet_mu = -1
pet_sigma = 1.2
typical_pet = np.arange(pet_mu-0.2, pet_mu+0.2, 0.01)

def pet_gaussian(domain):
    return norm.pdf(domain, loc=pet_mu, scale=pet_sigma)

fish_mu = 1
fish_sigma = 1.2
typical_fish = np.arange(fish_mu-0.2, fish_mu+0.2, 0.01)

def fish_gaussian(domain):
    return norm.pdf(domain, loc=fish_mu, scale=fish_sigma)


petFish_mu = 0
typical_petFish = np.arange(petFish_mu-0.2, petFish_mu+0.2, 0.01)

def petFish_gaussian(domain):
    return (pet_gaussian(domain) + fish_gaussian(domain)) / 2


fig, ax = plt.subplots()

plt.plot(x, pet_gaussian(x),
         label='Distribution of Concrete Pet Exemplars')
plt.fill_between(typical_pet, pet_gaussian(typical_pet), alpha=0.5,
                 label='Domain of ''Typical Pets''')

plt.plot(x, fish_gaussian(x),
         label='Distribution of Concrete Fish Exemplars')
plt.fill_between(typical_fish, fish_gaussian(typical_fish), alpha=0.5,
                 label='Domain of ''Typical Fish''')

plt.plot(x, petFish_gaussian(x), color='purple',
         label='Mixed Distribution of Concrete\nPet-fish Exemplars')
plt.fill_between(typical_petFish, petFish_gaussian(typical_petFish),
                 color='purple', alpha=0.5,
                 label='Domain of ''Typical Pet-fish''')

h, l = plt.gca().get_legend_handles_labels()
h[0], h[1], h[2], h[3], h[4], h[5] = h[0], h[3], h[1], h[4], h[2], h[5]
l[0], l[1], l[2], l[3], l[4], l[5] = l[0], l[3], l[1], l[4], l[2], l[5]

plt.title("1D Gaussian Mixture Modelling of the Pet-fish Problem")
plt.legend(h, l, prop={'size': 7})
plt.xlabel('Degrees of ''Possession'' of an Arbitrary Feature (in Arbitrary Units)')
plt.ylabel('Degree of Conceptual Category Membership\n(Probability Density)')

plt.ylim((0, 0.43))

pet = mpimg.imread('pet.jpg')
newax = fig.add_axes([0.2,0.71,0.1,0.1], anchor='NE', zorder=1)
newax.axis('off')
newax.annotate('Prototypical\nPet: Dog', (0,0))
newax.imshow(pet)

petFish = mpimg.imread('petFish.jpg')
newax1 = fig.add_axes([0.285,0.54,0.1,0.1], anchor='NE', zorder=1)
newax1.axis('off')
newax1.annotate('Prototypical\nPet-fish: Goldfish', (0,0))
newax1.imshow(petFish)

fish = mpimg.imread('fish.png')
newax = fig.add_axes([0.37,0.7,0.1,0.1], anchor='NE', zorder=1)
newax.axis('off')
newax.annotate('Prototypical\nFish: Tuna', (0,0))
newax.imshow(fish)

plt.savefig('pet-fish.png')
plt.show()


