# Crud Product Python


This package contains a crud of a Product entity with id (int) and image url (string) attributes

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install DataProduct.

```bash
pip install DataProduct
```

## Usage

```python
from DataProduct import DataProduct

list=DataProduct.getProducts()
for x in list: 
  print("------------")
  print(x.id)
  print("------------")
  print(x.image)
  print("------------")


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)