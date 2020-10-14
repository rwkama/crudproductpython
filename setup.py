from distutils.core import setup
setup(
  name = 'DataProduct',         # How you named your package folder (MyLib)
  packages = ['DataProduct','conection','entity'],   
  version = '0.12', 
  long_description=README,
  long_description_content_type="text/markdown",
  license='MIT',
  include_package_data=True,        #
  description = 'this pip contains a crud of a Product entity',   # Give a short description about your library
  author = 'Carlos Rodriguez',                   # Type in your name
  author_email = 'rwkamandriw@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/rwkama/crudproductpython',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/rwkama/crudproductpython/archive/v_12.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pip',
          'pypyodbc',
          'setuptools',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
