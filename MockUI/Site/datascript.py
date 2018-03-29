import os, random, string
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MockUI.settings")

PRODUCTNAMES = ['ranch', 'tubular socks', 'tshirt', 'yeezys']
PRODUCTTYPES = ['socks', 'shoes', 'shirt', 'gloves', 'energy pizza']
SIZES = ['XS', 'S', 'M', 'L', 'XL']
IMAGES = ['']

STORES = ['American Eagle', 'Hollister', 'H and M']


# your imports, e.g. Django models
from models import *

def main():
	AE = Store()
	H = Store()
	HM = Store()

	for i in range(0,100):
		product = Product()
		product.product_type = PRODUCTTYPES[random.randrange(len(PRODUCTTYPES))]
		product.name = PRODUCTNAMES[random.randrange(len(PRODUCTNAMES))]
		product.source = STORES[random.randrange(len(STORES))]
		product.size_type = random.randrange(2)
		product.size_primary = SIZES[random.randrange(len(SIZES))]
		product.size_secondary = SIZES[random.randrange(len(SIZES))]

		product.save()

		if i < 30:
			AE.products += product
		elif i < 70:
			H.products += product
		else:
			HM.product += product

	for i in range(0,25):
		coupon = Coupon()
		coupon.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
		coupon.description = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
		coupon.discount = random.randrange(30)

		coupon.save()

		if i < 10:
			AE.products += product
		elif i < 20:
			H.products += product
		else:
			HM.product += product


	AE.save()
	H.save()
	HM.save()


if __name__ == '__main__':
	main()
